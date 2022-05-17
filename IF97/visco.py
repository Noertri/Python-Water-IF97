import numpy as np
from .coefficients import IJH
from .constants import *


def visc(rho, t):
    """Calculate dynamic viscosity of ordinary/pure water

    Limit
    -----
    Valid for:
        273.15 K <= t <= 1173.15 K or 0 C <= t <= 900 C and 0 MPa < p <= 100 MPa or 0 KPa < p <= 100000 KPa.

    Parameters
    ----------
    rho: float
        density (Kg/m^3).
    t: float
        temperature (K).

    Returns
    -------
    _mu: float
        return value of dynamic viscosity (*1e-6 Pa*s)
    """

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