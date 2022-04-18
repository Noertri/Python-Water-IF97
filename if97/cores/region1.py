from ..koefisien import IJnReg1


def gamma(pi, tau, desc=None):
    """Fungsi untuk persamaan gamma dan turunannya"""

    _gamma = dict()
    _gamma["gamma"] = 0.
    _gamma["dgammadpi"] = 0.
    _gamma["dgammadpi2"] = 0.
    _gamma["dgammadtau"] = 0.
    _gamma["dgammadtau2"] = 0.
    _gamma["dgammadpidtau"] = 0.

    for Ii, Ji, ni in zip(IJnReg1.values()):
        _gamma["gamma"] += ni*((7.1-pi)**Ii)*((tau-1.222)**Ji)
        _gamma["dgammadpi"] += -ni*Ii*((7.1-pi)**(Ii-1))*((tau-1.222)**Ji)
        _gamma["dgammadpi2"] += ni*Ii*(Ii-1)*((7.1-pi)**(Ii-2))*((tau-1.222)**Ji)
        _gamma["dgammadtau"] += ni*Ji*((7.1-pi)**Ii)*((tau-1.222)**(Ji-1))
        _gamma["dgammadtau2"] += ni*Ji*(Ji-1)*((7.1-pi)**Ii)*((tau-1.222)**(Ji-2))
        _gamma["dgammadpidtau"] += -ni*Ii*Ji*((7.1-pi)**(Ii-1))*((tau-1.222)**(Ji-1))

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