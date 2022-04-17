from if97.koefisien import nReg4
import numpy as np


def get_satur_press(tsat):
    n = nReg4["n"]
    nu = (tsat/1)+(n[8]/((tsat/1)-n[9]))
    Ai = (nu**2)+n[0]*nu+n[1]
    Bi = n[2]*(nu**2)+n[3]*nu+n[4]
    Ci = n[5]*(nu**2)+n[6]*nu+n[7]
    ans = 1e3*((2*Ci/(-Bi + np.sqrt(Bi**2 - 4*Ai*Ci)))**4)
    return ans


def get_satur_temp(psat):
    n = nReg4["n"]
    beta = (psat/1000)**(1/4)
    Ei = (beta**2)+n[2]*beta+n[5]
    Fi = n[0]*(beta**2)+n[3]*beta+n[6]
    Gi = n[1]*(beta**2)+n[4]*beta+n[7]
    Di = 2*Gi/(-Fi - np.sqrt((Fi**2) - 4*Ei*Gi))
    ans = 1*((n[9]+Di-np.sqrt((n[9]+Di)**2-4*(n[8]+n[9]*Di)))/2)
    return ans