import numpy as np
from ..koefisien import IJnReg3, RHOC, TEMPC, BIGR


class Region3:

    def __init__(self, rho, t):
        self.rho = rho
        self.t = t
        self.delta = rho/RHOC
        self.tau = TEMPC/t

    def phi(self, desc):

        n = IJnReg3["n"]
        I = IJnReg3["I"]
        J = IJnReg3["J"]
        _phi = dict()
        _phi["phi"] = n[0]*np.log(self.delta)
        _phi["dphiddelta"] = n[0]/self.delta
        _phi["dphiddelta2"] = (-1*n[0])/(self.delta**2)
        _phi["dphidtau"] = 0.
        _phi["dphidtau2"] = 0.
        _phi["dphiddeltadtau"] = 0.

        for Ii, Ji, ni in zip(I[1:], J[1:], n[1:]):
            _phi["phi"] += ni*(self.delta**Ii)*(self.tau**Ji)
            _phi["dphiddelta"] += ni*Ii*(self.delta**(Ii-1))*(self.tau**Ji)
            _phi["dphiddelta2"] += ni*Ii*(Ii-1)*(self.delta**(Ii-2))*(self.tau**Ji)
            _phi["dphidtau"] += ni*Ji*(self.delta**Ii)*(self.tau**(Ji-1))
            _phi["dphidtau2"] += ni*Ji*(Ji-1)*(self.delta**Ii)*(self.tau**(Ji-2))
            _phi["dphiddeltadtau"] += ni*Ii*Ji*(self.delta**(Ii-1))*(self.tau**(Ji-1))

        if desc and desc.lower() in _phi.keys():
            return _phi[desc.lower()]
        else:
            return None

    def get_properties(self, desc=None):

        props = dict()

        phi = self.phi(desc="phi")
        dphiddelta = self.phi(desc="dphiddelta")
        dphiddelta2 = self.phi(desc="dphiddelta2")
        dphidtau = self.phi(desc="dphidtau")
        dphidtau2 = self.phi(desc="dphidtau2")
        dphiddeltadtau = self.phi(desc="dphiddeltadtau")

        props["p"] = self.rho*BIGR*self.t*self.delta*dphiddelta
        props["u"] = BIGR*self.t*self.tau*dphidtau
        props["s"] = BIGR*(self.tau*dphidtau-phi)
        props["h"] = BIGR*self.t*(self.tau*dphidtau+self.delta*dphiddelta)
        props["cv"] = -1*BIGR*(dphidtau2**2)
        props["cp"] = BIGR*(-1*(self.tau**2)*dphidtau2+(((self.delta*dphiddelta-self.delta*self.tau*dphiddeltadtau)**2)/(
                2*self.delta*dphiddelta+(self.delta**2)*dphiddelta2)))

        if desc and desc.lower() in props.keys():
            return props[desc.lower()]
        else:
            return None