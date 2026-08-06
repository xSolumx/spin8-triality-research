"""Contracts for the preregistered second-residual Dirac bridge."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from spin8_dirac_two_edge import (
    ANCHORS,
    exact_normalized_determinant,
    exact_sign_symmetry_certificate,
    verify_anchor_report,
)


class Spin8DiracTwoEdgeTests(unittest.TestCase):
    def test_common_triality_symmetry_allows_exactly_eight_sectors(self) -> None:
        report = exact_sign_symmetry_certificate()
        self.assertTrue(report["passed"])
        self.assertEqual(len(report["induced_sign_group"]), 8)
        self.assertEqual(len(report["walsh_annihilator"]), 8)

    def test_two_exact_anchors_activate_the_complete_allowed_support(self) -> None:
        artifact = (
            Path(__file__).parents[1]
            / "artifacts"
            / "spin8_dirac_two_edge_anchor_20260806.json"
        )
        report = json.loads(artifact.read_text(encoding="utf-8"))
        self.assertTrue(verify_anchor_report(report))
        self.assertEqual(report["exact_determinant_count"], 128)
        self.assertTrue(report["supports_match_between_anchors"])
        self.assertTrue(
            all(row["support_equals_symmetry_annihilator"] for row in report["anchors"])
        )

        first = report["determinant_rows"][0]
        direct = exact_normalized_determinant(
            ANCHORS[first["anchor_index"]], tuple(first["signs"])
        )
        self.assertEqual(str(direct), first["normalized_determinant"])


if __name__ == "__main__":
    unittest.main()
