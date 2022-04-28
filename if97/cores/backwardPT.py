from numpy import exp
from ..koefisien import IJnSubReg3
from .boundary import Boundary23, temp3
from .basic import region4


def region3PT(p, t, desc=None):
    """Persamaan balik untuk region 3"""

    if desc and desc.lower() != "3n":
        a = IJnSubReg3[desc.lower()]["a"]
        b = IJnSubReg3[desc.lower()]["b"]
        c = IJnSubReg3[desc.lower()]["c"]
        d = IJnSubReg3[desc.lower()]["d"]
        e = IJnSubReg3[desc.lower()]["e"]
        I = IJnSubReg3[desc.lower()]["I"]
        J = IJnSubReg3[desc.lower()]["J"]
        n = IJnSubReg3[desc.lower()]["n"]
        v0 = IJnSubReg3[desc.lower()]["vol0"]
        p0 = IJnSubReg3[desc.lower()]["press0"]
        t0 = IJnSubReg3[desc.lower()]["temp0"]

        pi = p/p0
        theta = t/t0

        omega = 0.
        for Ii, Ji, ni, in zip(I, J, n):
            omega += ni*(((pi-a)**c)**Ii)*(((theta-b)**d)**Ji)

        return v0*(omega**e)
    elif desc and desc.lower() == "3n":
        a = IJnSubReg3["3n"]["a"]
        b = IJnSubReg3["3n"]["b"]
        I = IJnSubReg3["3n"]["I"]
        J = IJnSubReg3["3n"]["J"]
        n = IJnSubReg3["3n"]["n"]
        v0 = IJnSubReg3["3n"]["vol0"]
        p0 = IJnSubReg3["3n"]["press0"]
        t0 = IJnSubReg3["3n"]["temp0"]

        pi = p/p0
        theta = t/t0

        omega = 0.
        for Ii, Ji, ni, in zip(I, J, n):
            omega += ni*((pi-a)**Ii)*((theta-b)**Ji)

        return v0*exp(omega)
    else:
        return None


class Reg3RhoPT:
    """Implementasi persamaan balik region 3 v(P, T)"""

    @classmethod
    def singleRho(cls, p, t):
        """Implementasi persamaan subregion 3a sampai 3t"""

        vol = 0.
        p23 = Boundary23.getPress(t)
        p643 = region4(tsat=643.15)
        p3cd = 19.00881189173929e3
        pmin = region4(tsat=623.15)

        if 623.15 < t <= 863.15 and p23 < p <= 1e5:
            if 4e4 < p <= 1e5:
                if t <= temp3(p, "3ab"):
                    vol = region3PT(p, t, "3a")
                elif t > temp3(p, "3ab"):
                    vol = region3PT(p, t, "3b")
            elif 25e3 < p <= 4e4:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= temp3(p, "3ab"):
                    vol = region3PT(p, t, "3d")
                elif temp3(p, "3ab") < t <= temp3(p, "3ef"):
                    vol = region3PT(p, t, "3e")
                elif t > temp3(p, "3ef"):
                    vol = region3PT(p, t, "3f")
            elif 23.5e3 < p <= 25e3:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= temp3(p, "3gh"):
                    vol = region3PT(p, t, "3g")
                elif temp3(p, "3gh") < t <= temp3(p, "3ef"):
                    vol = region3PT(p, t, "3h")
                elif temp3(p, "3ef") < t <= temp3(p, "3ij"):
                    vol = region3PT(p, t, "3i")
                elif temp3(p, "3ij") < t <= temp3(p, "3jk"):
                    vol = region3PT(p, t, "3j")
                elif t > temp3(p, "3jk"):
                    vol = region3PT(p, t, "3k")
            elif 23e3 < p <= 23.5e3:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= temp3(p, "3gh"):
                    vol = region3PT(p, t, "3l")
                elif temp3(p, "3gh") < t <= temp3(p, "3ef"):
                    vol = region3PT(p, t, "3h")
                elif temp3(p, "3ef") < t <= temp3(p, "3ij"):
                    vol = region3PT(p, t, "3i")
                elif temp3(p, "3ij") < t <= temp3(p, "3jk"):
                    vol = region3PT(p, t, "3j")
                elif t > temp3(p, "3jk"):
                    vol = region3PT(p, t, "3k")
            elif 22.5e3 < p <= 23e3:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= temp3(p, "3gh"):
                    vol = region3PT(p, t, "3l")
                elif temp3(p, "3gh") < t <= temp3(p, "3mn"):
                    vol = region3PT(p, t, "3m")
                elif temp3(p, "3mn") < t <= temp3(p, "3ef"):
                    vol = region3PT(p, t, "3n")
                elif temp3(p, "3ef") < t <= temp3(p, "3op"):
                    vol = region3PT(p, t, "3o")
                elif temp3(p, "3op") < t <= temp3(p, "3ij"):
                    vol = region3PT(p, t, "3p")
                elif temp3(p, "3ij") < t <= temp3(p, "3jk"):
                    vol = region3PT(p, t, "3j")
                elif t > temp3(p, "3jk"):
                    vol = region3PT(p, t, "3k")
            elif p643 < p <= 22.5e3:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= temp3(p, "3qu"):
                    vol = region3PT(p, t, "3q")
                elif temp3(p, "3qu") < t <= temp3(p, "3rx"):
                    vol = cls.auxEqs(p, t)
                elif temp3(p, "3rx") < t <= temp3(p, "3jk"):
                    vol = region3PT(p, t, "3r")
                elif t > temp3(p, "3jk"):
                    vol = region3PT(p, t, "3k")
            elif 20.5e3 < p <= p643:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= region4(psat=p):
                    vol = region3PT(p, t, "3s")
                elif region4(psat=p) < t <= temp3(p, "3jk"):
                    vol = region3PT(p, t, "3r")
                elif t > temp3(p, "3jk"):
                    vol = region3PT(p, t, "3k")
            elif p3cd < p <= 20.5e3:
                if t <= temp3(p, "3cd"):
                    vol = region3PT(p, t, "3c")
                elif temp3(p, "3cd") < t <= region4(psat=p):
                    vol = region3PT(p, t, "3s")
                elif t >= region4(psat=p):
                    vol = region3PT(p, t, "3t")
            elif pmin < p <= p3cd:
                if t <= region4(psat=p):
                    vol = region3PT(p, t, "3c")
                elif t >= region4(psat=p):
                    vol = region3PT(p, t, "3t")
            return 1/vol
        else:
            return None

    @classmethod
    def auxEqs(cls, p, t):
        """Persamaan bantuan untuk subregion 3u sampai 3z untuk daerah mendekati titik kritis"""

        vol = 0.
        pmin = region4(tsat=643.15)

        if temp3(p, "3qu") < t <= temp3(p, "3rx") and pmin < p <= 22.5e3:

            if 21.93161551e3 < p <= 22.064e3 and t < region4(psat=p):
                if temp3(p, "3qu") < p <= temp3(p, "3uv"):
                    vol = region3PT(p, t, "3u")
                elif t > temp3(p, "3uv"):
                    vol = region3PT(p, t, "3y")
            elif p643 < p <= 21.93161551e3 and t < region4(psat=p):
                if t > temp3(p, "3qu"):
                    vol = region3PT(p, t, "3u")
            elif 21.90096265e3 < p <= 22.064e3 and t > region4(psat=p):
                if t <= temp3(p, "3wx"):
                    vol = region3PT(p, t, "3z")
                elif temp3(p, "3wx") < t <= temp3(p, "3rx"):
                    vol = region3PT(p, t, "3x")
            elif pmin < p <= 21.90096265e3 and t > region4(psat=p):
                if t <= temp3(p, "3rx"):
                    vol = region3PT(p, t, "3x")
            elif 22.11e3 < p <= 22.5e3:
                if temp3(p, "3qu") < t <= temp3(p, "3uv"):
                    vol = region3PT(p, t, "3u")
                elif temp3(p, "3uv") < t <= temp3(p, "3ef"):
                    vol = region3PT(p, t, "3v")
                elif temp3(p, "3ef") < t <= temp3(p, "3wx"):
                    vol = region3PT(p, t, "3w")
                elif temp3(p, "3wx") < t <= temp3(p, "3rx"):
                    vol = region3PT(p, t, "3x")
            elif 22.064e3 < p <= 22.11e3:
                if temp3(p, "3qu") < t <= temp3(p, "3uv"):
                    vol = region3PT(p, t, "3u")
                elif temp3(p, "3uv") < t <= temp3(p, "3ef"):
                    vol = region3PT(p, t, "3y")
                elif temp3(p, "3ef") < t <= temp3(p, "3wx"):
                    vol = region3PT(p, t, "3z")
                elif temp3(p, "3wx") < t <= temp3(p, "3rx"):
                    vol = region3PT(p, t, "3x")

            return vol
        else:
            return None