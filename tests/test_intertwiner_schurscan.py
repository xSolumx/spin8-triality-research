from __future__ import annotations

import unittest

import torch

from intertwiner_schurscan import (
    bilinear_contract,
    diagnostics,
    feedback_degree_growth,
    so3_cross_product_tensor,
)


class IntertwinerSchurScanTests(unittest.TestCase):
    def test_generic_triangular_scan_and_lift(self) -> None:
        report = diagnostics()
        self.assertTrue(report["passed"], report)
        self.assertEqual(report["parallel_scan_stages"], 2)
        self.assertEqual(report["streaming_cache_scalars"], 9)
        self.assertEqual(report["homogeneous_proof_lift_scalars"], 19)
        self.assertLessEqual(report["staged_recurrent_max_abs_error"], 1e-11)
        self.assertLessEqual(report["lifted_recurrent_max_abs_error"], 1e-11)
        self.assertLessEqual(report["equivariance_max_abs_error"], 1e-11)

    def test_so3_control_is_actual_cross_product(self) -> None:
        dtype = torch.float64
        beta = so3_cross_product_tensor(dtype=dtype)
        u = torch.tensor([[1.0, 2.0, -1.0]], dtype=dtype)
        v = torch.tensor([[0.5, -2.0, 3.0]], dtype=dtype)
        self.assertTrue(
            torch.equal(bilinear_contract(u, v, beta), torch.linalg.cross(u, v))
        )

    def test_feedback_degree_obstruction(self) -> None:
        growth = feedback_degree_growth(8)
        self.assertEqual(growth["triangular"], [2] * 8)
        self.assertEqual(growth["feedback_into_one_source"], list(range(2, 10)))
        self.assertEqual(
            growth["feedback_into_both_sources"],
            [2, 4, 8, 16, 32, 64, 128, 256],
        )


if __name__ == "__main__":
    unittest.main()
