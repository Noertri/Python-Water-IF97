import unittest
from IF97.visco import visc


class TestVisc(unittest.TestCase):

    def test_visc(self):
        des1 = 889.735100
        des2 = 1437.649467
        des3 = 307.883622
        des4 = 14.538324
        des5 = 217.685358
        des6 = 32.619287
        des7 = 35.802262
        des8 = 77.430195
        des9 = 44.217245
        des10 = 47.640433
        des11 = 64.154608

        self.assertAlmostEqual(visc(rho=998, t=298.15)*1e6, des1, delta=1e-6)
        self.assertAlmostEqual(visc(rho=1200, t=298.15)*1e6, des2, delta=1e-6)
        self.assertAlmostEqual(visc(rho=1000, t=373.15)*1e6, des3, delta=1e-6)
        self.assertAlmostEqual(visc(rho=1, t=433.15)*1e6, des4, delta=1e-6)
        self.assertAlmostEqual(visc(rho=1000, t=433.15)*1e6, des5, delta=1e-6)
        self.assertAlmostEqual(visc(rho=1, t=873.15)*1e6, des6, delta=1e-6)
        self.assertAlmostEqual(visc(rho=100, t=873.15)*1e6, des7, delta=1e-6)
        self.assertAlmostEqual(visc(rho=600, t=873.15)*1e6, des8, delta=1e-6)
        self.assertAlmostEqual(visc(rho=1, t=1173.15)*1e6, des9, delta=1e-6)
        self.assertAlmostEqual(visc(rho=100, t=1173.15)*1e6, des10, delta=1e-6)
        self.assertAlmostEqual(visc(rho=400, t=1173.15)*1e6, des11, delta=1e-6)


if __name__ == "__main__":
    unittest.main()