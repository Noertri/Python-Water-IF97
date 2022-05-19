"""This module contains all basic and property equations for region 1 to region 5"""

import numpy as np
from scipy import optimize
from ..coefficients import *
from ..constants import *


#Region 1
class Region1:
    """Class for region 1.

    Static Methods
    --------------
    _gamma(pi, tau)
        Basic equations for region 1.

    Class Methods
    -------------
    props(cls, p, t, desc)
        Equations of property for region 1.
    """

    @staticmethod
    def _gamma(pi, tau):
        """Basic equations for region 1.

        Parameters
        ----------
        pi: float
            pi = p/16.5e3.
        tau: float
            tau = 1386/t.

        Returns
        -------
        g: float
            specific Gibbs free energy.
        dgdpi: float
            first partial derivative of g to pi.
        d2gdpi2: float
            second partial derivative of g to pi.
        dgdtau: float
            first partial derivative of g to tau.
        d2gdtau2: float
            second partial derivative of g to tau.
        d2gdpidtau: float
            partial derivative of g to pi and tau.
        """

        #coefficients
        _I = IJnReg1["I"]
        _J = IJnReg1["J"]
        _n = IJnReg1["n"]

        g = 0.
        dgdpi = 0.
        d2gdpi2 = 0.
        dgdtau = 0.
        d2gdtau2 = 0.
        d2gdpidtau = 0.

        for Ii, Ji, ni in zip(_I, _J, _n):
            g += ni*((7.1-pi)**Ii)*((tau-1.222)**Ji)
            dgdpi += -ni*Ii*((7.1-pi)**(Ii-1))*((tau-1.222)**Ji)
            d2gdpi2 += ni*Ii*(Ii-1)*((7.1-pi)**(Ii-2))*((tau-1.222)**Ji)
            dgdtau += ni*Ji*((7.1-pi)**Ii)*((tau-1.222)**(Ji-1))
            d2gdtau2 += ni*Ji*(Ji-1)*((7.1-pi)**Ii)*((tau-1.222)**(Ji-2))
            d2gdpidtau += -ni*Ii*Ji*((7.1-pi)**(Ii-1))*((tau-1.222)**(Ji-1))

        return g, dgdpi, d2gdpi2, dgdtau, d2gdtau2, d2gdpidtau

    @classmethod
    def props(cls, p, t, desc):
        """Equations of property for region 1.

        Available Properties
        --------------------
        v: float
            specific volume (Kg/m^3).
        u: float
            specific internal energy (KJ/Kg).
        h: float
            specific enthalpy (KJ/Kg).
        s: float
            specific entropy (KJ/Kg*K).
        cp: float
            specific isobaric heat capacity (KJ/Kg*K).
        cv: float
            specific isochoric heat capacity (KJ/Kg*K).

        Parameters
        ----------
        p: float
            pressure (KPa).
        t: float
            temperature (K).
        desc: str
            property to return, one of v, u, h, s, cp, and cv.

        Returns
        -------
        _props: dict or None
            return one of available properties, if the property is not available return None instead, see Available Properties.
        """

        pi = p/16.53e3
        tau = 1386/t

        g, dgdpi, d2gdpi2, dgdtau, d2gdtau2, d2gdpidtau = cls._gamma(pi=pi, tau=tau)

        _props = dict()
        _props["v"] = BIGR*t*pi*dgdpi/p
        _props["u"] = BIGR*t*(tau*dgdtau-pi*dgdpi)
        _props["s"] = BIGR*(tau*dgdtau-g)
        _props["h"] = BIGR*t*tau*dgdtau
        _props["cp"] = -1*BIGR*(tau**2)*d2gdtau2
        _props["cv"] = BIGR*(-1*(tau**2)*d2gdtau2+((dgdpi-tau*d2gdpidtau)**2)/d2gdpi2)

        if desc and desc.lower() in _props.keys():
            return _props[desc.lower()]
        else:
            return None


#Region 2
class Region2:
    """Class for region 2.

    Static Methods
    --------------
    _gammao(pi, tau)
        Ideal part of basic equations for region 2.
    _gammar(pi, tau)
        Residual part of basic equations for region 2.

    Class Methods
    -------------
    props(cls, p, t, desc)
        Equations of property for region 2.
    """

    @staticmethod
    def _gammao(pi, tau):
        """Ideal part of basic equations for region 2.

        Parameters
        ----------
        pi: float
            pi = p/1e3.
        tau: float
            tau = 540/t.

        Returns
        -------
        go: float
            specific Gibbs free energy.
        dgodpi: float
            first partial derivative of go to pi.
        d2godpi2: float
            second partial derivative of go to pi.
        dgodtau: float
            first partial derivative of go to tau.
        d2godtau2: float
            second partial derivative of go to tau.
        d2godpidtau: float
            partial derivative of go to pi and tau.
        """

        #coefficients
        _Jo = IJnReg2["Jo"]
        _no = IJnReg2["no"]

        go = np.log(pi)
        dgodpi = 1./pi
        d2godpi2 = -1./(pi**2)
        dgodtau = 0.
        d2godtau2 = 0.
        d2godpidtau = 0.

        for Jio, nio in zip(_Jo, _no):
            go += nio*(tau**Jio)
            dgodtau += nio*Jio*(tau**(Jio-1))
            d2godtau2 += nio*Jio*(Jio-1)*(tau**(Jio-2))

        return go, dgodpi, d2godpi2, dgodtau, d2godtau2, d2godpidtau

    @staticmethod
    def _gammar(pi, tau):
        """Residual part of basic equations for region 2.

        Parameters
        ----------
        pi: float
            pi = p/1e3.
        tau: float
            tau = 540/t.

        Returns
        -------
        gr: float
            specific Gibbs free energy.
        dgrdpi: float
            first partial derivative of gr to pi.
        d2grdpi2: float
            second partial derivative of gr to pi.
        dgrdtau: float
            first partial derivative of gr to tau.
        d2grdtau2: float
            second partial derivative of gr to tau.
        d2grdpidtau: float
            partial derivative of gr to pi and tau.
        """

        #coefficients
        _I = IJnReg2["I"]
        _J = IJnReg2["J"]
        _n = IJnReg2["n"]

        gr = 0.
        dgrdpi = 0.
        d2grdpi2 = 0.
        dgrdtau = 0.
        d2grdtau2 = 0.
        d2grdpidtau = 0.

        for Ii, Ji, ni in zip(_I, _J, _n):
            gr += ni*(pi**Ii)*((tau-0.5)**Ji)
            dgrdpi += ni*Ii*(pi**(Ii-1))*((tau-0.5)**Ji)
            d2grdpi2 += ni*Ii*(Ii-1)*(pi**(Ii-2))*((tau-0.5)**Ji)
            dgrdtau += ni*Ji*(pi**Ii)*((tau-0.5)**(Ji-1))
            d2grdtau2 += ni*Ji*(Ji-1)*(pi**Ii)*((tau-0.5)**(Ji-2))
            d2grdpidtau += ni*Ii*Ji*(pi**(Ii-1))*((tau-0.5)**(Ji-1))

        return gr, dgrdpi, d2grdpi2, dgrdtau, d2grdtau2, d2grdpidtau

    @classmethod
    def props(cls, p, t, desc):
        """Equations of property for region 2.

        Available Properties
        --------------------
        v: float
            specific volume (m^3/Kg).
        u: float
            specific internal energy (KJ/Kg).
        h: float
            specific enthalpy (KJ/Kg).
        s: float
            specific entropy (KJ/Kg*K).
        cp: float
            specific isobaric heat capacity (KJ/Kg*K).
        cv: float
            specific isochoric heat capacity (KJ/Kg*K).

        Parameters
        ----------
        p: float
            pressure (KPa).
        t: float
            temperature (K).
        desc: str
            property to return, one of v, u, h, s, cp, and cv.

        Returns
        -------
        _props : dict or None
            return one of available properties or if the property is not available return None instead, see Available Properties.
        """

        pi = p/1e3
        tau = 540/t

        go, dgodpi, d2godpi2, dgodtau, d2godtau2, d2godpidtau = cls._gammao(pi, tau)
        gr, dgrdpi, d2grdpi2, dgrdtau, d2grdtau2, d2grdpidtau = cls._gammar(pi, tau)

        _props = dict()
        _props["v"] = BIGR*t*pi*(dgodpi+dgrdpi)/p
        _props["u"] = BIGR*t*(tau*(dgodtau+dgrdtau)-pi*(dgodpi+dgrdpi))
        _props["s"] = BIGR*(tau*(dgodtau+dgrdtau)-(go+gr))
        _props["h"] = BIGR*t*tau*(dgodtau+dgrdtau)
        _props["cp"] = -1*BIGR*(tau**2)*(d2godtau2+d2grdtau2)
        _props["cv"] = BIGR*(-1*(tau**2)*(d2godtau2+d2grdtau2)-(((1+pi*dgrdpi-tau*pi*d2grdpidtau)**2)/(1-(pi**2)*d2grdpi2)))

        if desc and desc.lower() in _props.keys():
            return _props[desc.lower()]
        else:
            return None


#Supplementary equations of region 2
class SuppRegion2(Region2):
    """Class for supplementary equations of region 2, subclass of class Region2.

    Static Methods
    --------------
    _gammao(pi, tau)
        Ideal part of supplementary equations for region 2.
    _gammar(pi, tau)
        Residual part of supplementary equations for region 2.
    """

    @staticmethod
    def _gammao(pi, tau):
        """Ideal part of supplementary equations for region 2.

        Parameters
        ----------
        pi: float
            pi = p/1e3.
        tau: float
            tau = 540/t.

        Returns
        -------
        go: float
            specific Gibbs free energy.
        dgodpi: float
            first partial derivative of go to pi.
        d2godpi2: float
            second partial derivative of go to pi.
        dgodtau: float
            first partial derivative of go to tau.
        d2godtau2: float
            second partial derivative of go to tau.
        d2godpidtau: float
            partial derivative of go to pi and tau.
        """

        #coefficients
        _Jo = IJnReg2Supp["Jo"]
        _no = IJnReg2Supp["no"]

        go = np.log(pi)
        dgodpi = 1./pi
        d2godpi2 = -1./(pi**2)
        dgodtau = 0.
        d2godtau2 = 0.
        d2godpidtau = 0.

        for Jio, nio in zip(_Jo, _no):
            go += nio*(tau**Jio)
            dgodtau += nio*Jio*(tau**(Jio-1))
            d2godtau2 += nio*Jio*(Jio-1)*(tau**(Jio-2))

        return go, dgodpi, d2godpi2, dgodtau, d2godtau2, d2godpidtau

    @staticmethod
    def _gammar(pi, tau):
        """Residual part of supplementary equations for region 2.

        Parameters
        ----------
        pi: float
            pi = p/1e3.
        tau: float
            tau = 540/t.

        Returns
        -------
        gr: float
            specific Gibbs free energy.
        dgrdpi: float
            first partial derivative of gr to pi.
        d2grdpi2: float
            second partial derivative of gr to pi.
        dgrdtau: float
            first partial derivative of gr to tau.
        d2grdtau2: float
            second partial derivative of gr to tau.
        d2grdpidtau: float
            partial derivative of gr to pi and tau.
        """

        #coefficients
        _I = IJnReg2Supp["I"]
        _J = IJnReg2Supp["J"]
        _n = IJnReg2Supp["n"]

        gr = 0.
        dgrdpi = 0.
        d2grdpi2 = 0.
        dgrdtau = 0.
        d2grdtau2 = 0.
        d2grdpidtau = 0.

        for Ii, Ji, ni in zip(_I, _J, _n):
            gr += ni*(pi**Ii)*((tau-0.5)**Ji)
            dgrdpi += ni*Ii*(pi**(Ii-1))*((tau-0.5)**Ji)
            d2grdpi2 += ni*Ii*(Ii-1)*(pi**(Ii-2))*((tau-0.5)**Ji)
            dgrdtau += ni*Ji*(pi**Ii)*((tau-0.5)**(Ji-1))
            d2grdtau2 += ni*Ji*(Ji-1)*(pi**Ii)*((tau-0.5)**(Ji-2))
            d2grdpidtau += ni*Ii*Ji*(pi**(Ii-1))*((tau-0.5)**(Ji-1))

        return gr, dgrdpi, d2grdpi2, dgrdtau, d2grdtau2, d2grdpidtau


#Region 3
class Region3:
    """Class for region 3

    Static Methods
    --------------
    _phi(delta, tau)
        Basic equation for region 3

    Classs Methods
    --------------
    saturRho(cls, psat, tsat)
        Calculate saturation densities in region 3
    props(cls, rho, t, desc)
        Calculate properties in region 3
    _iterRho(cls, delta0, p, t)
        Backward equation to calculate density using iterative method
    """

    @staticmethod
    def _phi(delta, tau):
        """Basic equations for region 3.

        Parameters
        ----------
        delta: float
            delta = rho/RHOC.
        tau: float
            tau = TEMPC/t.

        Returns
        -------
        f: float
           specific Helmhotz free energy.
        dfddel: float
            first partial derivative of f to delta.
        d2fddel2: float
            second partial derivative of f to delta.
        dfdtau: float
            first partial derivative of f to tau.
        d2fdtau2: float
            second partial derivative of f to tau.
        dfddeldtau: float
            partial derivative of f to delta and tau.
        """

        #coefficients
        _n = IJnReg3["n"]
        _I = IJnReg3["I"]
        _J = IJnReg3["J"]

        f = _n[0]*np.log(delta)
        dfddel = _n[0]/delta
        d2fddel2 = (-1*_n[0])/(delta**2)
        dfdtau = 0.
        d2fdtau2 = 0.
        d2fddeldtau = 0.

        for Ii, Ji, ni in zip(_I[1:], _J[1:], _n[1:]):
            f += ni*(delta**Ii)*(tau**Ji)
            dfddel += ni*Ii*(delta**(Ii-1))*(tau**Ji)
            d2fddel2 += ni*Ii*(Ii-1)*(delta**(Ii-2))*(tau**Ji)
            dfdtau += ni*Ji*(delta**Ii)*(tau**(Ji-1))
            d2fdtau2 += ni*Ji*(Ji-1)*(delta**Ii)*(tau**(Ji-2))
            d2fddeldtau += ni*Ii*Ji*(delta**(Ii-1))*(tau**(Ji-1))

        return f, dfddel, d2fddel2, dfdtau, d2fdtau2, d2fddeldtau

    @classmethod
    def _iterRho(cls, delta0, p, t):
        """Backward equation using iterative method to calculate density using pressure and temperature as inputs.

        Parameters
        ----------
        delta0: float
            initial guess value of delta.
        p: float
            pressure (KPa).
        t: float
            temperature (K).

        Returns
        -------
        _rho: float
            density (Kg/m^3).
        """

        tau = TEMPC/t
        c = p/(RHOC*BIGR*t)

        def func(delta):
            baseq = cls._phi(delta=delta, tau=tau)
            f1 = (delta**2)*baseq[1]-c
            return f1

        def dfunc(delta):
            baseq = cls._phi(delta=delta, tau=tau)
            f1 = 2*delta*baseq[1]+(delta**2)*baseq[2]
            return f1

        _delta = optimize.newton(func, x0=delta0, fprime=dfunc, tol=1e-9)
        _rho = RHOC*_delta
        return _rho

    @classmethod
    def saturRho(cls, psat, tsat):
        """Calculate saturated liquid and vapor density for region 3.

        Parameters
        ----------
        psat: float
            saturation pressure (KPa).
        tsat: float
            saturation temperature (K).

        Returns
        -------
        rhof: float
            saturated liquid density (Kg/m^3).
        rhof: float
            saturated vapor density (Kg/m^3).
        """

        if 623.15 < tsat <= 647:
            rhof = cls._iterRho(1.7, psat, tsat)
            rhog = cls._iterRho(0.4, psat, tsat)
        elif 647 < tsat < TEMPC:
            rhof = cls._iterRho(0.999999999, psat, tsat)
            rhog = cls._iterRho(0.999999999, psat, tsat)

        return rhof, rhog

    @classmethod
    def props(cls, rho, t, desc):
        """Equations of property for region 3.

        Available Properties
        --------------------
        p: float
            pressure (KPa).
        u: float
            specific internal energy (KJ/Kg).
        h: float
            specific enthalpy (KJ/Kg).
        s: float
            specific entropy (KJ/Kg*K).
        cp: float
            specific isobaric heat capacity (KJ/Kg*K).
        cv: float
            specific isochoric heat capacity (KJ/Kg*K).

        Parameters
        ----------
        rho: float
            density (Kg/m^3).
        t: float
            temperature (K).
        desc: str
            property to return, one of p, u, h, s, cp, and cv.

        Returns
        -------
        _props: dict or None
            return one of available properties or if property is not available return None instead, see Available Properties.
        """

        delta = rho/RHOC
        tau = TEMPC/t

        f, dfddel, d2fddel2, dfdtau, d2fdtau2, d2fddeldtau = cls._phi(delta=delta, tau=tau)

        _props = dict()
        _props["p"] = rho*BIGR*t*delta*dfddel
        _props["u"] = BIGR*t*tau*dfdtau
        _props["s"] = BIGR*(tau*dfdtau-f)
        _props["h"] = BIGR*t*(tau*dfdtau+delta*dfddel)
        _props["cv"] = -1*BIGR*(tau**2)*d2fdtau2
        sub = ((delta*dfddel-delta*tau*d2fddeldtau)**2)/(2*delta*dfddel+(delta**2)*d2fddel2)
        _props["cp"] = BIGR*(-1*(tau**2)*d2fdtau2+sub)

        if desc and desc.lower() in _props.keys():
            return _props[desc.lower()]
        else:
            return None


#Region 4
class Region4:
    """Class for region 4.

    Class Methods
    -------------
    getSaturPress(cls, tsat)
        Method to calculate saturation pressure.
    getSaturTemp(cls, psat)
        Method to calculate saturation temperature.
    """

    @classmethod
    def getSaturPress(cls, tsat):
        """Calculate saturation pressure.

        Limit
        -----
        Valid for:
            273.15 K <= tsat <= 647.096 K or 0 C <= tsat <= 373.946 C.

        Parameters
        ----------
        tsat: float
            Saturation temperature (K).

        Returns
        -------
        psat: float
            return saturation pressure (KPa) or if saturation temperature (tsat) exceed
            and/or is not in range of limit return None instead, see Limit.
        """

        n = nReg4["n"]
        if 273.15 <= tsat <= TEMPC:
            nu = (tsat/1)+(n[8]/((tsat/1)-n[9]))
            Ai = (nu**2)+n[0]*nu+n[1]
            Bi = n[2]*(nu**2)+n[3]*nu+n[4]
            Ci = n[5]*(nu**2)+n[6]*nu+n[7]
            psat = 1e3*((2*Ci/(-Bi+np.sqrt(Bi**2-4*Ai*Ci)))**4)
            return psat
        else:
            return None

    @classmethod
    def getSaturTemp(cls, psat):
        """Calculate saturation pressure.

        Limit
        -----
        Valid for:
            0.6112127 KPa <= psat <= 22064 KPa or 0.6112127e-3 MPa <= psat <= 22.064 MPa

        Parameters
        ----------
        psat: float
            Saturation presssure (KPa).

        Returns
        -------
        tsat: float
            Saturation temperature (K) or if saturation pressure exceed and/or
            is not in range of limit return None instead, see Limit.
        """

        n = nReg4["n"]
        if cls.getSaturPress(tsat=273.15) <= psat <= PRESSC:
            beta = (psat/1000)**(1/4)
            Ei = (beta**2)+n[2]*beta+n[5]
            Fi = n[0]*(beta**2)+n[3]*beta+n[6]
            Gi = n[1]*(beta**2)+n[4]*beta+n[7]
            Di = 2*Gi/(-Fi - np.sqrt((Fi**2) - 4*Ei*Gi))
            tsat = 1*((n[9]+Di-np.sqrt((n[9]+Di)**2-4*(n[8]+n[9]*Di)))/2)
            return tsat
        else:
            return None


#Region 5
class Region5:
    """Class for region 5.

    Static Methods
    --------------
    _gammao(pi, tau)
        Ideal part of basic equations for region 5.
    _gammar(pi, tau)
        Residual part of basic equations for region 5.

    Class Methods
    -------------
    props(cls, p, t, desc)
        Equations of property for region 5.
    """

    @staticmethod
    def _gammao(pi, tau):
        """Ideal part of basic equations for region 5.

        Parameters
        ----------
        pi: float
            pi = p/1e3.
        tau: float
            tau = 1000/t.

        Returns
        -------
        go: float
            specific Gibbs free energy.
        dgodpi: float
            first partial derivative of go to pi.
        d2godpi2: float
            second partial derivative of go to pi.
        dgodtau: float
            first partial derivative of go to tau.
        d2godtau2: float
            second partial derivative of go to tau.
        d2godpidtau: float
            partial derivative of go to pi and tau.
        """

        #coefficients
        _Jo = IJnReg5["Jo"]
        _no = IJnReg5["no"]

        go = np.log(pi)
        dgodpi = 1./pi
        d2godpi2 = -1./(pi**2)
        dgodtau = 0.
        d2godtau2 = 0.
        d2godpidtau = 0.

        for Jio, nio in zip(_Jo, _no):
            go += nio*(tau**Jio)
            dgodtau += nio*Jio*(tau**(Jio-1))
            d2godtau2 += nio*Jio*(Jio-1)*(tau**(Jio-2))

        return go, dgodpi, d2godpi2, dgodtau, d2godtau2, d2godpidtau

    @staticmethod
    def _gammar(pi, tau):
        """Residual part of basic equations for region 5.

        Parameters
        ----------
        pi: float
            pi = p/1e3.
        tau: float
            tau = 1000/t.

        Returns
        -------
        gr: float
            specific Gibbs free energy.
        dgrdpi: float
            first partial derivative of gr to pi.
        d2grdpi2: float
            second partial derivative of gr to pi.
        dgrdtau: float
            first partial derivative of gr to tau.
        d2grdtau2: float
            second partial derivative of gr to tau.
        d2grdpidtau: float
            partial derivative of gr to pi and tau.
        """

        #coefficients
        _I = IJnReg5["I"]
        _J = IJnReg5["J"]
        _n = IJnReg5["n"]

        gr = 0.
        dgrdpi = 0.
        d2grdpi2 = 0.
        dgrdtau = 0.
        d2grdtau2 = 0.
        d2grdpidtau = 0.

        for Ii, Ji, ni in zip(_I, _J, _n):
            gr += ni*(pi**Ii)*(tau**Ji)
            dgrdpi += ni*Ii*(pi**(Ii-1))*(tau**Ji)
            d2grdpi2 += ni*Ii*(Ii-1)*(pi**(Ii-2))*(tau**Ji)
            dgrdtau += ni*Ji*(pi**Ii)*(tau**(Ji-1))
            d2grdtau2 += ni*Ji*(Ji-1)*(pi**Ii)*(tau**(Ji-2))
            d2grdpidtau += ni*Ii*Ji*(pi**(Ii-1))*(tau**(Ji-1))

        return gr, dgrdpi, d2grdpi2, dgrdtau, d2grdtau2, d2grdpidtau

    @classmethod
    def props(cls, p, t, desc):
        """Equations of property for region 5

        Available Properties
        --------------------
        v: float
            specific volume (m^3/Kg).
        u: float
            specific internal energy (KJ/Kg).
        h: float
            specific enthalpy (KJ/Kg).
        s: float
            specific entropy (KJ/Kg*K).
        cp: float
            specific isobaric heat capacity (KJ/Kg*K).
        cv: float
            specific isochoric heat capacity (KJ/Kg*K).

        Parameters
        ----------
        p: float
            pressure (KPa).
        t: float
            temperature (K).
        desc: str
            property to return, one of v, u, h, s, cp, and cv.

        Returns
        -------
        _props: dict or None
            return one of available properties or if property is not available return None instead, see Available Properties.
        """

        pi = p/1e3
        tau = 1000/t

        go, dgodpi, d2godpi2, dgodtau, d2godtau2, d2godpidtau = cls._gammao(pi, tau)
        gr, dgrdpi, d2grdpi2, dgrdtau, d2grdtau2, d2grdpidtau = cls._gammar(pi, tau)

        _props = dict()
        _props["v"] = (BIGR*t*pi*(dgrdpi+dgodpi))/p
        _props["u"] = BIGR*t*(tau*(dgodtau+dgrdtau)-pi*(dgodpi+dgrdpi))
        _props["s"] = BIGR*(tau*(dgodtau+dgrdtau)-(go+gr))
        _props["h"] = BIGR*t*tau*(dgodtau+dgrdtau)
        _props["cp"] = -1*BIGR*(tau**2)*(d2godtau2+d2grdtau2)
        _props["cv"] = BIGR*(-1*(tau**2)*(d2godtau2+d2grdtau2)-(((1+pi*dgrdpi-tau*pi*d2grdpidtau)**2)/(1-(pi**2)*d2grdpi2)))

        if desc and desc.lower() in _props.keys():
            return _props[desc.lower()]
        else:
            return None