import numpy as np
from .coefficients import IJH
from .constants import *


def _myu0(tbar):

    H = IJH["H"]
    n = len(H)
    sub = 0.

    for i in range(n):
        sub += H[i]/(tbar**i)

    ans = (100*np.sqrt(tbar))/sub

    return ans


def _myu1(tbar, rhobar):

    I = IJH["I"]
    J = IJH["J"]
    H = IJH["Hij"]

    sub1 = 0.
    for i in range(5):
        sub1 += ((1/tbar)-1)**i