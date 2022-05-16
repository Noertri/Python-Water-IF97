from math import log, sqrt
from ..coefficients import InBoundT3, nb23


class Boundary23:
    """Class for boundary equations between region 2 and 3.

    class Methods
    -------------
    getPress(cls, t)
        find pressure at boundary line between region 2 and region 3.
    getTemp(cls, p)
        find temperature at boundary line betweeen region 2 and region 3.
    """

    _n = nb23

    @classmethod
    def getPress(cls, t):
        """Find pressure at boundary line between region 2 and region 3.

        Limit
        -----
        Valid for:
            623.15 K <= t <= 863.15 K or 350 C <= t <= 800 C.

        Parameters
        ----------
        t: float
            temperature (K).

        Returns
        -------
        p: float or None
            return presssure (KPa) or None if value of temperature(t) is not in or exceed range of limit.
        """

        if 623.15 <= t <= 863.15:
            _n = nb23
            theta = t/1
            p = cls._n[0] + cls._n[1]*theta + cls._n[2]*(theta**2)
            return p*1000
        else:
            return None

    @classmethod
    def getTemp(cls, p):
        """Find temperature at boundary line between region 2 and region 3.

        Limit
        -----
        Valid for:
            16.5291643e3 KPa <= p <= 1e5 KPa or 16.5291643 MPa <= p <= 100 MPa.

        Parameters
        ----------
        p: float
            presssure (KPa).

        Returns
        -------
        t: float or None
            return temperature (K) or None if value of pressure(p) is not in or exceed range of limit return None instead.
        """

        if 16.5291643e3 <= p <= 1e5:
            pi = p/1000
            t = cls._n[3] + sqrt((pi - cls._n[4])/cls._n[2])
            return t*1
        else:
            return None


def temp3(p, desc):
    """Boundary equations for subregion 3.

    Parameters
    ----------
    p: float
        presssure (KPa).
    desc: str
        input key, one of: "3ab", "3cd", "3gh", "3ij", "3jk", "3mn", "3op", "3qu", "3rx", "3uv", "3wx".

    Returns
    -------
    t: float or None
        return temperature (K) or None if value of desc is wrong key.


    For more details see http://www.iapws.org/relguide/Supp-VPT3-2016.pdf.
    """

    pi = p/1e3

    if desc and desc.lower() in InBoundT3.keys():
        if desc.lower() != "3ab" and desc.lower() != "3ef" and desc.lower() != "3op" and desc.lower() != "3wx":
            koef = InBoundT3[desc.lower()]

            theta = 0.
            for ni, Ii in zip(koef["n"], koef["I"]):
                theta += ni*(pi**Ii)

            t = theta*1
            return t
        elif desc.lower() == "3ab" or desc.lower() == "3op" or desc.lower() == "3wx":
            koef = InBoundT3[desc.lower()]

            theta = 0.
            for ni, Ii in zip(koef["n"], koef["I"]):
                theta += ni*(log(pi)**Ii)

            t = theta*1
            return t
    elif desc and desc.lower() == "3ef":
        t = 3.727888004*(pi-22.064)+647.096
        return t
    else:
        return None