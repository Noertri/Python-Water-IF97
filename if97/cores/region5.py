import numpy as np
from ..koefisien import IJnReg5, BIGR


class Region5:

    def __init__(self, p, t):
        self.p = p
        self.t = t
        self.pi = p/1e3
        self.tau = 1000/t

    def gammao(self, desc=None):

        _gamma = dict()
        _gamma["gammao"] = np.log(self.pi)
        _gamma["dgammaodpi"] = 1./self.pi
        _gamma["dgammaodpi2"] = -1./(self.pi**2)
        _gamma["dgammaodtau"] = 0.
        _gamma["dgammaodtau2"] = 0.
        _gamma["dgammaodpidtau"] = 0.

        for Jio, nio in zip(IJnReg5["Jo"], IJnReg5["no"]):
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

        for Ii, Ji, ni in zip(IJnReg5["I"], IJnReg5["J"], IJnReg5["n"]):
            _gamma["gammar"] += ni*(self.pi**Ii)*(self.tau**Ji)
            _gamma["dgammardpi"] += ni*Ii*(self.pi**(Ii-1))*(self.tau**Ji)
            _gamma["dgammardpi2"] += ni*Ii*(Ii-1)*(self.pi**(Ii-2))*(self.tau**Ji)
            _gamma["dgammardtau"] += ni*Ji*(self.pi**Ii)*(self.tau**(Ji-1))
            _gamma["dgammardtau2"] += ni*Ji*(Ji-1)*(self.pi**Ii)*(self.tau**(Ji-2))
            _gamma["dgammardpidtau"] += ni*Ii*Ji*(self.pi**(Ii-1))*(self.tau**(Ji-1))

        if desc and desc.lower() in _gamma.keys():
            return _gamma[desc.lower()]
        else:
            return None

    def get_properties(self, desc):

        props = dict()

        gammo = self.gammao(desc="gammao")
        dgammodpi = self.gammao(desc="dgammaodpi")
        dgammodtau = self.gammao(desc="dgammaodtau")
        dgammodtau2 = self.gammao(desc="dgammaodtau2")
        gammr = self.gammar(desc="gammar")
        dgammrdpi = self.gammar(desc="dgammardpi")
        dgammrdpi2 = self.gammar(desc="dgammardpi2")
        dgammrdtau = self.gammar(desc="dgammardtau")
        dgammrdtau2 = self.gammar(desc="dgammardtau2")
        dgammrdpidtau = self.gammar(desc="dgammardpidtau")

        props["v"] = (BIGR*self.t*self.pi*(dgammrdpi+dgammodpi))/self.p
        props["u"] = BIGR*self.t*(self.tau*(dgammodtau+dgammrdtau)-self.pi*(dgammodpi+dgammrdpi))
        props["s"] = BIGR*(self.tau*(dgammodtau+dgammrdtau)-(gammo+gammr))
        props["h"] = BIGR*self.t*self.tau*(dgammodtau+dgammrdtau)
        props["cp"] = -1*BIGR*(self.tau**2)*(dgammodtau2+dgammrdtau2)
        props["cv"] = BIGR*(-1*(self.tau**2)*(dgammodtau2+dgammrdtau2)-
                            (((1+self.pi*dgammrdpi-self.tau*self.pi*dgammrdpidtau)**2)/(1-(self.pi**2)*dgammrdpi2)))

        if desc and desc.lower() in props.keys():
            return props[desc.lower()]
        else:
            return None