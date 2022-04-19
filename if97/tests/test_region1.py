import unittest
from IF97.cores import region1


class TestRegion1(unittest.TestCase):

    def setUp(self):
        self.props1 = region1.Region1(p=3e3, t=300)
        self.props2 = region1.Region1(p=80e3, t=300)
        self.props3 = region1.Region1(p=3e3, t=500)

    def test_properties1(self):
        v_des = 0.100215168e-2
        h_des = 0.115331273e3
        u_des = 0.112324818e3
        s_des = 0.392294792
        cp_des = 0.417301218e1

        self.assertAlmostEqual(self.props1.get_properties("v"), v_des, delta=1e-10)
        self.assertAlmostEqual(self.props1.get_properties("h"), h_des, delta=1e-6)
        self.assertAlmostEqual(self.props1.get_properties("u"), u_des, delta=1e-6)
        self.assertAlmostEqual(self.props1.get_properties("s"), s_des, delta=1e-8)
        self.assertAlmostEqual(self.props1.get_properties("cp"), cp_des, delta=1e-8)

    def test_properties2(self):
        v_des = 0.971180894e-3
        h_des = 0.184142828e3
        u_des = 0.106448356e3
        s_des = 0.368563852
        cp_des = 0.401008987e1

        self.assertAlmostEqual(self.props2.get_properties("v"), v_des, delta=1e-10)
        self.assertAlmostEqual(self.props2.get_properties("h"), h_des, delta=1e-6)
        self.assertAlmostEqual(self.props2.get_properties("u"), u_des, delta=1e-6)
        self.assertAlmostEqual(self.props2.get_properties("s"), s_des, delta=1e-8)
        self.assertAlmostEqual(self.props2.get_properties("cp"), cp_des, delta=1e-8)

    def test_properties3(self):
        v_des = 0.120241800e-2
        h_des = 0.975542239e3
        u_des = 0.971934985e3
        s_des = 0.258041912e1
        cp_des = 0.465580682e1

        self.assertAlmostEqual(self.props3.get_properties("v"), v_des, delta=1e-10)
        self.assertAlmostEqual(self.props3.get_properties("h"), h_des, delta=1e-6)
        self.assertAlmostEqual(self.props3.get_properties("u"), u_des, delta=1e-6)
        self.assertAlmostEqual(self.props3.get_properties("s"), s_des, delta=1e-8)
        self.assertAlmostEqual(self.props3.get_properties("cp"), cp_des, delta=1e-8)


if __name__ == "__main__":
    unittest.main()