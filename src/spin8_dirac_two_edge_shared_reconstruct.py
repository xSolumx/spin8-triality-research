"""Crash-safe shared-grid reconstruction of all eight two-edge sectors."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp

from spin8_dirac_star import rational_circle
from spin8_dirac_two_edge import exact_normalized_determinant
from spin8_dirac_two_edge_amplitude import exact_extended_chart_sign_certificate
from spin8_dirac_two_edge_degree import _sector_setup

VARIABLE_ORDER = ("a2", "d2", "e2", "g2", "i2", "c2")
NODE_SETS = {
    "alpha": (
        sp.Rational(1, 7),
        sp.Rational(2, 9),
        sp.Rational(3, 11),
        sp.Rational(4, 13),
        sp.Rational(5, 17),
    ),
    "beta": (
        sp.Rational(1, 8),
        sp.Rational(2, 11),
        sp.Rational(3, 13),
        sp.Rational(4, 15),
        sp.Rational(5, 19),
    ),
}
DEGREE_BOUNDS = {
    (0, 0, 0, 0, 0, 0): (4, 4, 4, 4, 4, 4),
    (0, 0, 1, 1, 0, 1): (4, 4, 3, 3, 3, 3),
    (0, 1, 0, 1, 1, 0): (4, 3, 3, 3, 3, 4),
    (0, 1, 1, 0, 1, 1): (4, 3, 3, 4, 3, 3),
    (1, 0, 0, 0, 1, 1): (3, 4, 4, 4, 3, 3),
    (1, 0, 1, 1, 1, 0): (3, 4, 3, 3, 3, 4),
    (1, 1, 0, 1, 0, 1): (3, 3, 3, 3, 3, 3),
    (1, 1, 1, 0, 0, 0): (3, 3, 3, 4, 4, 4),
}


def _digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def _mask_text(mask: tuple[int, ...]) -> str:
    return "".join(map(str, mask))


@lru_cache(maxsize=1)
def _shared_setup():
    masks, signs, inverse = _sector_setup()
    chart = exact_extended_chart_sign_certificate()
    complements = {
        tuple(row["lower_mask"]): tuple(row["complement_mask"])
        for row in chart["chart_characters"]
    }
    if set(masks) != set(DEGREE_BOUNDS) or set(masks) != set(complements):
        raise AssertionError("shared-grid sector metadata is incomplete")
    return masks, signs, inverse, complements


def _shared_point_worker(job):
    multi_index, parameters, masks, signs, inverse, complements = job
    determinants = sp.Matrix(
        [exact_normalized_determinant(parameters, sign_row) for sign_row in signs]
    )
    sectors = inverse * determinants
    pairs = tuple(rational_circle(value) for value in parameters)
    residuals = []
    for mask, sector in zip(masks, sectors, strict=True):
        complement_mask = complements[mask]
        forced = pairs[-1][1] ** 6
        forced *= sp.prod(
            pair[0] ** lower_bit * pair[1] ** complement_bit
            for pair, lower_bit, complement_bit in zip(
                pairs, mask, complement_mask, strict=True
            )
        )
        residuals.append(str(sp.factor(sector / forced)))
    return multi_index, residuals


def evaluate_tile(
    *, node_set: str, tile_a: int, tile_d: int, workers: int
) -> dict[str, object]:
    masks, signs, inverse, complements = _shared_setup()
    nodes = NODE_SETS[node_set]
    if tile_a not in range(5) or tile_d not in range(5):
        raise ValueError("tile indices must be between 0 and 4")
    indices = [
        (tile_a, tile_d, *tail) for tail in itertools.product(range(5), repeat=4)
    ]
    jobs = [
        (
            index,
            tuple(nodes[position] for position in index),
            masks,
            signs,
            inverse,
            complements,
        )
        for index in indices
    ]
    if workers == 1:
        evaluated = list(map(_shared_point_worker, jobs))
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            evaluated = list(pool.map(_shared_point_worker, jobs, chunksize=2))
    rows = [
        {"multi_index": list(index), "sector_residuals": residuals}
        for index, residuals in sorted(evaluated)
    ]
    return {
        "experiment": "two-edge all-sector exact shared-grid tile",
        "node_set": node_set,
        "nodes": [str(value) for value in nodes],
        "squared_nodes": [str(rational_circle(value)[0] ** 2) for value in nodes],
        "tile": [tile_a, tile_d],
        "sector_masks": [list(mask) for mask in masks],
        "degree_bounds": {
            _mask_text(mask): list(DEGREE_BOUNDS[mask]) for mask in masks
        },
        "point_count": len(rows),
        "direct_determinant_count": len(rows) * len(signs),
        "rows_sha256": _digest(rows),
        "rows": rows,
        "passed": len(rows) == 625,
    }


def _write_gzip_json(path: Path, value: object) -> None:
    with gzip.open(path, "wt", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, sort_keys=True, separators=(",", ":"))
        handle.write("\n")


def _read_gzip_json(path: Path) -> dict[str, object]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def verify_tile_report(report: dict[str, object]) -> bool:
    """Replay tile integrity and exact coverage without trusting ``passed``."""

    if report.get("node_set") not in NODE_SETS:
        return False
    tile = report.get("tile")
    if (
        not isinstance(tile, list)
        or len(tile) != 2
        or any(int(value) not in range(5) for value in tile)
    ):
        return False
    masks, _signs, _inverse, _complements = _shared_setup()
    expected_masks = [list(mask) for mask in masks]
    expected_bounds = {_mask_text(mask): list(DEGREE_BOUNDS[mask]) for mask in masks}
    nodes = NODE_SETS[report["node_set"]]
    if report.get("nodes") != [str(value) for value in nodes]:
        return False
    if report.get("squared_nodes") != [
        str(rational_circle(value)[0] ** 2) for value in nodes
    ]:
        return False
    rows = report.get("rows")
    if not isinstance(rows, list) or report.get("rows_sha256") != _digest(rows):
        return False
    expected_indices = {
        (int(tile[0]), int(tile[1]), *tail)
        for tail in itertools.product(range(5), repeat=4)
    }
    try:
        observed_indices = {
            tuple(int(value) for value in row["multi_index"]) for row in rows
        }
        residuals_are_exact = all(
            len(row["sector_residuals"]) == 8
            and all(sp.Rational(value).is_Rational for value in row["sector_residuals"])
            for row in rows
        )
    except (KeyError, TypeError, ValueError):
        return False
    return bool(
        len(rows) == len(observed_indices) == len(expected_indices) == 625
        and observed_indices == expected_indices
        and residuals_are_exact
        and report.get("sector_masks") == expected_masks
        and report.get("degree_bounds") == expected_bounds
        and report.get("point_count") == 625
        and report.get("direct_determinant_count") == 5000
        and report.get("passed") is True
    )


def reconstruct(tiles: list[Path]) -> dict[str, object]:
    if len(tiles) != 25:
        raise ValueError("exactly 25 tile files are required")
    reports = [_read_gzip_json(path) for path in tiles]
    node_set = reports[0]["node_set"]
    if any(report["node_set"] != node_set for report in reports):
        raise ValueError("tiles use different node sets")
    if {tuple(report["tile"]) for report in reports} != set(
        itertools.product(range(5), repeat=2)
    ):
        raise ValueError("tiles do not cover the 5 x 5 leading-axis grid")
    if not all(verify_tile_report(report) for report in reports):
        raise ValueError("tile failed replay verification")

    masks = tuple(tuple(mask) for mask in reports[0]["sector_masks"])
    tensors = {mask: np.empty((5,) * 6, dtype=object) for mask in masks}
    for report in reports:
        for row in report["rows"]:
            index = tuple(row["multi_index"])
            for mask, value in zip(masks, row["sector_residuals"], strict=True):
                tensors[mask][index] = sp.Rational(value)

    squared_nodes = tuple(sp.Rational(value) for value in reports[0]["squared_nodes"])
    vandermonde = sp.Matrix(
        [[node**power for power in range(5)] for node in squared_nodes]
    )
    inverse = vandermonde.inv()
    sector_rows = []
    for mask in masks:
        coefficients = tensors[mask]
        for axis in range(6):
            moved = np.moveaxis(coefficients, axis, 0)
            flat = moved.reshape(5, -1)
            transformed = np.empty_like(flat)
            for column in range(flat.shape[1]):
                transformed[:, column] = list(
                    inverse * sp.Matrix(list(flat[:, column]))
                )
            coefficients = np.moveaxis(transformed.reshape(moved.shape), 0, axis)

        coefficient_rows = []
        out_of_bound_rows = []
        bound = DEGREE_BOUNDS[mask]
        for powers in itertools.product(range(5), repeat=6):
            value = sp.factor(coefficients[powers])
            if value == 0:
                continue
            row = {"powers": list(powers), "coefficient": str(value)}
            coefficient_rows.append(row)
            if any(
                power > ceiling for power, ceiling in zip(powers, bound, strict=True)
            ):
                out_of_bound_rows.append(row)
        observed_degree = [
            max(row["powers"][axis] for row in coefficient_rows) for axis in range(6)
        ]
        sector_rows.append(
            {
                "mask": list(mask),
                "degree_bound": list(bound),
                "observed_multidegree": observed_degree,
                "nonzero_coefficient_count": len(coefficient_rows),
                "out_of_bound_nonzero_count": len(out_of_bound_rows),
                "coefficient_rows_sha256": _digest(coefficient_rows),
                "coefficient_rows": coefficient_rows,
            }
        )
    all_bounds_pass = all(row["out_of_bound_nonzero_count"] == 0 for row in sector_rows)
    return {
        "experiment": "two-edge all-sector exact shared-grid reconstruction",
        "node_set": node_set,
        "variable_order": list(VARIABLE_ORDER),
        "point_count": 5**6,
        "direct_determinant_count": 8 * 5**6,
        "sector_count": len(sector_rows),
        "all_individual_degree_bounds_pass": all_bounds_pass,
        "sector_rows_sha256": _digest(sector_rows),
        "sector_rows": sector_rows,
        "source_tile_hashes": [report["rows_sha256"] for report in reports],
        "passed": bool(len(sector_rows) == 8 and all_bounds_pass),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="stage", required=True)
    tile_parser = subparsers.add_parser("evaluate-tile")
    tile_parser.add_argument("--node-set", choices=tuple(NODE_SETS), required=True)
    tile_parser.add_argument("--tile-a", type=int, required=True)
    tile_parser.add_argument("--tile-d", type=int, required=True)
    tile_parser.add_argument("--workers", type=int, default=1)
    tile_parser.add_argument("--output", type=Path, required=True)
    reconstruct_parser = subparsers.add_parser("reconstruct")
    reconstruct_parser.add_argument("--tiles", nargs=25, type=Path, required=True)
    reconstruct_parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    if arguments.stage == "evaluate-tile":
        report = evaluate_tile(
            node_set=arguments.node_set,
            tile_a=arguments.tile_a,
            tile_d=arguments.tile_d,
            workers=arguments.workers,
        )
        _write_gzip_json(arguments.output, report)
    else:
        report = reconstruct(arguments.tiles)
        arguments.output.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    print(
        json.dumps(
            {
                key: value
                for key, value in report.items()
                if key not in {"rows", "sector_rows", "source_tile_hashes"}
            },
            indent=2,
        )
    )
    if not report["passed"]:
        raise SystemExit("shared-grid reconstruction stage failed")


if __name__ == "__main__":
    main()
