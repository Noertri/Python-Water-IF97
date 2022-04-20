import unittest
from IF97.cores.boundary import bound_subreg3


class TestBoundSubReg3(unittest.TestCase):

    def test_bound_subreg3(self):
        t3ab = 6.930341408e2
        t3cd = 6.493659208e2
        t3ef = 7.139593992e2
        t3gh = 6.498873759e2
        t3ij = 6.515778091e2
        t3jk = 6.558338344e2
        t3mn = 6.496054133e2
        t3op = 6.500106943e2
        t3qu = 6.456355027e2
        t3rx = 6.482622754e2
        t3uv = 6.477996121e2
        t3wx = 6.482049480e2

        self.assertAlmostEqual(bound_subreg3(p=40e3, desc="3ab"), t3ab, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=25e3, desc="3cd"), t3cd, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=40e3, desc="3ef"), t3ef, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=23e3, desc="3gh"), t3gh, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=23e3, desc="3ij"), t3ij, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=23e3, desc="3jk"), t3jk, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=22.8e3, desc="3mn"), t3mn, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=22.8e3, desc="3op"), t3op, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=22e3, desc="3qu"), t3qu, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=22e3, desc="3rx"), t3rx, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=22.3e3, desc="3uv"), t3uv, delta=1e-7)
        self.assertAlmostEqual(bound_subreg3(p=22.3e3, desc="3wx"), t3wx, delta=1e-7)

    def test_result_none(self):
        self.assertIsNone(bound_subreg3(p=22.3e3, desc="3yz"))


if __name__ == "__main__":
    unittest.main()