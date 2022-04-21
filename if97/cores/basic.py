from ..koefisien import IJnReg1, BIGR


#Region 1
def _region1(p, t, desc=None):
    p = p
    t = t
    pi = p/16.53e3
    tau = 1386/t
    _I = IJnReg1["I"]
    _J = IJnReg1["J"]
    _n = IJnReg1["n"]

    g = 0.
    dgdpi = 0.
    dgdpi2 = 0.
    dgdtau = 0.
    dgdtau2 = 0.
    dgdpidtau = 0.

    for Ii, Ji, ni in zip(_I, _J, _n):
        g += ni*((7.1-pi)**Ii)*((tau-1.222)**Ji)
        dgdpi += -ni*Ii*((7.1-pi)**(Ii-1))*((tau-1.222)**Ji)
        dgdpi2 += ni*Ii*(Ii-1)*((7.1-pi)**(Ii-2))*((tau-1.222)**Ji)
        dgdtau += ni*Ji*((7.1-pi)**Ii)*((tau-1.222)**(Ji-1))
        dgdtau2 += ni*Ji*(Ji-1)*((7.1-pi)**Ii)*((tau-1.222)**(Ji-2))
        dgdpidtau += -ni*Ii*Ji*((7.1-pi)**(Ii-1))*((tau-1.222)**(Ji-1))

    props = dict()

    props["v"] = BIGR*t*pi*dgdpi/p
    props["u"] = BIGR*t*(tau*dgdtau-pi*dgdpi)
    props["s"] = BIGR*(tau*dgdtau-g)
    props["h"] = BIGR*t*tau*dgdtau
    props["cp"] = -1*BIGR*(tau**2)*dgdtau2
    props["cv"] = -1*(tau**2)*dgdtau2 + ((dgdpi-tau*dgdpidtau)**2)/dgdpi2

    if desc and desc.lower() in props.keys():
        return props[desc.lower()]
    else:
        return None