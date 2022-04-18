from ..koefisien import IJnReg1, BIGR


class Properties:

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

    def get_spec_vol(self):

        dgamdpi = self.gamma(desc="dgammadpi")

        return (BIGR*self.t*self.pi*dgamdpi)/self.p

    def get_intenal_energy(self):

        dgamdpi = self.gamma(desc="dgammadpi")
        dgamdtau = self.gamma(desc="dgammadtau")

        return BIGR*self.t*(self.tau*dgamdtau-self.pi*dgamdpi)

    def get_entropy(self):

        dgamdtau = self.gamma(desc="dgammadtau")
        gamm = self.gamma(desc="gamma")

        return BIGR*(self.tau*dgamdtau-gamm)

    def get_enthalpy(self):

        dgammdtau = self.gamma(desc="dgammadtau")

        return BIGR*self.tau*self.t*dgammdtau

    def get_cp(self):

        dgamdtau2 = self.gamma(desc="dgammadtau2")

        return -1*BIGR*(self.tau**2)*dgamdtau2

    def get_cv(self):

        dgamdtau2 = self.gamma(desc="dgammadtau2")
        dgamdpi = self.gamma(desc="dgammadpi")
        dgamdpi2 = self.gamma(desc="dgammadpi2")
        dgamdpidtau = self.gamma(desc="dgammadpidtau")

        return -1*(self.tau**2)*dgamdtau2 + ((dgamdpi-self.tau*dgamdpidtau)**2)/dgamdpi2