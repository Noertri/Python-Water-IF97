import unittest
from if97 import get_satur_press, get_satur_temp


class TestRegion4(unittest.TestCase):

    def test_satur_temp(self):
        psat1_des = 0.353658941e-2
        psat2_des = 0.263889776e1
        psat3_des = 0.123443146e2

        self.assertAlmostEqual(get_satur_press(tsat=300)*1e-3, psat1_des, delta=1e-10)
        self.assertAlmostEqual(get_satur_press(tsat=500)*1e-3, psat2_des, delta=1e-5)
        self.assertAlmostEqual(get_satur_press(tsat=600)*1e-3, psat3_des, delta=1e-5)


if __name__ == "__main__":
    unittest.main()