"""Contracts for the two-edge common Cayley-boundary factor."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from spin8_dirac_two_edge_amplitude import (
    exact_cayley_boundary_factor_certificate,
    exact_extended_chart_sign_certificate,
)


class Spin8DiracTwoEdgeAmplitudeTests(unittest.TestCase):
    def test_extended_chart_has_one_complement_parity_per_sector(self) -> None:
        report = exact_extended_chart_sign_certificate()
        self.assertTrue(report["passed"])
        self.assertEqual(report["induced_chart_sign_group_order"], 512)
        self.assertEqual(report["annihilator_order"], 8)
        mapping = {
            "".join(map(str, row["lower_mask"])): "".join(
                map(str, row["complement_mask"])
            )
            for row in report["chart_characters"]
        }
        self.assertEqual(mapping["001101"], "001110")
        self.assertEqual(mapping["111000"], "110000")

    def test_both_cayley_boundary_branches_have_exact_nullity_three(self) -> None:
        report = exact_cayley_boundary_factor_certificate()
        self.assertTrue(report["passed"])
        self.assertEqual(
            [row["symbolic_rank"] for row in report["boundary_branch_rows"]],
            [25, 25],
        )
        self.assertEqual(
            [row["symbolic_nullity"] for row in report["boundary_branch_rows"]],
            [3, 3],
        )
        self.assertEqual(
            report["common_normalized_determinant_factor"],
            "s^6 = (1-c^2)^3",
        )

    def test_published_artifact_matches_fresh_certificate(self) -> None:
        artifact = (
            Path(__file__).parents[1]
            / "artifacts"
            / "spin8_dirac_two_edge_amplitude_20260806.json"
        )
        stored = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertEqual(stored, exact_cayley_boundary_factor_certificate())


if __name__ == "__main__":
    unittest.main()
