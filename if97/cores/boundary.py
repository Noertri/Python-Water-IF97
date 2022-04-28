from math import sqrt, log
from ..koefisien import nb23, InBoundT3


class Boundary23:
    """Persamaan garis batas untuk region 2 dan 3"""

    _n = nb23

    @classmethod
    def getPress(cls, t):
        if 623.15 <= t <= 863.15:
            _n = nb23
            theta = t/1
            ans = cls._n[0] + cls._n[1]*theta + cls._n[2]*(theta**2)
            return ans*1000
        else:
            return None

    @classmethod
    def getTemp(cls, p):
        if 16.5291643e3 <= p <= 1e5:
            pi = p/1000
            ans = cls._n[3] + sqrt((pi - cls._n[4])/cls._n[2])
            return ans*1
        else:
            return None


def temp3(p, desc=None):
    """Persamaan batas untuk subregion3"""

    pi = p/1e3

    if desc and desc.lower() in InBoundT3.keys():
        if desc.lower() != "3ab" and desc.lower() != "3ef" and desc.lower() != "3op" and desc.lower() != "3wx":
            koef = InBoundT3[desc.lower()]

            theta = 0.
            for ni, Ii in zip(koef["n"], koef["I"]):
                theta += ni*(pi**Ii)

            return theta*1
        elif desc.lower() == "3ab" or desc.lower() == "3op" or desc.lower() == "3wx":
            koef = InBoundT3[desc.lower()]

            theta = 0.
            for ni, Ii in zip(koef["n"], koef["I"]):
                theta += ni*(log(pi)**Ii)

            return theta*1
    elif desc and desc.lower() == "3ef":
        return 3.727888004*(pi-22.064)+647.096
    else:
        return None