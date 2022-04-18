import unittest
from if97 import PRESSC, TEMPC, PRESST, TEMPT
from if97.cores.region4 import get_satur_press, get_satur_temp


class TestRegion4(unittest.TestCase):

    def test_satur_press(self):
        psat1_des = 0.353658941e-2
        psat2_des = 0.263889776e1
        psat3_des = 0.123443146e2

        self.assertAlmostEqual(get_satur_press(tsat=300)*1e-3, psat1_des, delta=1e-10)
        self.assertAlmostEqual(get_satur_press(tsat=500)*1e-3, psat2_des, delta=1e-5)
        self.assertAlmostEqual(get_satur_press(tsat=600)*1e-3, psat3_des, delta=1e-5)

    def test_satur_temp(self):
        tsat1_des = 0.372755919e3
        tsat2_des = 0.453035632e3
        tsat3_des = 0.584149488e3

        self.assertAlmostEqual(get_satur_temp(psat=100), tsat1_des, delta=1e-6)
        self.assertAlmostEqual(get_satur_temp(psat=1e3), tsat2_des, delta=1e-6)
        self.assertAlmostEqual(get_satur_temp(psat=1e4), tsat3_des, delta=1e-6)

    def test_satpress_critical_and_triple_point(self):

        self.assertAlmostEqual(get_satur_press(tsat=273.16), PRESST, delta=1e-6)
        self.assertAlmostEqual(get_satur_press(tsat=647.096), PRESSC, delta=1e-6)

    def test_sattemp_critical_and_triple_point(self):

        self.assertAlmostEqual(get_satur_temp(psat=PRESST), TEMPT, delta=1e-8)
        self.assertAlmostEqual(get_satur_temp(psat=PRESSC), TEMPC, delta=1e-8)


if __name__ == "__main__":
    unittest.main()