import unittest
from IF97.visc import visc


class TestVisc(unittest.TestCase):

    def test_visc(self):
        des1 = 889.735100

        self.assertAlmostEqual(visc(rho=998, t=298.15)*1e6, des1, delta=1e-6)


if __name__ == "__main__":
    unittest.main()