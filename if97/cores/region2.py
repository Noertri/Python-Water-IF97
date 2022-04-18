import numpy as np
from ..koefisien import IJnReg2, IJnReg2Supp, BIGR


class Region2:
    """Untuk mencari properties pada fase uap dan pada titik saturasi dengan tekanan saturasi lebih dari 10 MPa"""

    def __init__(self, p, t):
        self.p = p
        self.t = t
        self.pi = p/1e3
        self.tau = 540/t

    def gammao(self, desc=None):

        _gamma = dict()
        _gamma["gammao"] = np.log(self.pi)
        _gamma["dgammaodpi"] = 1./self.pi
        _gamma["dgammaodpi2"] = -1./(self.pi**2)
        _gamma["dgammaodtau"] = 0.
        _gamma["dgammaodtau2"] = 0.
        _gamma["dgammaodpidtau"] = 0.

        for Jio, nio in zip(IJnReg2["Jo"], IJnReg2["no"]):
            _gamma["gammao"] += nio*(self.tau**Jio)
            _gamma["dgammaodtau"] += nio*Jio*(self.tau**(Jio-1))
            _gamma["dgammaodtau2"] += nio*Jio*(Jio-1)*(self.tau**(Jio-2))

        if desc and desc.lower() in _gamma.keys():
            return _gamma[desc.lower()]
        else:
            return None

    def gammar(self, desc):

        _gamma = dict()
        _gamma["gammar"] = 0.
        _gamma["dgammardpi"] = 0.
        _gamma["dgammardpi2"] = 0.
        _gamma["dgammardtau"] = 0.
        _gamma["dgammardtau2"] = 0.
        _gamma["dgammardpidtau"] = 0.

        for Ii, Ji, ni in zip(IJnReg2["I"], IJnReg2["J"], IJnReg2["n"]):
            _gamma["gammar"] += ni*(self.pi**Ii)*((self.tau-0.5)**Ji)
            _gamma["dgammardpi"] += ni*Ii*(self.pi**(Ii-1))*((self.tau-0.5)**Ji)
            _gamma["dgammardpi2"] += ni*Ii*(Ii-1)*(self.pi**(Ii-2))*((self.tau-0.5)**Ji)
            _gamma["dgammardtau"] += ni*Ji*(self.pi**Ii)*((self.tau-0.5)**(Ji-1))
            _gamma["dgammardtau2"] += ni*Ji*(Ji-1)*(self.pi**Ii)*((self.tau-0.5)**(Ji-2))
            _gamma["dgammardpidtau"] += ni*Ii*Ji*(self.pi**(Ii-1))*((self.tau-0.5)**(Ji-1))

        if desc and desc.lower() in _gamma.keys():
            return _gamma[desc.lower()]
        else:
            return None

    def get_properties(self):

        props = dict()

        gammo = self.gammao(desc="gammao")
        gammr = self.gammar(desc="gammar")
        dgammodpi = self.gammao(desc="dgammaodpi")
        dgammrdpi = self.gammar(desc="dgammardpi")
        dgammrdpi2 = self.gammar(desc="dgammrdpi2")
        dgammodtau = self.gammao(desc="dgammaodtau")
        dgammodtau2 = self.gammao(desc="dgammadtau2")
        dgammrdtau = self.gammar(desc="dgammardtau")
        dgammrdtau2 = self.gamma(desc="dgammardtau2")
        dgammrdpidtau = self.gammar(desc="dgammardpidtau")

        props["v"] = BIGR*self.t*self.pi*(dgammodpi+dgammrdpi)/self.p
        props["u"] = BIGR*self.t*(self.tau*(dgammodtau+dgammrdtau)-self.pi*(dgammodpi+dgammrdpi))
        props["s"] = BIGR*(self.tau*(dgammodtau+dgammrdtau)-(gammo-gammr))
        props["h"] = BIGR*self.t*self.tau*(dgammodtau+dgammrdtau)
        props["cp"] = -1*BIGR*(self.tau**2)*(dgammodtau2+dgammrdtau2)
        props["cv"] = -1*(self.tau**2)*(dgammodtau2+dgammrdtau2)-(((1+self.pi*dgammrdpi-self.tau*self.pi*dgammrdpidtau)**2)/(1-(self.pi**2)*dgammrdpi2))

        if desc and desc.lower() in props.keys():
            return props[desc.lower()]
        else:
            return None


class SuppRegion2:

    def __init__(self, p, t):
        self.p = p
        self.t = t
        self.pi = p/1e3
        self.tau = 540/t

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
                return None

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
                return None