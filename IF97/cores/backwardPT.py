"""Contain backward equations using pressure and temperature as inputs"""

from numpy import exp
from .basic import Region4
from .boundary import Boundary23, temp3
from ..coefficients import IJnVPTReg3


class Region3VPT:
    """Class of backward equations for region 3.

    staticmethods
    -------------
    volPT(p, t, desc="")
        Backward equation for region 3.

    classmethods
    ------------
    singleRho(cls, p, t)
        Method for subregion 3a to 3t to get value of density at single phase.
    auxEqs(cls, p, t)
        Auxillary equations for subregion 3u to 3z that near critical point.
    """

    @staticmethod
    def volPT(p, t, desc):
        """Backward equations for subregion 3 to get value of specific volume(v) using presssure(p) and temperature(t) as inputs.

        Parameters
        ----------
        p: float
            pressure (KPa).
        t: float
            temperature (K).
        desc: str
            input key, one of: "3a", "3b", "3c", "3d", "3e", "3f", "3g", "3h", "3i", "3j", "3k", "3l",
            "3m", "3n", "3o", "3p", "3q", "3r", "3s", "3t", "3u", "3v", "3w", "3x", "3y",  "3z".

        Returns
        -------
        v: float
            specific volume (m^3/Kg).

        For more details see References[2, 3].
        """

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
        """Method to get density at single phase for subregion 3a to 3t.

        Limit
        -----
        Valid for:
            623.15 K < t <= 863.15 K and p23 < p <= 100 MPa or 350 C < t <= 800 C and p23 < p <= 100000 KPa,
            p23 represent boundary equation between region 2 and region 3.

        Parameters
        ----------
        p: float
            pressure (KPa).
        t: float
            temperature (K).

        Returns
        -------
        rho: float or None
            return density (Kg/m^3) or None if pressure(p) and/or temperature(t) are not in or exceed range of limmit, see Limit.

        For more details see References[2, 3].
        """

        vol = 0.
        p3cd = 19.00881189173929e3

        if 623.15 < t <= 863.15 and Boundary23.getPress(t) < p <= 1e5:

            #subregion 3a and 3b
            if 4e4 < p <= 1e5 and t <= temp3(p, "3ab"):
                vol = cls.volPT(p, t, "3a")
            elif 4e4 < p <= 1e5 and t > temp3(p, "3ab"):
                vol = cls.volPT(p, t, "3b")

            #subregion 3c, 3d, 3e, 3f
            if 25e3 < p <= 4e4 and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif 25e3 < p <= 4e4 and (temp3(p, "3cd") < t <= temp3(p, "3ab")):
                vol = cls.volPT(p, t, "3d")
            elif 25e3 < p <= 4e4 and (temp3(p, "3ab") < t <= temp3(p, "3ef")):
                vol = cls.volPT(p, t, "3e")
            elif 25e3 < p <= 4e4 and t > temp3(p, "3ef"):
                vol = cls.volPT(p, t, "3f")

            #subregion 3c, 3g, 3h, 3i, 3j, 3k
            if 23.5e3 < p <= 25e3 and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif 23.5e3 < p <= 25e3 and (temp3(p, "3cd") < t <= temp3(p, "3gh")):
                vol = cls.volPT(p, t, "3g")
            elif 23.5e3 < p <= 25e3 and (temp3(p, "3gh") < t <= temp3(p, "3ef")):
                vol = cls.volPT(p, t, "3h")
            elif 23.5e3 < p <= 25e3 and (temp3(p, "3ef") < t <= temp3(p, "3ij")):
                vol = cls.volPT(p, t, "3i")
            elif 23.5e3 < p <= 25e3 and (temp3(p, "3ij") < t <= temp3(p, "3jk")):
                vol = cls.volPT(p, t, "3j")
            elif 23.5e3 < p <= 25e3 and t > temp3(p, "3jk"):
                vol = cls.volPT(p, t, "3k")

            #subregion 3c, 3l, 3h, 3i, 3j, 3k
            if 23e3 < p <= 23.5e3 and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif 23e3 < p <= 23.5e3 and (temp3(p, "3cd") < t <= temp3(p, "3gh")):
                vol = cls.volPT(p, t, "3l")
            elif 23e3 < p <= 23.5e3 and (temp3(p, "3gh") < t <= temp3(p, "3ef")):
                vol = cls.volPT(p, t, "3h")
            elif 23e3 < p <= 23.5e3 and (temp3(p, "3ef") < t <= temp3(p, "3ij")):
                vol = cls.volPT(p, t, "3i")
            elif 23e3 < p <= 23.5e3 and (temp3(p, "3ij") < t <= temp3(p, "3jk")):
                vol = cls.volPT(p, t, "3j")
            elif 23e3 < p <= 23.5e3 and t > temp3(p, "3jk"):
                vol = cls.volPT(p, t, "3k")

            #subregion 3c, 3l, 3m, 3n, 3o, 3p, 3j, 3k
            if 22.5e3 < p <= 23e3 and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif 22.5e3 < p <= 23e3 and (temp3(p, "3cd") < t <= temp3(p, "3gh")):
                vol = cls.volPT(p, t, "3l")
            elif 22.5e3 < p <= 23e3 and (temp3(p, "3gh") < t <= temp3(p, "3mn")):
                vol = cls.volPT(p, t, "3m")
            elif 22.5e3 < p <= 23e3 and (temp3(p, "3mn") < t <= temp3(p, "3ef")):
                vol = cls.volPT(p, t, "3n")
            elif 22.5e3 < p <= 23e3 and (temp3(p, "3ef") < t <= temp3(p, "3op")):
                vol = cls.volPT(p, t, "3o")
            elif 22.5e3 < p <= 23e3 and (emp3(p, "3op") < t <= temp3(p, "3ij")):
                vol = cls.volPT(p, t, "3p")
            elif 22.5e3 < p <= 23e3 and (temp3(p, "3ij") < t <= temp3(p, "3jk")):
                vol = cls.volPT(p, t, "3j")
            elif 22.5e3 < p <= 23e3 and t > temp3(p, "3jk"):
                vol = cls.volPT(p, t, "3k")

            #subregion 3c, 3q, 3r, 3k
            if Region4.getSaturPress(tsat=643.15) < p <= 22.5e3 and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif Region4.getSaturPress(tsat=643.15) < p <= 22.5e3 and (temp3(p, "3cd") < t <= temp3(p, "3qu")):
                vol = cls.volPT(p, t, "3q")
            elif Region4.getSaturPress(tsat=643.15) < p <= 22.5e3 and (temp3(p, "3qu") < t <= temp3(p, "3rx")):
                vol = cls.auxEqs(p, t)
            elif Region4.getSaturPress(tsat=643.15) < p <= 22.5e3 and (temp3(p, "3rx") < t <= temp3(p, "3jk")):
                vol = cls.volPT(p, t, "3r")
            elif Region4.getSaturPress(tsat=643.15) < p <= 22.5e3 and t > temp3(p, "3jk"):
                vol = cls.volPT(p, t, "3k")

            #subregion 3c, 3r, 3s, 3k
            if 20.5e3 < p <= Region4.getSaturPress(tsat=643.15) and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif 20.5e3 < p <= Region4.getSaturPress(tsat=643.15) and (temp3(p, "3cd") < t <= Region4.getSaturTemp(psat=p)):
                vol = cls.volPT(p, t, "3s")
            elif 20.5e3 < p <= Region4.getSaturPress(tsat=643.15) and (Region4.getSaturTemp(psat=p) < t <= temp3(p, "3jk")):
                vol = cls.volPT(p, t, "3r")
            elif 20.5e3 < p <= Region4.getSaturPress(tsat=643.15) and t > temp3(p, "3jk"):
                vol = cls.volPT(p, t, "3k")

            #subregion 3c, 3s, 3t
            if p3cd < p <= 20.5e3 and t <= temp3(p, "3cd"):
                vol = cls.volPT(p, t, "3c")
            elif p3cd < p <= 20.5e3 and (temp3(p, "3cd") < t <= Region4.getSaturTemp(psat=p)):
                vol = cls.volPT(p, t, "3s")
            elif p3cd < p <= 20.5e3 and t >= Region4.getSaturTemp(psat=p):
                vol = cls.volPT(p, t, "3t")

            #subregion 3c, 3t
            if Region4.getSaturPress(tsat=623.15) < p <= p3cd and t <= Region4.getSaturTemp(psat=p):
                vol = cls.volPT(p, t, "3c")
            elif Region4.getSaturPress(tsat=623.15) < p <= p3cd and t >= Region4.getSaturTemp(psat=p):
                vol = cls.volPT(p, t, "3t")

            rho = 1/vol
            return rho
        else:
            return None

    @classmethod
    def auxEqs(cls, p, t):
        """Auxillary equation for subregion 3u to 3z near critical point.

        Limit
        -----
        Valid for:
            T3qu < t <= T3rx and psat(643.15 K) < p <= 22.5 MPa.

        Parameters
        ----------
        p: float
            pressure (KPa).
        t: float
            temperature (K).

        Returns
        -------
        vol: float or None
            return specific volume (m^3/Kg) or None if pressure(p) and/or temperature(t) are not in or exceed range of limit, see Limit.

        For more details see References[2, 3]
        """

        vol = 0.
        if (temp3(p, "3qu") < t <= temp3(p, "3rx")) and Region4.getSaturPress(tsat=643.15) < p <= 22.5e3:

            #subcritical pressure region 3u, 3y
            if t <= Region4.getSaturTemp(psat=p) and 21.93161551e3 < p <= 22.064e3 and (temp3(p, "3qu") < t <= temp3(p, "3uv")):
                vol = cls.volPT(p, t, "3u")
            elif (temp3(p, "3uv") < t <= Region4.getSaturTemp(psat=p)) and 21.93161551e3 < p <= 22.064e3:
                vol = cls.volPT(p, t, "3y")
            elif (temp3(p, "3qu") < t <= Region4.getSaturTemp(psat=p) ) and (Region4.getSaturPress(tsat=643.15) < p <= 21.93161551e3):
                vol = cls.volPT(p, t, "3u")

            #subcritical pressure region 3x, 3z
            if (Region4.getSaturTemp(psat=p) <= t <= temp3(p, "3wx")) and 21.90096265e3 < p <= 22.064e3:
                vol = cls.volPT(p, t, "3z")
            elif t >= Region4.getSaturTemp(psat=p) and 21.90096265e3 < p <= 22.064e3 and (temp3(p, "3wx") < t <= temp3(p, "3rx")):
                vol = cls.volPT(p, t, "3x")
            elif (Region4.getSaturTemp(psat=p) <= t <= temp3(p, "3rx")) and Region4.getSaturPress(tsat=643.15) < p <= 21.90096265e3:
                vol = cls.volPT(p, t, "3x")

            #supercritical pressure region 3u, 3v, 3w, 3x
            if 22.11e3 < p <= 22.5e3 and (temp3(p, "3qu") < t <= temp3(p, "3uv")):
                vol = cls.volPT(p, t, "3u")
            elif 22.11e3 < p <= 22.5e3 and (temp3(p, "3uv") < t <= temp3(p, "3ef")):
                vol = cls.volPT(p, t, "3v")
            elif 22.11e3 < p <= 22.5e3 and (temp3(p, "3ef") < t <= temp3(p, "3wx")):
                vol = cls.volPT(p, t, "3w")
            elif 22.11e3 < p <= 22.5e3 and (temp3(p, "3wx") < t <= temp3(p, "3rx")):
                vol = cls.volPT(p, t, "3x")

            # supercritical pressure region 3u, 3x, 3y, 3z
            if 22.064e3 < p <= 22.11e3 and (temp3(p, "3qu") < t <= temp3(p, "3uv")):
                vol = cls.volPT(p, t, "3u")
            elif 22.064e3 < p <= 22.11e3 and (temp3(p, "3uv") < t <= temp3(p, "3ef")):
                vol = cls.volPT(p, t, "3y")
            elif 22.064e3 < p <= 22.11e3 and (temp3(p, "3ef") < t <= temp3(p, "3wx")):
                vol = cls.volPT(p, t, "3z")
            elif 22.064e3 < p <= 22.11e3 and (temp3(p, "3wx") < t <= temp3(p, "3rx")):
                vol = cls.volPT(p, t, "3x")

            return vol
        else:
            return None