import numpy as np
from ..koefisien import IJnReg2, IJnReg2Supp


def gammao(pi, tau, desc=None):

    _gamma = dict()
    _gamma["gamma"] = np.log(pi)
    _gamma["dgammadpi"] = 1./pi
    _gamma["dgammadpi2"] = -1./(pi**2)
    _gamma["dgammadtau"] = 0.
    _gamma["dgammadtau2"] = 0.
    _gamma["dgammadpidtau"] = 0.

    for Jio, nio in zip(IJnReg2["Jo"], IJnReg2["no"]):
        _gamma["gamma"] += nio*(tau**Jio)
        _gamma["dgammadtau"] += nio*Jio*(tau**(Jio-1))
        _gamma["dgammadtau2"] += nio*Jio*(Jio-1)*(tau**(Jio-2))

    match desc:
        case "gamma":
            return _gamma["gamma"]
        case "dgammadpi":
            return _gamma["dgammadpi"]
        case "dgammadpi2":
            return _gamma["dgammadpi2"]
        case "dgammadtau":
            return _gamma["dgammadtau"]
        case "dgammadtau2":
            return _gamma["dgammadtau2"]
        case "dgammadpidtau":
            return _gamma["dgammadpidtau"]
        case _:
            return Nome


def gammar(pi, tau, desc):

    _gamma = dict()
    _gamma["gamma"] = 0.
    _gamma["dgammadpi"] = 0.
    _gamma["dgammadpi2"] = 0.
    _gamma["dgammadtau"] = 0.
    _gamma["dgammadtau2"] = 0.
    _gamma["dgammadpidtau"] = 0.

    for Ii, Ji, ni in zip(IJnReg2["I"], IJnReg2["J"], IJnReg2["n"]):
        _gamma["gamma"] += ni*(pi**Ii)*((tau-0.5)**Ji)
        _gamma["dgammadpi"] += ni*Ii*(pi**(Ii-1))*((tau-0.5)**Ji)
        _gamma["dgammadpi2"] += ni*Ii*(Ii-1)*(pi**(Ii-2))*((tau-0.5)**Ji)
        _gamma["dgammadtau"] += ni*Ji*(pi**Ii)*((tau-0.5)**(Ji-1))
        _gamma["dgammadtau2"] += ni*Ji*(Ji-1)*(pi**Ii)*((tau-0.5)**(Ji-2))
        _gamma["dgammadpidtau"] += ni*Ii*Ji*(pi**(Ii-1))*((tau-0.5)**(Ji-1))

    match desc:
        case "gamma":
            return _gamma["gamma"]
        case "dgammadpi":
            return _gamma["dgammadpi"]
        case "dgammadpi2":
            return _gamma["dgammadpi2"]
        case "dgammadtau":
            return _gamma["dgammadtau"]
        case "dgammadtau2":
            return _gamma["dgammadtau2"]
        case "dgammadpidtau":
            return _gamma["dgammadpidtau"]
        case _:
            return Nome


def supp_gammao(pi, tau, desc=None):

    _gamma = dict()
    _gamma["gamma"] = np.log(pi)
    _gamma["dgammadpi"] = 1./pi
    _gamma["dgammadpi2"] = -1./(pi**2)
    _gamma["dgammadtau"] = 0.
    _gamma["dgammadtau2"] = 0.
    _gamma["dgammadpidtau"] = 0.

    for Jio, nio in zip(IJnReg2Supp["Jo"], IJnReg2Supp["no"]):
        _gamma["gamma"] += nio*(tau**Jio)
        _gamma["dgammadtau"] += nio*Jio*(tau**(Jio-1))
        _gamma["dgammadtau2"] += nio*Jio*(Jio-1)*(tau**(Jio-2))

    match desc:
        case "gamma":
            return _gamma["gamma"]
        case "dgammadpi":
            return _gamma["dgammadpi"]
        case "dgammadpi2":
            return _gamma["dgammadpi2"]
        case "dgammadtau":
            return _gamma["dgammadtau"]
        case "dgammadtau2":
            return _gamma["dgammadtau2"]
        case "dgammadpidtau":
            return _gamma["dgammadpidtau"]
        case _:
            return Nome


def supp_gammar(pi, tau, desc):

    _gamma = dict()
    _gamma["gamma"] = 0.
    _gamma["dgammadpi"] = 0.
    _gamma["dgammadpi2"] = 0.
    _gamma["dgammadtau"] = 0.
    _gamma["dgammadtau2"] = 0.
    _gamma["dgammadpidtau"] = 0.

    for Ii, Ji, ni in zip(IJnReg2Supp["I"], IJnReg2Supp["J"], IJnReg2Supp["n"]):
        _gamma["gamma"] += ni*(pi**Ii)*((tau-0.5)**Ji)
        _gamma["dgammadpi"] += ni*Ii*(pi**(Ii-1))*((tau-0.5)**Ji)
        _gamma["dgammadpi2"] += ni*Ii*(Ii-1)*(pi**(Ii-2))*((tau-0.5)**Ji)
        _gamma["dgammadtau"] += ni*Ji*(pi**Ii)*((tau-0.5)**(Ji-1))
        _gamma["dgammadtau2"] += ni*Ji*(Ji-1)*(pi**Ii)*((tau-0.5)**(Ji-2))
        _gamma["dgammadpidtau"] += ni*Ii*Ji*(pi**(Ii-1))*((tau-0.5)**(Ji-1))

    match desc:
        case "gamma":
            return _gamma["gamma"]
        case "dgammadpi":
            return _gamma["dgammadpi"]
        case "dgammadpi2":
            return _gamma["dgammadpi2"]
        case "dgammadtau":
            return _gamma["dgammadtau"]
        case "dgammadtau2":
            return _gamma["dgammadtau2"]
        case "dgammadpidtau":
            return _gamma["dgammadpidtau"]
        case _:
            return Nome