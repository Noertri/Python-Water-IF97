import unittest
from IF97.cores import region5


class TestRegion5(unittest.TestCase):

    def setUp(self):
        self.props1 = region5.Region5(p=0.5e3, t=1500)
        self.props2 = region5.Region5(p=30e3, t=1500)
        self.props3 = region5.Region5(p=30e3, t=2000)

    def test_properties1(self):
        v_des = 0.138455090e1
        h_des = 0.521976855e4
        u_des = 0.452749310e4
        s_des = 0.965408875e1
        cp_des = 0.261609445e1

        self.assertAlmostEqual(self.props1.get_properties("v"), v_des, delta=1e-8)
        self.assertAlmostEqual(self.props1.get_properties("h"), h_des, delta=1e-5)
        self.assertAlmostEqual(self.props1.get_properties("u"), u_des, delta=1e-5)
        self.assertAlmostEqual(self.props1.get_properties("s"), s_des, delta=1e-8)
        self.assertAlmostEqual(self.props1.get_properties("cp"), cp_des, delta=1e-8)

    def test_properties2(self):
        v_des = 0.230761299e-1
        h_des = 0.516723514e4
        u_des = 0.447495124e4
        s_des = 0.772970133e1
        cp_des = 0.272724317e1

        self.assertAlmostEqual(self.props2.get_properties("v"), v_des, delta=1e-10)
        self.assertAlmostEqual(self.props2.get_properties("h"), h_des, delta=1e-5)
        self.assertAlmostEqual(self.props2.get_properties("u"), u_des, delta=1e-5)
        self.assertAlmostEqual(self.props2.get_properties("s"), s_des, delta=1e-8)
        self.assertAlmostEqual(self.props2.get_properties("cp"), cp_des, delta=1e-8)

    def test_properties3(self):
        v_des = 0.311385219e-1
        h_des = 0.657122604e4
        u_des = 0.563707038e4
        s_des = 0.853640523e1
        cp_des = 0.288569882e1

        self.assertAlmostEqual(self.props3.get_properties("v"), v_des, delta=1e-10)
        self.assertAlmostEqual(self.props3.get_properties("h"), h_des, delta=1e-5)
        self.assertAlmostEqual(self.props3.get_properties("u"), u_des, delta=1e-5)
        self.assertAlmostEqual(self.props3.get_properties("s"), s_des, delta=1e-8)
        self.assertAlmostEqual(self.props3.get_properties("cp"), cp_des, delta=1e-8)


if __name__ == "__main__":
    unittest.main()