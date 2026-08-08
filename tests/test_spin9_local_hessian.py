from __future__ import annotations

import unittest

from spin9_local_hessian import diagnostics


class Spin9LocalHessianTests(unittest.TestCase):
    def test_exact_strict_local_maximum_certificate(self) -> None:
        report = diagnostics()
        self.assertTrue(report["passed"], report)
        self.assertTrue(report["orientation_identity"])
        self.assertTrue(report["frame_orthonormal"])
        self.assertTrue(report["information_block_diagonal"])
        self.assertTrue(report["supported_identity"])
        self.assertTrue(report["cross_squared_identity"])
        self.assertTrue(report["multiplicity_determinant_identity"])
        self.assertTrue(report["curve_stationary_identity"])
        self.assertTrue(report["curve_hessian_identity"])
        self.assertTrue(report["orientation_first_variation_zero"])
        self.assertTrue(report["supported_first_variations_zero"])
        self.assertTrue(report["supported_v5_hessian_isotropic"])
        self.assertTrue(report["local_hessian_negative_modulo_spin9"])
        self.assertTrue(report["orientation_curve_inner_zero"])
        self.assertTrue(report["orientation_spin9_orbit_normal"])
        self.assertTrue(report["curve_spin9_orbit_normal"])
        self.assertFalse(report["global_maximum_claimed"])


if __name__ == "__main__":
    unittest.main()
