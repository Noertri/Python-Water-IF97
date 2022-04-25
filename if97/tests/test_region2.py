import unittest
from IF97.cores.basic import region2, supp_region2


class TestRegion2(unittest.TestCase):

    def test_properties1(self):
        v_des = 0.394913866e2
        h_des = 0.254991145e4
        u_des = 0.241169160e4
        s_des = 0.852238967e1
        cp_des = 0.191300162e1
        cv_des = 0.144132662e1

        self.assertAlmostEqual(region2(p=3.5, t=300, desc="v"), v_des, delta=1e-7)
        self.assertAlmostEqual(region2(p=3.5, t=300, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(region2(p=3.5, t=300, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(region2(p=3.5, t=300, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(region2(p=3.5, t=300, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(region2(p=3.5, t=300, desc="cv"), cv_des, delta=1e-8)

    def test_properties2(self):
        v_des = 0.923015898e2
        h_des = 0.333568375e4
        u_des = 0.301262819e4
        s_des = 0.101749996e2
        cp_des = 0.208141274e1
        cv_des = 0.161978333e1

        self.assertAlmostEqual(region2(p=3.5, t=700, desc="v"), v_des, delta=1e-7)
        self.assertAlmostEqual(region2(p=3.5, t=700, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(region2(p=3.5, t=700, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(region2(p=3.5, t=700, desc="s"), s_des, delta=1e-7)
        self.assertAlmostEqual(region2(p=3.5, t=700, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(region2(p=3.5, t=700, desc="cv"), cv_des, delta=1e-8)

    def test_properties3(self):
        v_des = 0.542946619e-2
        h_des = 0.263149474e4
        u_des = 0.246861076e4
        s_des = 0.517540298e1
        cp_des = 0.103505092e2
        cv_des = 0.297553837e1

        self.assertAlmostEqual(region2(p=30e3, t=700, desc="v"), v_des, delta=1e-10)
        self.assertAlmostEqual(region2(p=30e3, t=700, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(region2(p=30e3, t=700, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(region2(p=30e3, t=700, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(region2(p=30e3, t=700, desc="cp"), cp_des, delta=1e-7)
        self.assertAlmostEqual(region2(p=30e3, t=700, desc="cv"), cv_des, delta=1e-7)

    def test_supp_properties1(self):
        v_des = 0.192516540
        h_des = 0.276881115e4
        u_des = 0.257629461e4
        s_des = 0.656660377e1
        cp_des = 0.276349265e1
        cv_des = 0.195830730e1

        self.assertAlmostEqual(supp_region2(p=1e3, t=450, desc="v"), v_des, delta=1e-9)
        self.assertAlmostEqual(supp_region2(p=1e3, t=450, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(supp_region2(p=1e3, t=450, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(supp_region2(p=1e3, t=450, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(supp_region2(p=1e3, t=450, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(supp_region2(p=1e3, t=450, desc="cv"), cv_des, delta=1e-8)

    def test_supp_properties2(self):
        v_des = 0.186212297
        h_des = 0.274015123e4
        u_des = 0.255393894e4
        s_des = 0.650218759e1
        cp_des = 0.298166443e1
        cv_des = 0.208622142e1

        self.assertAlmostEqual(supp_region2(p=1e3, t=440, desc="v"), v_des, delta=1e-9)
        self.assertAlmostEqual(supp_region2(p=1e3, t=440, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(supp_region2(p=1e3, t=440, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(supp_region2(p=1e3, t=440, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(supp_region2(p=1e3, t=440, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(supp_region2(p=1e3, t=440, desc="cv"), cv_des, delta=1e-8)

    def test_supp_properties3(self):
        v_des = 0.121685206
        h_des = 0.272134539e4
        u_des = 0.253881758e4
        s_des = 0.629170440e1
        cp_des = 0.362795578e1
        cv_des = 0.241213708e1

        self.assertAlmostEqual(supp_region2(p=1.5e3, t=450, desc="v"), v_des, delta=1e-9)
        self.assertAlmostEqual(supp_region2(p=1.5e3, t=450, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(supp_region2(p=1.5e3, t=450, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(supp_region2(p=1.5e3, t=450, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(supp_region2(p=1.5e3, t=450, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(supp_region2(p=1.5e3, t=450, desc="cv"), cv_des, delta=1e-8)


if __name__ == "__main__":
    unittest.main()