from math import sqrt
from ..koefisien import nb23


class Boundary23:
    """Persamaan garis batas untuk region 2 dan 3"""

    _n = nb23

    @classmethod
    def getPress(cls, t):
        _n = nb23
        theta = t/1
        ans = cls._n[0] + cls._n[1]*theta + cls._n[2]*(theta**2)
        return ans*1000

    @classmethod
    def getTemp(cls, p):
        pi = p/1000
        ans = cls._n[3] + sqrt((pi - cls._n[4])/cls._n[2])
        return ans*1