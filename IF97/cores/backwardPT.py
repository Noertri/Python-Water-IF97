from numpy import exp
from ..coefficients import IJnVPTReg3
from .boundary import Boundary23, temp3
from .basic import Region4


class Region3VPT:
    """Implementasi persamaan balik region 3 v(P, T)"""

    @classmethod
    def volPT(cls, p, t, desc=""):
        """Persamaan balik untuk region 3"""

        if desc and desc.lower() != "3n":
            a = IJnVPTReg3[desc.lower()]["a"]
            b = IJnVPTReg3[desc.lower()]["b"]
            c = IJnVPTReg3[desc.lower()]["c"]
            d = IJnVPTReg3[desc.lower()]["d"]
            e = IJnVPTReg3[desc.lower()]["e"]
            I = IJnVPTReg3[desc.lower()]["I"]
            J = IJnVPTReg3[desc.lower()]["J"]
            n = IJnVPTReg3[desc.lower()]["n"]
            v0 = IJnVPTReg3[desc.lower()]["vol0"]
            p0 = IJnVPTReg3[desc.lower()]["press0"]
            t0 = IJnVPTReg3[desc.lower()]["temp0"]

            pi = p/p0
            theta = t/t0

            omega = 0.
            for Ii, Ji, ni, in zip(I, J, n):
                omega += ni*(((pi-a)**c)**Ii)*(((theta-b)**d)**Ji)

            v = v0*(omega**e)
            return v
        elif desc and desc.lower() == "3n":
            a = IJnVPTReg3["3n"]["a"]
            b = IJnVPTReg3["3n"]["b"]
            I = IJnVPTReg3["3n"]["I"]
            J = IJnVPTReg3["3n"]["J"]
            n = IJnVPTReg3["3n"]["n"]
            v0 = IJnVPTReg3["3n"]["vol0"]
            p0 = IJnVPTReg3["3n"]["press0"]
            t0 = IJnVPTReg3["3n"]["temp0"]

            pi = p/p0
            theta = t/t0

            omega = 0.
            for Ii, Ji, ni, in zip(I, J, n):
                omega += ni*((pi-a)**Ii)*((theta-b)**Ji)

            v = v0*exp(omega)
            return v
        else:
            return None

    @classmethod
    def singleRho(cls, p, t):
        """Implementasi persamaan subregion 3a sampai 3t"""

        vol = 0.
        p3cd = 19.00881189173929e3

        if 623.15 < t <= 863.15 and (p23 := Boundary23.getPress(t)) < p <= 1e5:
            if 4e4 < p <= 1e5:
                if t <= (t3ab := (t3ab := temp3(p, "3ab"))):
                    vol = cls.volPT(p, t, "3a")
                elif t > (t3ab := temp3(p, "3ab")):
                    vol = cls.volPT(p, t, "3b")
            elif 25e3 < p <= 4e4:
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= (t3ab := temp3(p, "3ab")):
                    vol = cls.volPT(p, t, "3d")
                elif (t3ab := temp3(p, "3ab")) < t <= (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3e")
                elif t > (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3f")
            elif 23.5e3 < p <= 25e3:
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= (t3gh := temp3(p, "3gh")):
                    vol = cls.volPT(p, t, "3g")
                elif (t3gh := temp3(p, "3gh")) < t <= (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3h")
                elif (t3ef := temp3(p, "3ef")) < t <= (t3ij := temp3(p, "3ij")):
                    vol = cls.volPT(p, t, "3i")
                elif (t3ij := temp3(p, "3ij")) < t <= (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3j")
                elif t > (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3k")
            elif 23e3 < p <= 23.5e3:
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= (t3gh := temp3(p, "3gh")):
                    vol = cls.volPT(p, t, "3l")
                elif (t3gh := temp3(p, "3gh")) < t <= (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3h")
                elif (t3ef := temp3(p, "3ef")) < t <= (t3ij := temp3(p, "3ij")):
                    vol = cls.volPT(p, t, "3i")
                elif (t3ij := temp3(p, "3ij")) < t <= (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3j")
                elif t > (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3k")
            elif 22.5e3 < p <= 23e3:
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= (t3gh := temp3(p, "3gh")):
                    vol = cls.volPT(p, t, "3l")
                elif (t3gh := temp3(p, "3gh")) < t <= (t3mn := temp3(p, "3mn")):
                    vol = cls.volPT(p, t, "3m")
                elif (t3mn := temp3(p, "3mn")) < t <= (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3n")
                elif (t3ef := temp3(p, "3ef")) < t <= (t3op := temp3(p, "3op")):
                    vol = cls.volPT(p, t, "3o")
                elif (t3op := temp3(p, "3op")) < t <= (t3ij := temp3(p, "3ij")):
                    vol = cls.volPT(p, t, "3p")
                elif (t3ij := temp3(p, "3ij")) < t <= (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3j")
                elif t > (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3k")
            elif (p643 := Region4.getSaturPress(tsat=643.15)) < p <= 22.5e3:
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= (t3qu := temp3(p, "3qu")):
                    vol = cls.volPT(p, t, "3q")
                elif (t3qu := temp3(p, "3qu")) < t <= (t3rx := temp3(p, "3rx")):
                    vol = cls.auxEqs(p, t)
                elif (t3rx := temp3(p, "3rx")) < t <= (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3r")
                elif t > (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3k")
            elif 20.5e3 < p <= (p643 := Region4.getSaturPress(tsat=643.15)):
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= Region4.getSaturTemp(psat=p):
                    vol = cls.volPT(p, t, "3s")
                elif Region4.getSaturTemp(psat=p) < t <= (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3r")
                elif t > (t3jk := temp3(p, "3jk")):
                    vol = cls.volPT(p, t, "3k")
            elif p3cd < p <= 20.5e3:
                if t <= (t3cd := temp3(p, "3cd")):
                    vol = cls.volPT(p, t, "3c")
                elif (t3cd := temp3(p, "3cd")) < t <= Region4.getSaturTemp(psat=p):
                    vol = cls.volPT(p, t, "3s")
                elif t >= (tsat := Region4.getSaturTemp(psat=p)):
                    vol = cls.volPT(p, t, "3t")
            elif (pmin := Region4.getSaturPress(tsat=623.15)) < p <= p3cd:
                if t <= (tsat := Region4.getSaturTemp(psat=p)):
                    vol = cls.volPT(p, t, "3c")
                elif t >= (tsat := Region4.getSaturTemp(psat=p)):
                    vol = cls.volPT(p, t, "3t")
            return 1/vol
        else:
            return None

    @classmethod
    def auxEqs(cls, p, t):
        """Persamaan bantuan untuk subregion 3u sampai 3z untuk daerah mendekati titik kritis"""

        vol = 0.

        if (t3qu := temp3(p, "3qu")) < t <= (t3rx := temp3(p, "3rx")) and (pmin := Region4.getSaturPress(tsat=643.15)) < p <= 22.5e3:
            if 21.93161551e3 < p <= 22.064e3 and t < (tsat := Region4.getSaturTemp(psat=p)):
                if (t3qu := temp3(p, "3qu")) < p <= (t3uv := temp3(p, "3uv")):
                    vol = cls.volPT(p, t, "3u")
                elif t > (t3uv := temp3(p, "3uv")):
                    vol = cls.volPT(p, t, "3y")
            elif (pmin := Region4.getSaturPress(tsat=643.15)) < p <= 21.93161551e3 and t < (tsat := Region4.getSaturTemp(psat=p)):
                if t > (t3qu := temp3(p, "3qu")):
                    vol = cls.volPT(p, t, "3u")
            elif 21.90096265e3 < p <= 22.064e3 and t > (tsat := Region4.getSaturTemp(psat=p)):
                if t <= (t3wx := temp3(p, "3wx")):
                    vol = cls.volPT(p, t, "3z")
                elif (t3wx := temp3(p, "3wx")) < t <= (t3rx := temp3(p, "3rx")):
                    vol = cls.volPT(p, t, "3x")
            elif (pmin := Region4.getSaturPress(tsat=643.15)) < p <= 21.90096265e3 and t > Region4.getSaturTemp(psat=p):
                if t <= (t3rx := temp3(p, "3rx")):
                    vol = cls.volPT(p, t, "3x")
            elif 22.11e3 < p <= 22.5e3:
                if (t3qu := temp3(p, "3qu")) < t <= (t3uv := temp3(p, "3uv")):
                    vol = cls.volPT(p, t, "3u")
                elif (t3uv := temp3(p, "3uv")) < t <= (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3v")
                elif (t3ef := temp3(p, "3ef")) < t <= (t3wx := temp3(p, "3wx")):
                    vol = cls.volPT(p, t, "3w")
                elif (t3wx := temp3(p, "3wx")) < t <= (t3rx := temp3(p, "3rx")):
                    vol = cls.volPT(p, t, "3x")
            elif 22.064e3 < p <= 22.11e3:
                if (t3qu := temp3(p, "3qu")) < t <= (t3uv := temp3(p, "3uv")):
                    vol = cls.volPT(p, t, "3u")
                elif (t3uv := temp3(p, "3uv")) < t <= (t3ef := temp3(p, "3ef")):
                    vol = cls.volPT(p, t, "3y")
                elif (t3ef := temp3(p, "3ef")) < t <= (t3wx := temp3(p, "3wx")):
                    vol = cls.volPT(p, t, "3z")
                elif (t3wx := temp3(p, "3wx")) < t <= (t3rx := temp3(p, "3rx")):
                    vol = cls.volPT(p, t, "3x")

            return vol
        else:
            return None