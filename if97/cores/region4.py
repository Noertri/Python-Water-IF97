from if97.koefisien import nReg4
import numpy as np


def get_satur_press(tsat):
    _n = nReg4["n"]
    nu = (tsat/1)+(_n[8]/((tsat/1)-_n[9]))
    Ai = (nu**2) + _n[0]*nu + _n[1]
    Bi = _n[2]*(nu**2) + _n[3]*nu + _n[4]
    Ci = _n[5]*(nu**2) + _n[6]*nu + _n[7]
    ans = 1e3*((2*Ci/(-Bi + np.sqrt(Bi**2 - 4*Ai*Ci)))**4)
    return ans


def get_satur_temp(psat):
    _n = nReg4["n"]
    beta = (psat/1000)**(1/4)
    Ei = (beta**2) + _n[2]*beta + _n[5]
    Fi = _n[0]*(beta**2) + _n[3]*beta + _n[6]
    Gi = _n[1]*(beta**2) + _n[4]*beta + _n[7]
    Di = 2*Gi/(-Fi - np.sqrt((Fi**2) - 4*Ei*Gi))
    ans = 1*((_n[9] + Di - np.sqrt((_n[9] + Di)**2 - 4*(_n[8] + _n[9]*Di)))/2)
    return ans