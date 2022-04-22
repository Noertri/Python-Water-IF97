import numpy as np
from ..koefisien import IJnReg3, RHOC, TEMPC, BIGR
from scipy import optimize


class Region3:

    def phi(self, delta, tau, desc):

        n = IJnReg3["n"]
        I = IJnReg3["I"]
        J = IJnReg3["J"]
        _phi = dict()
        _phi["phi"] = n[0]*np.log(abs(delta))
        _phi["dphiddelta"] = n[0]/delta
        _phi["dphiddelta2"] = (-1*n[0])/(delta**2)
        _phi["dphidtau"] = 0.
        _phi["dphidtau2"] = 0.
        _phi["dphiddeltadtau"] = 0.

        for Ii, Ji, ni in zip(I[1:], J[1:], n[1:]):
            _phi["phi"] += ni*(delta**Ii)*(tau**Ji)
            _phi["dphiddelta"] += ni*Ii*(delta**(Ii-1))*(tau**Ji)
            _phi["dphiddelta2"] += ni*Ii*(Ii-1)*(delta**(Ii-2))*(tau**Ji)
            _phi["dphidtau"] += ni*Ji*(delta**Ii)*(tau**(Ji-1))
            _phi["dphidtau2"] += ni*Ji*(Ji-1)*(delta**Ii)*(tau**(Ji-2))
            _phi["dphiddeltadtau"] += ni*Ii*Ji*(delta**(Ii-1))*(tau**(Ji-1))

        if desc and desc.lower() in _phi.keys():
            return _phi[desc.lower()]
        else:
            return None

    def func(self, delta, p, t):
        tau = TEMPC/t
        # delta = rho/RHOC
        c = p/(RHOC*BIGR*t)

        dphiddel = self.phi(delta, tau, desc="dphiddelta")

        f1 = (delta**2)*dphiddel-c

        return f1

    def get_properties(self, rho, t, desc=None):

        props = dict()

        delta = rho/RHOC
        tau = TEMPC/t

        phi = self.phi(delta, tau, desc="phi")
        dphiddelta = self.phi(delta, tau, desc="dphiddelta")
        dphiddelta2 = self.phi(delta, tau, desc="dphiddelta2")
        dphidtau = self.phi(delta, tau, desc="dphidtau")
        dphidtau2 = self.phi(delta, tau, desc="dphidtau2")
        dphiddeltadtau = self.phi(delta, tau, desc="dphiddeltadtau")

        props["p"] = rho*BIGR*t*delta*dphiddelta
        props["u"] = BIGR*t*tau*dphidtau
        props["s"] = BIGR*(tau*dphidtau-phi)
        props["h"] = BIGR*t*(tau*dphidtau+delta*dphiddelta)
        props["cv"] = -1*BIGR*(dphidtau2**2)
        props["cp"] = BIGR*(-1*(tau**2)*dphidtau2+(((delta*dphiddelta-delta*tau*dphiddeltadtau)**2)/(
                2*delta*dphiddelta+(delta**2)*dphiddelta2)))

        if desc and desc.lower() in props.keys():
            return props[desc.lower()]
        else:
            return None