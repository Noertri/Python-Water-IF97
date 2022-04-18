import numpy as np
from ..koefisien import IJnReg3


def phi(delta, tau, desc):

    n = IJnReg3["n"]
    I = IJnReg3["I"]
    J = IJnReg3["J"]
    _phi = dict()
    _phi["phi"] = n[0]*np.log(delta)
    _phi["dphiddelta"] = n[0]/delta
    _phi["dphiddelta2"] = -n[0]/(delta**2)
    _phi["dphidtau"] = 0.
    _phi["dphidtau2"] = 0.
    _phi["dphiddeltadtau"] = 0.

    for Ii, Ji, ni in zip(I[1:], J[1:], n[1:]):
        _phi["phi"] += ni*(delta**Ii)*(tau**Ji)
        _phi["dphiddelta"] += ni*Ii**(delta**(Ii-1))*(tau**Ji)
        _phi["dphiddelta2"] += ni*Ii*(Ii-1)*(delta**(Ii-2))*(tau**Ji)
        _phi["dphidtau"] += ni*Ji*(delta**Ii)*(tau**(Ji-1))
        _phi["dphidtau2"] += ni*Ji*(Ji-1)*(delta**Ii)*(tau**(Ji-2))
        _phi["dphiddeltadtau"] += ni*Ii*Ji*(delta**(Ii-1))*(tau**(Ji-1))

    match desc:
        case "phi":
            return _phi["phi"]
        case "dphiddelta":
            return _phi["dphiddelta"]
        case "dphiddelta2":
            return _phi["dphiddelta2"]
        case "dphidtau":
            return _phi["dphidtau"]
        case "dphidelta2":
            return _phi["dphidtau2"]
        case "dphiddeltadtau":
            return _phi["dphiddeltadtau"]
        case _:
            return None