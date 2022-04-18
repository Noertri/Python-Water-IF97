import numpy as np
from ..koefisien import IJnReg2, IJnReg2Supp


class Properties:

    def __init__(self, p, t):
        self.p = p
        self.t = t
        self.pi = p/1e3
        self.tau = 540/t

    def gammao(self, desc=None):

        _gamma = dict()
        _gamma["gamma"] = np.log(self.pi)
        _gamma["dgammadpi"] = 1./self.pi
        _gamma["dgammadpi2"] = -1./(self.pi**2)
        _gamma["dgammadtau"] = 0.
        _gamma["dgammadtau2"] = 0.
        _gamma["dgammadpidtau"] = 0.

        for Jio, nio in zip(IJnReg2["Jo"], IJnReg2["no"]):
            _gamma["gamma"] += nio*(self.tau**Jio)
            _gamma["dgammadtau"] += nio*Jio*(self.tau**(Jio-1))
            _gamma["dgammadtau2"] += nio*Jio*(Jio-1)*(self.tau**(Jio-2))

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

    def gammar(self, desc):

        _gamma = dict()
        _gamma["gamma"] = 0.
        _gamma["dgammadpi"] = 0.
        _gamma["dgammadpi2"] = 0.
        _gamma["dgammadtau"] = 0.
        _gamma["dgammadtau2"] = 0.
        _gamma["dgammadpidtau"] = 0.

        for Ii, Ji, ni in zip(IJnReg2["I"], IJnReg2["J"], IJnReg2["n"]):
            _gamma["gamma"] += ni*(self.pi**Ii)*((self.tau-0.5)**Ji)
            _gamma["dgammadpi"] += ni*Ii*(self.pi**(Ii-1))*((self.tau-0.5)**Ji)
            _gamma["dgammadpi2"] += ni*Ii*(Ii-1)*(self.pi**(Ii-2))*((self.tau-0.5)**Ji)
            _gamma["dgammadtau"] += ni*Ji*(self.pi**Ii)*((self.tau-0.5)**(Ji-1))
            _gamma["dgammadtau2"] += ni*Ji*(Ji-1)*(self.pi**Ii)*((self.tau-0.5)**(Ji-2))
            _gamma["dgammadpidtau"] += ni*Ii*Ji*(self.pi**(Ii-1))*((self.tau-0.5)**(Ji-1))

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

    def supp_gammao(self, desc=None):

        _gamma = dict()
        _gamma["gamma"] = np.log(self.pi)
        _gamma["dgammadpi"] = 1./self.pi
        _gamma["dgammadpi2"] = -1./(self.pi**2)
        _gamma["dgammadtau"] = 0.
        _gamma["dgammadtau2"] = 0.
        _gamma["dgammadpidtau"] = 0.

        for Jio, nio in zip(IJnReg2Supp["Jo"], IJnReg2Supp["no"]):
            _gamma["gamma"] += nio*(self.tau**Jio)
            _gamma["dgammadtau"] += nio*Jio*(self.tau**(Jio-1))
            _gamma["dgammadtau2"] += nio*Jio*(Jio-1)*(self.tau**(Jio-2))

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

    def supp_gammar(self, desc):

        _gamma = dict()
        _gamma["gamma"] = 0.
        _gamma["dgammadpi"] = 0.
        _gamma["dgammadpi2"] = 0.
        _gamma["dgammadtau"] = 0.
        _gamma["dgammadtau2"] = 0.
        _gamma["dgammadpidtau"] = 0.

        for Ii, Ji, ni in zip(IJnReg2Supp["I"], IJnReg2Supp["J"], IJnReg2Supp["n"]):
            _gamma["gamma"] += ni*(self.pi**Ii)*((self.tau-0.5)**Ji)
            _gamma["dgammadpi"] += ni*Ii*(self.pi**(Ii-1))*((self.tau-0.5)**Ji)
            _gamma["dgammadpi2"] += ni*Ii*(Ii-1)*(self.pi**(Ii-2))*((self.tau-0.5)**Ji)
            _gamma["dgammadtau"] += ni*Ji*(self.pi**Ii)*((self.tau-0.5)**(Ji-1))
            _gamma["dgammadtau2"] += ni*Ji*(Ji-1)*(self.pi**Ii)*((self.tau-0.5)**(Ji-2))
            _gamma["dgammadpidtau"] += ni*Ii*Ji*(self.pi**(Ii-1))*((self.tau-0.5)**(Ji-1))

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