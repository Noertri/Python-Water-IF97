import numpy as np
from .coefficients import IJH
from .constants import *


def visc(rho, t):
    """Calculate viscosity of ordinary/pure water"""

    delta = rho/RHOC
    tau = t/TEMPC
    theta = 1/tau

    Hi = IJH["Hi"]
    I = IJH["I"]
    J = IJH["J"]
    Hij = IJH["Hij"]

    suma = sum((hi/(tau**i) for hi, i in zip(Hi, range(len(Hi)))))
    mu0 = (100*np.sqrt(tau))/suma

    sumb = sum((hij*((delta-1)**Ji)*((theta-1)**Ii) for Ii, Ji, hij in zip(I, J, Hij)))

    pw = delta*sumb
    mu1 = np.exp(pw)

    _mu = mu0*mu1*1e-6
    return _mu