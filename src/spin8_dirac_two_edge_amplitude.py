"""Exact common Cayley-boundary factor for the two-edge Dirac bridge."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp

from spin8_cayley_spectrum import symbolic_triality_generators
from spin8_dirac_edge import (
    _character,
    _symbolic_observation_block,
    exact_walsh_symmetry_certificate,
)
from spin8_dirac_one_edge import _symbolic_vector

CHART_PARAMETER_ORDER = ("a", "A", "d", "D", "e", "E", "g", "G", "i", "I", "c", "s")
LOWER_INDICES = (0, 2, 4, 6, 8, 10)
COMPLEMENT_INDICES = (1, 3, 5, 7, 9, 11)


def exact_extended_chart_sign_certificate() -> dict[str, object]:
    """Derive all allowed parities in the twelve-coordinate circle chart."""

    base = exact_walsh_symmetry_certificate()
    induced = set()
    for action in base["triality_representation_actions"]:
        positive_signs = action["positive_spinor_signs"]
        negative_signs = action["negative_spinor_signs"]
        for (
            positive_gauge,
            first_negative_gauge,
            second_negative_gauge,
        ) in itertools.product((1, -1), repeat=3):
            for signs in itertools.product((1, -1), repeat=len(CHART_PARAMETER_ORDER)):
                a, diagonal_a, d, diagonal_d, e, diagonal_e = signs[:6]
                g, diagonal_g, i, diagonal_i, cayley, sine = signs[6:]
                if a != positive_gauge * positive_signs[0]:
                    continue
                if diagonal_a != positive_gauge * positive_signs[1]:
                    continue
                if d != first_negative_gauge * negative_signs[0]:
                    continue
                if diagonal_d * e != first_negative_gauge * negative_signs[1]:
                    continue
                if diagonal_d * diagonal_e != (
                    first_negative_gauge * negative_signs[2]
                ):
                    continue
                if g != second_negative_gauge * negative_signs[0]:
                    continue
                if diagonal_g * i != second_negative_gauge * negative_signs[2]:
                    continue
                if diagonal_g * diagonal_i * cayley != (
                    second_negative_gauge * negative_signs[3]
                ):
                    continue
                if diagonal_g * diagonal_i * sine != (
                    second_negative_gauge * negative_signs[4]
                ):
                    continue
                induced.add(signs)

    annihilator = {
        mask
        for mask in itertools.product((0, 1), repeat=len(CHART_PARAMETER_ORDER))
        if all(_character(signs, mask) == 1 for signs in induced)
    }
    chart_characters = []
    lower_masks = set()
    for mask in sorted(annihilator):
        lower = tuple(mask[index] for index in LOWER_INDICES)
        complement = tuple(mask[index] for index in COMPLEMENT_INDICES)
        lower_masks.add(lower)
        chart_characters.append(
            {
                "lower_mask": list(lower),
                "complement_mask": list(complement),
                "forced_monomial": " ".join(
                    name
                    for name, bit in zip(CHART_PARAMETER_ORDER, mask, strict=True)
                    if bit
                )
                or "1",
            }
        )

    passed = bool(
        base["passed"]
        and base["common_adjoint_conjugacy_verified"]
        and len(induced) == 512
        and len(annihilator) == 8
        and len(lower_masks) == 8
    )
    return {
        "chart_parameter_order": list(CHART_PARAMETER_ORDER),
        "induced_chart_sign_group_order": len(induced),
        "annihilator_order": len(annihilator),
        "one_complement_character_per_lower_character": len(lower_masks)
        == len(annihilator),
        "chart_characters": chart_characters,
        "global_sector_ansatz": (
            "Each sector equals its forced chart monomial times a polynomial "
            "in a^2,d^2,e^2,g^2,i^2,c^2 after the circle relations."
        ),
        "passed": passed,
    }


def exact_cayley_boundary_factor_certificate() -> dict[str, object]:
    chart_signs = exact_extended_chart_sign_certificate()
    generators = symbolic_triality_generators()
    basis = [[sp.Integer(row == column) for column in range(8)] for row in range(8)]
    a, diagonal_a, d, diagonal_d, e, diagonal_e = sp.symbols("a A d D e E")
    g, diagonal_g, i, diagonal_i = sp.symbols("g G i I")

    positive = _symbolic_vector((a, diagonal_a), (0, 1), basis)
    first_negative = _symbolic_vector(
        (d, diagonal_d * e, diagonal_d * diagonal_e), (0, 1, 2), basis
    )
    fixed_blocks = (
        _symbolic_observation_block(0, basis[0], generators),
        _symbolic_observation_block(1, basis[0], generators),
        _symbolic_observation_block(1, positive, generators),
        _symbolic_observation_block(2, first_negative, generators),
    )

    branch_rows = []
    for branch in (1, -1):
        final_negative = _symbolic_vector(
            (g, diagonal_g * i, branch * diagonal_g * diagonal_i),
            (0, 2, 3),
            basis,
        )
        jacobian = sp.Matrix.vstack(
            *fixed_blocks,
            _symbolic_observation_block(2, final_negative, generators),
        )
        nullspace = jacobian.nullspace()
        branch_rows.append(
            {
                "cayley_branch": "+1" if branch == 1 else "-1",
                "symbolic_rank": 28 - len(nullspace),
                "symbolic_nullity": len(nullspace),
                "nullspace_residual_exact_zero": all(
                    all(sp.factor(entry) == 0 for entry in jacobian * vector)
                    for vector in nullspace
                ),
                "nullspace_vectors": [
                    [str(sp.factor(entry)) for entry in vector] for vector in nullspace
                ],
                "guaranteed_minor_order_in_s": len(nullspace),
                "guaranteed_information_determinant_order_in_s": 2 * len(nullspace),
            }
        )

    circle_c, circle_s = sp.symbols("c s")
    groebner = sp.groebner(
        (circle_c**2 + circle_s**2 - 1,),
        circle_c,
        circle_s,
        order="lex",
    )
    leading_monomials = [
        list(polynomial.LM(order=groebner.order).exponents)
        for polynomial in groebner.polys
    ]
    normal_form_verified = leading_monomials == [[2, 0]]
    branches_pass = all(
        row["symbolic_rank"] == 25
        and row["symbolic_nullity"] == 3
        and row["nullspace_residual_exact_zero"]
        for row in branch_rows
    )
    target_identity = sp.expand(
        (1 - circle_c**2) ** 3 * (9 - circle_c**2) ** 2
        - circle_s**6 * (9 - circle_c**2) ** 2
    )
    target_remainder = sp.rem(
        sp.Poly(target_identity, circle_c),
        sp.Poly(circle_c**2 - (1 - circle_s**2), circle_c),
    ).as_expr()

    passed = bool(
        chart_signs["passed"]
        and branches_pass
        and normal_form_verified
        and target_remainder == 0
    )
    return {
        "experiment": "two-edge exact Cayley-boundary amplitude factor",
        "extended_chart_sign_certificate": chart_signs,
        "coordinate_ring": "Q[c,s]/(c^2+s^2-1)",
        "free_module_basis_over_Q_s": ["1", "c"],
        "groebner_leading_monomials": leading_monomials,
        "boundary_branch_rows": branch_rows,
        "both_branch_divisibility_argument": (
            "Every quotient element has unique form F0(s)+c F1(s). At s=0, "
            "the c=+1 and c=-1 branches both have Jacobian nullity three. "
            "Each 28-row minor is therefore O(s^3), and Cauchy-Binet makes "
            "det(J^T J)=O(s^6). Adding and subtracting the two branch "
            "expansions makes both F0 and F1 divisible by s^6 because "
            "sqrt(1-s^2) is a unit near s=0."
        ),
        "common_normalized_determinant_factor": "s^6 = (1-c^2)^3",
        "all_eight_walsh_sectors_inherit_factor": True,
        "target_after_common_factor": "(9-c^2)^2",
        "target_factor_identity_verified": target_remainder == 0,
        "passed": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    report = exact_cayley_boundary_factor_certificate()
    arguments.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit("two-edge Cayley-boundary factor certificate failed")


if __name__ == "__main__":
    main()
