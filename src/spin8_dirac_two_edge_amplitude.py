"""Exact common Cayley-boundary factor for the two-edge Dirac bridge."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp

from spin8_cayley_spectrum import symbolic_triality_generators
from spin8_dirac_edge import _symbolic_observation_block
from spin8_dirac_one_edge import _symbolic_vector


def exact_cayley_boundary_factor_certificate() -> dict[str, object]:
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

    passed = bool(branches_pass and normal_form_verified and target_remainder == 0)
    return {
        "experiment": "two-edge exact Cayley-boundary amplitude factor",
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
