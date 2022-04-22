import unittest
from IF97.cores.basic import region5


class TestRegion5(unittest.TestCase):

    def test_properties1(self):
        v_des = 0.138455090e1
        h_des = 0.521976855e4
        u_des = 0.452749310e4
        s_des = 0.965408875e1
        cp_des = 0.261609445e1
        cv_des = 0.215337784e1

        self.assertAlmostEqual(region5(p=0.5e3, t=1500, desc="v"), v_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=0.5e3, t=1500, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(region5(p=0.5e3, t=1500, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(region5(p=0.5e3, t=1500, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=0.5e3, t=1500, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=0.5e3, t=1500, desc="cv"), cv_des, delta=1e-8)

    def test_properties2(self):
        v_des = 0.230761299e-1
        h_des = 0.516723514e4
        u_des = 0.447495124e4
        s_des = 0.772970133e1
        cp_des = 0.272724317e1
        cv_des = 0.219274829e1

        self.assertAlmostEqual(region5(p=30e3, t=1500, desc="v"), v_des, delta=1e-10)
        self.assertAlmostEqual(region5(p=30e3, t=1500, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(region5(p=30e3, t=1500, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(region5(p=30e3, t=1500, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=30e3, t=1500, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=30e3, t=1500, desc="cv"), cv_des, delta=1e-8)

    def test_properties3(self):
        v_des = 0.311385219e-1
        h_des = 0.657122604e4
        u_des = 0.563707038e4
        s_des = 0.853640523e1
        cp_des = 0.288569882e1
        cv_des = 0.239589436e1

        self.assertAlmostEqual(region5(p=30e3, t=2000, desc="v"), v_des, delta=1e-10)
        self.assertAlmostEqual(region5(p=30e3, t=2000, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(region5(p=30e3, t=2000, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(region5(p=30e3, t=2000, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=30e3, t=2000, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(region5(p=30e3, t=2000, desc="cv"), cv_des, delta=1e-8)


if __name__ == "__main__":
    unittest.main()