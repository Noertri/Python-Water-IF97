import unittest
from IF97 import PRESSC, TEMPC, PRESST, TEMPT
from IF97.cores.basic import region4_satpress, region4_sattemp


class TestRegion4(unittest.TestCase):

    def test_satur_press(self):
        psat1_des = 0.353658941e-2
        psat2_des = 0.263889776e1
        psat3_des = 0.123443146e2

        self.assertAlmostEqual(region4_satpress(tsat=300)*1e-3, psat1_des, delta=1e-10)
        self.assertAlmostEqual(region4_satpress(tsat=500)*1e-3, psat2_des, delta=1e-5)
        self.assertAlmostEqual(region4_satpress(tsat=600)*1e-3, psat3_des, delta=1e-5)

    def test_satur_temp(self):
        tsat1_des = 0.372755919e3
        tsat2_des = 0.453035632e3
        tsat3_des = 0.584149488e3

        self.assertAlmostEqual(region4_sattemp(psat=100), tsat1_des, delta=1e-6)
        self.assertAlmostEqual(region4_sattemp(psat=1e3), tsat2_des, delta=1e-6)
        self.assertAlmostEqual(region4_sattemp(psat=1e4), tsat3_des, delta=1e-6)

    def test_satpress_critical_and_triple_point(self):

        self.assertAlmostEqual(region4_satpress(tsat=273.16), PRESST, delta=1e-6)
        self.assertAlmostEqual(region4_satpress(tsat=647.096), PRESSC, delta=1e-6)

    def test_sattemp_critical_and_triple_point(self):

        self.assertAlmostEqual(region4_sattemp(psat=PRESST), TEMPT, delta=1e-8)
        self.assertAlmostEqual(region4_sattemp(psat=PRESSC), TEMPC, delta=1e-8)


if __name__ == "__main__":
    unittest.main()