from ..koefisien import IJnReg1, BIGR


class Region1:

    def __init__(self, p, t):
        self.p = p
        self.t = t
        self.pi = p/16.53e3
        self.tau = 1386/t

    def gamma(self, desc=None):
        """Method untuk persamaan dasar gamma dan turunannya"""

        _gamma = dict()
        _gamma["gamma"] = 0.
        _gamma["dgammadpi"] = 0.
        _gamma["dgammadpi2"] = 0.
        _gamma["dgammadtau"] = 0.
        _gamma["dgammadtau2"] = 0.
        _gamma["dgammadpidtau"] = 0.

        for Ii, Ji, ni in zip(IJnReg1["I"], IJnReg1["J"], IJnReg1["n"]):
            _gamma["gamma"] += ni*((7.1-self.pi)**Ii)*((self.tau-1.222)**Ji)
            _gamma["dgammadpi"] += -ni*Ii*((7.1-self.pi)**(Ii-1))*((self.tau-1.222)**Ji)
            _gamma["dgammadpi2"] += ni*Ii*(Ii-1)*((7.1-self.pi)**(Ii-2))*((self.tau-1.222)**Ji)
            _gamma["dgammadtau"] += ni*Ji*((7.1-self.pi)**Ii)*((self.tau-1.222)**(Ji-1))
            _gamma["dgammadtau2"] += ni*Ji*(Ji-1)*((7.1-self.pi)**Ii)*((self.tau-1.222)**(Ji-2))
            _gamma["dgammadpidtau"] += -ni*Ii*Ji*((7.1-self.pi)**(Ii-1))*((self.tau-1.222)**(Ji-1))

        if desc and desc.lower() in _gamma.keys():
            return _gamma[desc.lower()]
        else:
            return None

    def get_properties(self, desc=None):

        props = dict()

        gamm = self.gamma(desc="gamma")
        dgammdpi = self.gamma(desc="dgammadpi")
        dgammdpi2 = self.gamma(desc="dgammadpi2")
        dgammdtau = self.gamma(desc="dgammadtau")
        dgammdtau2 = self.gamma(desc="dgammadtau2")
        dgammdpidtau = self.gamma(desc="dgammadpidtau")

        props["v"] = BIGR*self.t*self.pi*dgammdpi/self.p
        props["u"] = BIGR*self.t*(self.tau*dgammdtau-self.pi*dgammdpi)
        props["s"] = BIGR*(self.tau*dgammdtau-gamm)
        props["h"] = BIGR*self.t*self.tau*dgammdtau
        props["cp"] = -1*BIGR*(self.tau**2)*dgammdtau2
        props["cv"] = -1*(self.tau**2)*dgammdtau2 + ((dgammdpi-self.tau*dgammdpidtau)**2)/dgammdpi2

        if desc and desc.lower() in props.keys():
            return props[desc.lower()]
        else:
            return None