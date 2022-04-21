import unittest
from IF97.cores.backwardPT import region3


class TestBackwardPT(unittest.TestCase):

    def test_subreg3a(self):
        v1 = 1.470853100e-3
        v2 = 1.503831359e-3

        self.assertAlmostEqual(region3(p=50e3, t=630, desc="3a"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=80e3, t=670, desc="3a"), v2, delta=1e-12)

    def test_subreg3b(self):
        v1 = 2.204728587e-3
        v2 = 1.973692940e-3

        self.assertAlmostEqual(region3(p=50e3, t=710, desc="3b"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=80e3, t=750, desc="3b"), v2, delta=1e-12)

    def test_subreg3c(self):
        v1 = 1.761696406e-3
        v2 = 1.819560617e-3

        self.assertAlmostEqual(region3(p=20e3, t=630, desc="3c"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=30e3, t=650, desc="3c"), v2, delta=1e-12)

    def test_subreg3d(self):
        v1 = 2.245587720e-3
        v2 = 2.506897702e-3

        self.assertAlmostEqual(region3(p=26e3, t=656, desc="3d"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=30e3, t=670, desc="3d"), v2, delta=1e-12)

    def test_subreg3e(self):
        v1 = 2.970225962e-3
        v2 = 3.004627086e-3

        self.assertAlmostEqual(region3(p=26e3, t=661, desc="3e"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=30e3, t=675, desc="3e"), v2, delta=1e-12)

    def test_subreg3f(self):
        v1 = 5.019029401e-3
        v2 = 4.656470142e-3

        self.assertAlmostEqual(region3(p=26e3, t=671, desc="3f"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=30e3, t=690, desc="3f"), v2, delta=1e-12)

    def test_subreg3g(self):
        v1 = 2.163198378e-3
        v2 = 2.166044161e-3

        self.assertAlmostEqual(region3(p=23.6e3, t=649, desc="3g"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=24e3, t=650, desc="3g"), v2, delta=1e-12)

    def test_subreg3h(self):
        v1 = 2.651081407e-3
        v2 = 2.967802335e-3

        self.assertAlmostEqual(region3(p=23.6e3, t=652, desc="3h"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=24e3, t=654, desc="3h"), v2, delta=1e-12)

    def test_subreg3i(self):
        v1 = 3.273916816e-3
        v2 = 3.550329864e-3

        self.assertAlmostEqual(region3(p=23.6e3, t=653, desc="3i"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=24e3, t=655, desc="3i"), v2, delta=1e-12)

    def test_subreg3j(self):
        v1 = 4.545001142e-3
        v2 = 5.100267704e-3

        self.assertAlmostEqual(region3(p=23.5e3, t=655, desc="3j"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=24e3, t=660, desc="3j"), v2, delta=1e-12)

    def test_subreg3k(self):
        v1 = 6.109525997e-3
        v2 = 6.427325645e-3

        self.assertAlmostEqual(region3(p=23e3, t=660, desc="3k"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=24e3, t=670, desc="3k"), v2, delta=1e-12)

    def test_subreg3l(self):
        v1 = 2.117860851e-3
        v2 = 2.062374674e-3

        self.assertAlmostEqual(region3(p=22.6e3, t=646, desc="3l"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=23e3, t=646, desc="3l"), v2, delta=1e-12)

    def test_subreg3m(self):
        v1 = 2.533063780e-3
        v2 = 2.572971781e-3

        self.assertAlmostEqual(region3(p=22.6e3, t=648.6, desc="3m"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.8e3, t=649.3, desc="3m"), v2, delta=1e-12)

    def test_subreg3n(self):
        v1 = 2.923432711e-3
        v2 = 2.913311494e-3

        self.assertAlmostEqual(region3(p=22.6e3, t=649, desc="3n"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.8e3, t=649.7, desc="3n"), v2, delta=1e-12)

    def test_subreg3o(self):
        v1 = 3.131208996e-3
        v2 = 3.221160278e-3

        self.assertAlmostEqual(region3(p=22.6e3, t=649.1, desc="3o"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.8e3, t=649.9, desc="3o"), v2, delta=1e-12)

    def test_subreg3p(self):
        v1 = 3.715596186e-3
        v2 = 3.664754790e-3

        self.assertAlmostEqual(region3(p=22.6e3, t=649.4, desc="3p"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.8e3, t=650.2, desc="3p"), v2, delta=1e-12)

    def test_subreg3q(self):
        v1 = 1.970999272e-3
        v2 = 2.043919161e-3

        self.assertAlmostEqual(region3(p=21.1e3, t=640, desc="3q"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=21.8e3, t=643, desc="3q"), v2, delta=1e-12)

    def test_subreg3r(self):
        v1 = 5.251009921e-3
        v2 = 5.256844741e-3

        self.assertAlmostEqual(region3(p=21.1e3, t=644, desc="3r"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=21.8e3, t=648, desc="3r"), v2, delta=1e-12)

    def test_subreg3s(self):
        v1 = 1.932829079e-3
        v2 = 1.985387227e-3

        self.assertAlmostEqual(region3(p=19.1e3, t=635, desc="3s"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=20e3, t=638, desc="3s"), v2, delta=1e-12)

    def test_subreg3t(self):
        v1 = 8.483262001e-3
        v2 = 6.227528101e-3

        self.assertAlmostEqual(region3(p=17e3, t=626, desc="3t"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=20e3, t=640, desc="3t"), v2, delta=1e-12)

    def test_subreg3u(self):
        v1 = 2.268366647e-3
        v2 = 2.296350553e-3

        self.assertAlmostEqual(region3(p=21.5e3, t=644.6, desc="3u"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22e3, t=646.1, desc="3u"), v2, delta=1e-12)

    def test_subreg3v(self):
        v1 = 2.832373260e-3
        v2 = 2.811424405e-3

        self.assertAlmostEqual(region3(p=22.5e3, t=648.6, desc="3v"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.3e3, t=647.9, desc="3v"), v2, delta=1e-12)

    def test_subreg3w(self):
        v1 = 3.694032281e-3
        v2 = 3.622226305e-3

        self.assertAlmostEqual(region3(p=22.15e3, t=647.5, desc="3w"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.3e3, t=648.1, desc="3w"), v2, delta=1e-12)

    def test_subreg3x(self):
        v1 = 4.528072649e-3
        v2 = 4.556905799e-3

        self.assertAlmostEqual(region3(p=22.11e3, t=648, desc="3x"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.3e3, t=649, desc="3x"), v2, delta=1e-12)

    def test_subreg3y(self):
        v1 = 2.698354719e-3
        v2 = 2.717655648e-3

        self.assertAlmostEqual(region3(p=22e3, t=646.84, desc="3y"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.064e3, t=647.05, desc="3y"), v2, delta=1e-12)

    def test_subreg3z(self):
        v1 = 3.798732962e-3
        v2 = 3.701940010e-3

        self.assertAlmostEqual(region3(p=22e3, t=646.89, desc="3z"), v1, delta=1e-12)
        self.assertAlmostEqual(region3(p=22.064e3, t=647.15, desc="3z"), v2, delta=1e-12)


if __name__ == "__main__":
    unittest.main()