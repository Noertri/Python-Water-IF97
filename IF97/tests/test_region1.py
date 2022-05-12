import unittest
from IF97.cores.basic import Region1


class TestRegion1(unittest.TestCase):

    def test_properties1(self):
        v_des = 0.100215168e-2
        h_des = 0.115331273e3
        u_des = 0.112324818e3
        s_des = 0.392294792
        cp_des = 0.417301218e1
        cv_des = 0.412120160e1

        self.assertAlmostEqual(Region1.props(p=3e3, t=300, desc="v"), v_des, delta=1e-10)
        self.assertAlmostEqual(Region1.props(p=3e3, t=300, desc="h"), h_des, delta=1e-6)
        self.assertAlmostEqual(Region1.props(p=3e3, t=300, desc="u"), u_des, delta=1e-6)
        self.assertAlmostEqual(Region1.props(p=3e3, t=300, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(Region1.props(p=3e3, t=300, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(Region1.props(p=3e3, t=300, desc="cv"), cv_des, delta=1e-8)

    def test_properties2(self):
        v_des = 0.971180894e-3
        h_des = 0.184142828e3
        u_des = 0.106448356e3
        s_des = 0.368563852
        cp_des = 0.401008987e1
        cv_des = 0.391736606e1

        self.assertAlmostEqual(Region1.props(p=80e3, t=300, desc="v"), v_des, delta=1e-10)
        self.assertAlmostEqual(Region1.props(p=80e3, t=300, desc="h"), h_des, delta=1e-6)
        self.assertAlmostEqual(Region1.props(p=80e3, t=300, desc="u"), u_des, delta=1e-6)
        self.assertAlmostEqual(Region1.props(p=80e3, t=300, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(Region1.props(p=80e3, t=300, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(Region1.props(p=80e3, t=300, desc="cv"), cv_des, delta=1e-8)

    def test_properties3(self):
        v_des = 0.120241800e-2
        h_des = 0.975542239e3
        u_des = 0.971934985e3
        s_des = 0.258041912e1
        cp_des = 0.465580682e1
        cv_des = 0.322139223e1

        self.assertAlmostEqual(Region1.props(p=3e3, t=500, desc="v"), v_des, delta=1e-10)
        self.assertAlmostEqual(Region1.props(p=3e3, t=500, desc="h"), h_des, delta=1e-6)
        self.assertAlmostEqual(Region1.props(p=3e3, t=500, desc="u"), u_des, delta=1e-6)
        self.assertAlmostEqual(Region1.props(p=3e3, t=500, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(Region1.props(p=3e3, t=500, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(Region1.props(p=3e3, t=500, desc="cv"), cv_des, delta=1e-8)


if __name__ == "__main__":
    unittest.main()