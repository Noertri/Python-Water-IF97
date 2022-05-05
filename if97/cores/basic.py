import numpy as np
from scipy import optimize
from ..koefisien import IJnReg1, IJnReg2, IJnReg2Supp, IJnReg3, nReg4, IJnReg5, BIGR, RHOC, TEMPC


#Region 1
def region1(p, t, desc=None):
    """Fungsi persamaan dasar dan propertis untuk region 1"""

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
    props["cv"] = BIGR*(-1*(tau**2)*dgdtau2 + ((dgdpi-tau*dgdpidtau)**2)/dgdpi2)

    if desc and desc.lower() in props.keys():
        return props[desc.lower()]
    else:
        return None


#Region 2
def region2(p, t, desc=None):
    """Fungsi persamaan dasar dan propertis untuk region 2"""

    pi = p/1e3
    tau = 540/t
    _Jo = IJnReg2["Jo"]
    _no = IJnReg2["no"]
    _I = IJnReg2["I"]
    _J = IJnReg2["J"]
    _n = IJnReg2["n"]

    go = np.log(pi)
    dgodpi = 1./pi
    # dgodpi2 = -1./(pi**2)
    dgodtau = 0.
    dgodtau2 = 0.
    # dgodpidtau = 0.

    for Jio, nio in zip(_Jo, _no):
        go += nio*(tau**Jio)
        dgodtau += nio*Jio*(tau**(Jio-1))
        dgodtau2 += nio*Jio*(Jio-1)*(tau**(Jio-2))

    gr = 0.
    dgrdpi = 0.
    dgrdpi2 = 0.
    dgrdtau = 0.
    dgrdtau2 = 0.
    dgrdpidtau = 0.

    for Ii, Ji, ni in zip(_I, _J, _n):
        gr += ni*(pi**Ii)*((tau-0.5)**Ji)
        dgrdpi += ni*Ii*(pi**(Ii-1))*((tau-0.5)**Ji)
        dgrdpi2 += ni*Ii*(Ii-1)*(pi**(Ii-2))*((tau-0.5)**Ji)
        dgrdtau += ni*Ji*(pi**Ii)*((tau-0.5)**(Ji-1))
        dgrdtau2 += ni*Ji*(Ji-1)*(pi**Ii)*((tau-0.5)**(Ji-2))
        dgrdpidtau += ni*Ii*Ji*(pi**(Ii-1))*((tau-0.5)**(Ji-1))

    props = dict()
    props["v"] = BIGR*t*pi*(dgodpi+dgrdpi)/p
    props["u"] = BIGR*t*(tau*(dgodtau+dgrdtau)-pi*(dgodpi+dgrdpi))
    props["s"] = BIGR*(tau*(dgodtau+dgrdtau)-(go+gr))
    props["h"] = BIGR*t*tau*(dgodtau+dgrdtau)
    props["cp"] = -1*BIGR*(tau**2)*(dgodtau2+dgrdtau2)
    props["cv"] = BIGR*(-1*(tau**2)*(dgodtau2+dgrdtau2)-(((1+pi*dgrdpi-tau*pi*dgrdpidtau)**2)/(1-(pi**2)*dgrdpi2)))

    if desc and desc.lower() in props.keys():
        return props[desc.lower()]
    else:
        return None


#Supplementary equations of region 2
def supp_region2(p, t, desc=None):
    """Fungsi persamaan tambahan untuk region 2"""

    pi = p/1e3
    tau = 540/t

    _Jo = IJnReg2Supp["Jo"]
    _no = IJnReg2Supp["no"]

    go = np.log(pi)
    dgodpi = 1./pi
    # dgodpi2 = -1./(pi**2)
    dgodtau = 0.
    dgodtau2 = 0.
    # dgodpidtau = 0.

    for Jio, nio in zip(_Jo, _no):
        go += nio*(tau**Jio)
        dgodtau += nio*Jio*(tau**(Jio-1))
        dgodtau2 += nio*Jio*(Jio-1)*(tau**(Jio-2))

    _I = IJnReg2Supp["I"]
    _J = IJnReg2Supp["J"]
    _n = IJnReg2Supp["n"]

    gr = 0.
    dgrdpi = 0.
    dgrdpi2 = 0.
    dgrdtau = 0.
    dgrdtau2 = 0.
    dgrdpidtau = 0.

    for Ii, Ji, ni in zip(_I, _J, _n):
        gr += ni*(pi**Ii)*((tau-0.5)**Ji)
        dgrdpi += ni*Ii*(pi**(Ii-1))*((tau-0.5)**Ji)
        dgrdpi2 += ni*Ii*(Ii-1)*(pi**(Ii-2))*((tau-0.5)**Ji)
        dgrdtau += ni*Ji*(pi**Ii)*((tau-0.5)**(Ji-1))
        dgrdtau2 += ni*Ji*(Ji-1)*(pi**Ii)*((tau-0.5)**(Ji-2))
        dgrdpidtau += ni*Ii*Ji*(pi**(Ii-1))*((tau-0.5)**(Ji-1))

    props = dict()
    props["v"] = BIGR*t*pi*(dgodpi+dgrdpi)/p
    props["u"] = BIGR*t*(tau*(dgodtau+dgrdtau)-pi*(dgodpi+dgrdpi))
    props["s"] = BIGR*(tau*(dgodtau+dgrdtau)-(go+gr))
    props["h"] = BIGR*t*tau*(dgodtau+dgrdtau)
    props["cp"] = -1*BIGR*(tau**2)*(dgodtau2+dgrdtau2)
    props["cv"] = BIGR*(-1*(tau**2)*(dgodtau2+dgrdtau2)-(((1+pi*dgrdpi-tau*pi*dgrdpidtau)**2)/(1-(pi**2)*dgrdpi2)))

    if desc and desc.lower() in props.keys():
        return props[desc.lower()]
    else:
        return None


#Region 3
def _phi(delta, tau):
    """Fungsi persamaan dasar untuk region 3"""

    _n = IJnReg3["n"]
    _I = IJnReg3["I"]
    _J = IJnReg3["J"]

    f = _n[0]*np.log(delta)
    dfddel = _n[0]/delta
    dfddel2 = (-1*_n[0])/(delta**2)
    dfdtau = 0.
    dfdtau2 = 0.
    dfddeldtau = 0.

    for Ii, Ji, ni in zip(_I[1:], _J[1:], _n[1:]):
        f += ni*(delta**Ii)*(tau**Ji)
        dfddel += ni*Ii*(delta**(Ii-1))*(tau**Ji)
        dfddel2 += ni*Ii*(Ii-1)*(delta**(Ii-2))*(tau**Ji)
        dfdtau += ni*Ji*(delta**Ii)*(tau**(Ji-1))
        dfdtau2 += ni*Ji*(Ji-1)*(delta**Ii)*(tau**(Ji-2))
        dfddeldtau += ni*Ii*Ji*(delta**(Ii-1))*(tau**(Ji-1))

    return f, dfddel, dfddel2, dfdtau, dfdtau2, dfddeldtau


def saturRhoReg3(psat, tsat):
    """Fungsi untuk mencari rho pada fase saturasi"""

    tau = TEMPC/tsat
    c = psat/(RHOC*BIGR*tsat)

    def func(delta):

        f, dfddel, dfddel2, dfdtau, dfdtau2, dfddeldtau = _phi(delta=delta, tau=tau)
        f1 = (delta**2)*dfddel-c
        return f1

    def dfunc(delta):

        f, dfddel, dfddel2, dfdtau, dfdtau2, dfddeldtau = _phi(delta=delta, tau=tau)
        f1 = 2*delta*dfddel+(delta**2)*dfddel2
        return f1

    delL = delV = 1.

    if tsat <= 647:
        delL = optimize.newton(func, x0=1.7, fprime=dfunc, tol=1e-9)
        delV = optimize.newton(func, x0=0.4, fprime=dfunc, tol=1e-9)
    elif 647 < tsat < TEMPC:
        delL = optimize.newton(func, x0=0.999999999, fprime=dfunc, tol=1e-9)
        delV = optimize.newton(func, x0=0.999999999, fprime=dfunc, tol=1e-9)

    return delL*RHOC, delV*RHOC


def region3(rho, t, desc):
    """Fungsi untuk mencari propertis untuk region 3"""

    delta = rho/RHOC
    tau = TEMPC/t

    f, dfddel, dfddel2, dfdtau, dfdtau2, dfddeldtau = _phi(delta=delta, tau=tau)

    props = dict()
    props["p"] = rho*BIGR*t*delta*dfddel
    props["u"] = BIGR*t*tau*dfdtau
    props["s"] = BIGR*(tau*dfdtau-f)
    props["h"] = BIGR*t*(tau*dfdtau+delta*dfddel)

    if not (647 <= t < TEMPC):
        props["cv"] = -1*BIGR*(tau**2)*dfdtau2
        sub = ((delta*dfddel-delta*tau*dfddeldtau)**2)/(2*delta*dfddel+(delta**2)*dfddel2)
        props["cp"] = BIGR*(-1*(tau**2)*dfdtau2+sub)
    else:
        props["cv"] = None
        props["cp"] = None

    if desc and desc.lower() in props.keys():
        return props[desc.lower()]
    else:
        return None


#Region 4
def region4(psat=None, tsat=None):
    """Fungsi untuk mencari suhu dan tekanan pada titik saturasi"""

    n = nReg4["n"]

    if tsat and psat is None:
        nu = (tsat/1)+(n[8]/((tsat/1)-n[9]))
        Ai = (nu**2)+n[0]*nu+n[1]
        Bi = n[2]*(nu**2)+n[3]*nu+n[4]
        Ci = n[5]*(nu**2)+n[6]*nu+n[7]
        ans = 1e3*((2*Ci/(-Bi + np.sqrt(Bi**2 - 4*Ai*Ci)))**4)
        return ans
    elif psat and tsat is None:
        beta = (psat/1000)**(1/4)
        Ei = (beta**2)+n[2]*beta+n[5]
        Fi = n[0]*(beta**2)+n[3]*beta+n[6]
        Gi = n[1]*(beta**2)+n[4]*beta+n[7]
        Di = 2*Gi/(-Fi - np.sqrt((Fi**2) - 4*Ei*Gi))
        ans = 1*((n[9]+Di-np.sqrt((n[9]+Di)**2-4*(n[8]+n[9]*Di)))/2)
        return ans


#Region 5
def region5(p, t, desc=None):
    """Fungsi untuk persamaan dasar dan propertis untuk region 5"""

    pi = p/1e3
    tau = 1000/t

    _Jo = IJnReg5["Jo"]
    _no = IJnReg5["no"]
    _I = IJnReg5["I"]
    _J = IJnReg5["J"]
    _n = IJnReg5["n"]

    go = np.log(pi)
    dgodpi = 1./pi
    # dgodpi2 = -1./(pi**2)
    dgodtau = 0.
    dgodtau2 = 0.
    # dgodpidtau = 0.

    for Jio, nio in zip(_Jo, _no):
        go += nio*(tau**Jio)
        dgodtau += nio*Jio*(tau**(Jio-1))
        dgodtau2 += nio*Jio*(Jio-1)*(tau**(Jio-2))

    gr = 0.
    dgrdpi = 0.
    dgrdpi2 = 0.
    dgrdtau = 0.
    dgrdtau2 = 0.
    dgrdpidtau = 0.

    for Ii, Ji, ni in zip(_I, _J, _n):
        gr += ni*(pi**Ii)*(tau**Ji)
        dgrdpi += ni*Ii*(pi**(Ii-1))*(tau**Ji)
        dgrdpi2 += ni*Ii*(Ii-1)*(pi**(Ii-2))*(tau**Ji)
        dgrdtau += ni*Ji*(pi**Ii)*(tau**(Ji-1))
        dgrdtau2 += ni*Ji*(Ji-1)*(pi**Ii)*(tau**(Ji-2))
        dgrdpidtau += ni*Ii*Ji*(pi**(Ii-1))*(tau**(Ji-1))

    props = dict()
    props["v"] = (BIGR*t*pi*(dgrdpi+dgodpi))/p
    props["u"] = BIGR*t*(tau*(dgodtau+dgrdtau)-pi*(dgodpi+dgrdpi))
    props["s"] = BIGR*(tau*(dgodtau+dgrdtau)-(go+gr))
    props["h"] = BIGR*t*tau*(dgodtau+dgrdtau)
    props["cp"] = -1*BIGR*(tau**2)*(dgodtau2+dgrdtau2)
    props["cv"] = BIGR*(-1*(tau**2)*(dgodtau2+dgrdtau2)-(((1+pi*dgrdpi-tau*pi*dgrdpidtau)**2)/(1-(pi**2)*dgrdpi2)))

    if desc and desc.lower() in props.keys():
        return props[desc.lower()]
    else:
        return None