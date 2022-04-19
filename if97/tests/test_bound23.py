import unittest
from IF97.cores.boundary import Boundary23


class TestBoundary23(unittest.TestCase):

    def test_press(self):
        p_des = 0.165291643e2

        self.assertAlmostEqual(Boundary23.getPress(t=623.15)*1e-3, p_des, delta=1e-7)

    def test_temp(self):
        t_des = 623.15

        self.assertAlmostEqual(Boundary23.getTemp(p=0.165291643e5), t_des, delta=1e-3)


if __name__ == "__main__":
    unittest.main()