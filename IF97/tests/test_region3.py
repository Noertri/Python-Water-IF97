import unittest
from IF97.cores.basic import Region3


class TestRegion3(unittest.TestCase):

    def test_properties1(self):
        p_des = 0.255837018e2
        h_des = 0.186343019e4
        u_des = 0.181226279e4
        s_des = 0.405427273e1
        cp_des = 0.138935717e2
        cv_des = 0.319131787e1

        self.assertAlmostEqual(Region3.region3(rho=500, t=650, desc="p")*1e-3, p_des, delta=1e-7)
        self.assertAlmostEqual(Region3.region3(rho=500, t=650, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(Region3.region3(rho=500, t=650, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(Region3.region3(rho=500, t=650, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(Region3.region3(rho=500, t=650, desc="cp"), cp_des, delta=1e-7)
        self.assertAlmostEqual(Region3.region3(rho=500, t=650, desc="cv"), cv_des, delta=1e-8)

    def test_properties2(self):
        p_des = 0.222930643e2
        h_des = 0.237512401e4
        u_des = 0.226365868e4
        s_des = 0.485438792e1
        cp_des = 0.446579342e2
        cv_des = 0.404118076e1

        self.assertAlmostEqual(Region3.region3(rho=200, t=650, desc="p")*1e-3, p_des, delta=1e-7)
        self.assertAlmostEqual(Region3.region3(rho=200, t=650, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(Region3.region3(rho=200, t=650, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(Region3.region3(rho=200, t=650, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(Region3.region3(rho=200, t=650, desc="cp"), cp_des, delta=1e-7)
        self.assertAlmostEqual(Region3.region3(rho=200, t=650, desc="cv"), cv_des, delta=1e-8)

    def test_properties3(self):
        p_des = 0.783095639e2
        h_des = 0.225868845e4
        u_des = 0.210206932e4
        s_des = 0.446971906e1
        cp_des = 0.634165359e1
        cv_des = 0.271701677e1

        self.assertAlmostEqual(Region3.region3(rho=500, t=750, desc="p")*1e-3, p_des, delta=1e-7)
        self.assertAlmostEqual(Region3.region3(rho=500, t=750, desc="h"), h_des, delta=1e-5)
        self.assertAlmostEqual(Region3.region3(rho=500, t=750, desc="u"), u_des, delta=1e-5)
        self.assertAlmostEqual(Region3.region3(rho=500, t=750, desc="s"), s_des, delta=1e-8)
        self.assertAlmostEqual(Region3.region3(rho=500, t=750, desc="cp"), cp_des, delta=1e-8)
        self.assertAlmostEqual(Region3.region3(rho=500, t=750, desc="cv"), cv_des, delta=1e-8)


if __name__ == "__main__":
    unittest.main()