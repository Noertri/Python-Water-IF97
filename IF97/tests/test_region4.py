import unittest
from IF97 import PRESSC, TEMPC, PRESST, TEMPT
from IF97.cores.basic import Region4


class TestRegion4(unittest.TestCase):

    def test_satur_press(self):
        psat1_des = 0.353658941e-2
        psat2_des = 0.263889776e1
        psat3_des = 0.123443146e2

        self.assertAlmostEqual(Region4.getSaturPress(tsat=300)*1e-3, psat1_des, delta=1e-10)
        self.assertAlmostEqual(Region4.getSaturPress(tsat=500)*1e-3, psat2_des, delta=1e-5)
        self.assertAlmostEqual(Region4.getSaturPress(tsat=600)*1e-3, psat3_des, delta=1e-5)

    def test_satur_temp(self):
        tsat1_des = 0.372755919e3
        tsat2_des = 0.453035632e3
        tsat3_des = 0.584149488e3

        self.assertAlmostEqual(Region4.getSaturTemp(psat=100), tsat1_des, delta=1e-6)
        self.assertAlmostEqual(Region4.getSaturTemp(psat=1e3), tsat2_des, delta=1e-6)
        self.assertAlmostEqual(Region4.getSaturTemp(psat=1e4), tsat3_des, delta=1e-6)

    def test_triple_point(self):

        self.assertAlmostEqual(Region4.getSaturPress(tsat=TEMPT), PRESST, delta=1e-6)
        self.assertAlmostEqual(Region4.getSaturTemp(psat=PRESST), TEMPT, delta=1e-6)

    def test_critical_point(self):

        self.assertAlmostEqual(Region4.getSaturTemp(psat=PRESSC), TEMPC, delta=1e-8)
        self.assertAlmostEqual(Region4.getSaturPress(tsat=TEMPC), PRESSC, delta=1e-6)


if __name__ == "__main__":
    unittest.main()