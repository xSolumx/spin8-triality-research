"""Contracts for the all-sector shared-grid reconstruction campaign."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import sympy as sp

from spin8_dirac_star import rational_circle
from spin8_dirac_two_edge_shared_reconstruct import (
    DEGREE_BOUNDS,
    NODE_SETS,
    _shared_point_worker,
    _shared_setup,
)


class Spin8DiracTwoEdgeSharedGridTests(unittest.TestCase):
    def test_shared_grid_is_disjoint_and_four_times_smaller(self) -> None:
        self.assertTrue(set(NODE_SETS["alpha"]).isdisjoint(NODE_SETS["beta"]))
        self.assertEqual(5**6, 15625)
        self.assertLess(5**6, 61321)
        self.assertEqual(len(DEGREE_BOUNDS), 8)

    def test_shared_point_recovers_published_110101_sector(self) -> None:
        root = Path(__file__).parents[1]
        coefficient_report = json.loads(
            (
                root
                / "artifacts/spin8_dirac_two_edge_sector_110101_coefficients_20260806.json"
            ).read_text(encoding="utf-8")
        )
        parameters = tuple(sp.Rational(2 + axis, 37 + 2 * axis) for axis in range(6))
        masks, signs, inverse, complements = _shared_setup()
        _, residuals = _shared_point_worker(
            ((0,) * 6, parameters, masks, signs, inverse, complements)
        )
        mask = (1, 1, 0, 1, 0, 1)
        observed = sp.Rational(residuals[masks.index(mask)])
        squared = tuple(rational_circle(value)[0] ** 2 for value in parameters)
        predicted = sp.factor(
            sum(
                sp.Rational(row["coefficient"])
                * sp.prod(
                    squared[axis] ** int(row["powers"][axis]) for axis in range(6)
                )
                for row in coefficient_report["coefficient_rows"]
            )
        )
        self.assertEqual(observed, predicted)


if __name__ == "__main__":
    unittest.main()
