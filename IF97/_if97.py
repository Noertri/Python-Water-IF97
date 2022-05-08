import math
from .cores.backwardPT import Region3VPT
from .cores.basic import region1, region2, supp_region2, Region3, Region4, region5
from .cores.boundary import Boundary23
from .constants import PRESSC, RHOC, TEMPC


def saturationT(tsat):
    """Calculate properties at saturation line using saturation temperature as input

    Parameters
    ----------
    tsat: float
       saturation temperature (K)

    Returns
    -------
    psat: float
        saturation pressure (KPa)
    tsat: float
        saturation temperature (K)
    v: float
        specific volume of liquid and vapor phase (m^3/Kg)
    u: float
        specific internal energy of liquid and vapor phase (KJ/Kg)
    h: float
        specific enthalpy of liquid and vapor phase (KJ/Kg)
    s: float
        specific entropy of liquid and vapor phase (KJ/Kg*K)
    cp: float or inf
        specific isobaric heat capacity of liquid and vapor phase (KJ/Kg*K),
        return inf when tsat near critical temperature, because near critical temperature value of cp is not accurate
    cv: float or inf
        specific isohoric heat capacity of liquid and vapor phase (KJ/Kg*K),
        return inf when tsat near critical temperature, because near critical temperature value of cv is not accurate
    """

    psat = 0.
    if tsat and (psat := Region4.getSaturPress(tsat=tsat)) and 273.15 <= tsat <= 623.15 and 0. < psat < PRESSC:
        props = {
            "psat": psat,
            "tsat": tsat,
            "v": [region1(p=psat, t=tsat, desc="v"), region2(p=psat, t=tsat, desc="v")],
            "u": [region1(p=psat, t=tsat, desc="u"), region2(p=psat, t=tsat, desc="u")],
            "h": [region1(p=psat, t=tsat, desc="h"), region2(p=psat, t=tsat, desc="h")],
            "s": [region1(p=psat, t=tsat, desc="s"), region2(p=psat, t=tsat, desc="s")],
            "cv": [region1(p=psat, t=tsat, desc="cv"), region2(p=psat, t=tsat, desc="cv")],
            "cp": [region1(p=psat, t=tsat, desc="cp"), region2(p=psat, t=tsat, desc="cp")]
        }
        return props
    elif tsat and (psat := Region4.getSaturPress(tsat=tsat)) and 623.15 < tsat < TEMPC and 0. < psat < PRESSC:
        rhof, rhog = Region3.saturRho(psat, tsat)
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhof, 1/rhog],
                "u": [Region3.region3(rho=rhof, t=tsat, desc="u"), Region3.region3(rho=rhog, t=tsat, desc="u")],
                "h": [Region3.region3(rho=rhof, t=tsat, desc="h"), Region3.region3(rho=rhog, t=tsat, desc="h")],
                "s": [Region3.region3(rho=rhof, t=tsat, desc="s"), Region3.region3(rho=rhog, t=tsat, desc="s")],
                "cv": [Region3.region3(rho=rhof, t=tsat, desc="cv"), Region3.region3(rho=rhog, t=tsat, desc="cv")],
                "cp": [Region3.region3(rho=rhof, t=tsat, desc="cp"), Region3.region3(rho=rhog, t=tsat, desc="cp")]
        }
        return props
    elif tsat and tsat == TEMPC:
        props = {
                "psat": PRESSC,
                "tsat": tsat,
                "v": [1/RHOC, 1/RHOC],
                "u": [Region3.region3(rho=RHOC, t=tsat, desc="u"), Region3.region3(rho=RHOC, t=tsat, desc="u")],
                "h": [Region3.region3(rho=RHOC, t=tsat, desc="h"), Region3.region3(rho=RHOC, t=tsat, desc="h")],
                "s": [Region3.region3(rho=RHOC, t=tsat, desc="s"), Region3.region3(rho=RHOC, t=tsat, desc="s")],
                "cv": [math.inf, math.inf],
                "cp": [math.inf, math.inf]
        }
        return props


def saturationP(psat):
    """Calculate properties at saturation line using saturation pressure as input

    Parameters
    ----------
    psat: float
       saturation pressure (KPa)

    Returns
    -------
    psat: float
        saturation pressure (KPa)
    tsat: float
        saturation temperature (K)
    v: float
        specific volume of liquid and vapor phase (m^3/Kg)
    u: float
        specific internal energy of liquid and vapor phase (KJ/Kg)
    h: float
        specific enthalpy of liquid and vapor phase (KJ/Kg)
    s: float
        specific entropy of liquid and vapor phase (KJ/Kg*K)
    cp: float or inf
        specific isobaric heat capacity of liquid and vapor phase (KJ/Kg*K),
        return inf when psat near critical temperature, because near critical temperature value of cp is not accurate
    cv: float or inf
        specific isohoric heat capacity of liquid and vapor phase (KJ/Kg*K),
        return inf when psat near critical temperature, because near critical temperature value of cv is not accurate
    """

    tsat = 0.
    if psat and (tsat := Region4.getSaturTemp(psat=psat)) and 0.6112127 <= psat <= 16529.2 and 273.15 <= tsat < TEMPC:
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [region1(p=psat, t=tsat, desc="v"), region2(p=psat, t=tsat, desc="v")],
                "u": [region1(p=psat, t=tsat, desc="u"), region2(p=psat, t=tsat, desc="u")],
                "h": [region1(p=psat, t=tsat, desc="h"), region2(p=psat, t=tsat, desc="h")],
                "s": [region1(p=psat, t=tsat, desc="s"), region2(p=psat, t=tsat, desc="s")],
                "cv": [region1(p=psat, t=tsat, desc="cv"), region2(p=psat, t=tsat, desc="cv")],
                "cp": [region1(p=psat, t=tsat, desc="cp"), region2(p=psat, t=tsat, desc="cp")]
        }
        return props
    elif psat and (tsat := Region4.getSaturTemp(psat=psat)) and 16529.2 < psat < PRESSC and 273.15 <= tsat < TEMPC:
        rhof, rhog = Region3.saturRho(psat, tsat)
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhof, 1/rhog],
                "u": [Region3.region3(rho=rhof, t=tsat, desc="u"), Region3.region3(rho=rhog, t=tsat, desc="u")],
                "h": [Region3.region3(rho=rhof, t=tsat, desc="h"), Region3.region3(rho=rhog, t=tsat, desc="h")],
                "s": [Region3.region3(rho=rhof, t=tsat, desc="s"), Region3.region3(rho=rhog, t=tsat, desc="s")],
                "cv": [Region3.region3(rho=rhof, t=tsat, desc="cv"), Region3.region3(rho=rhog, t=tsat, desc="cv")],
                "cp": [Region3.region3(rho=rhof, t=tsat, desc="cp"), Region3.region3(rho=rhog, t=tsat, desc="cp")]
        }
        return props
    elif psat and psat == PRESSC:
        props = {
                "psat": psat,
                "tsat": TEMPC,
                "v": [1/RHOC, 1/RHOC],
                "u": [Region3.region3(rho=RHOC, t=TEMPC, desc="u"), Region3.region3(rho=RHOC, t=TEMPC, desc="u")],
                "h": [Region3.region3(rho=RHOC, t=TEMPC, desc="h"), Region3.region3(rho=RHOC, t=TEMPC, desc="h")],
                "s": [Region3.region3(rho=RHOC, t=TEMPC, desc="s"), Region3.region3(rho=RHOC, t=TEMPC, desc="s")],
                "cv": [math.inf, math.inf],
                "cp": [math.inf, math.inf]
        }
        return props


def singlephase(p, t):
    """Calculate properties at single phase

    Parameters
    ----------
    p: float
        pressure (KPa)
    t: float
        temperature (K)

    Returns
    -------
    v: float
        specific volume (m^3/Kg)
    u: float
        specific internal energy (KJ/Kg)
    h: float
        specific enthalpy (KJ/Kg)
    s: float
        specific entropy (KJ/Kg*K)
    cp: float
        specific isobaric heat capacity (KJ/Kg*K)
    cv: float
        specific isochoric heat capacity (KJ/Kg*K)
    """

    t23 = 0.
    if 0 < p < (psat := Region4.getSaturPress(tsat=t)) and 273.15 <= t <= 623.15:
        props = {
                "v": region2(p, t, desc="v"),
                "u": region2(p, t, desc="u"),
                "h": region2(p, t, desc="h"),
                "s": region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp")
        }
        return props
    elif (psat := Region4.getSaturPress(tsat=t)) <= p <= 1e5 and 273.15 <= t <= 623.15:
        props = {
                "v": region1(p, t, desc="v"),
                "u": region1(p, t, desc="u"),
                "h": region1(p, t, desc="h"),
                "s": region1(p, t, desc="s"),
                "cv": region1(p, t, desc="cv"),
                "cp": region1(p, t, desc="cp")
        }
        return props
    elif (p23 := Boundary23.getPress(t)) and 0 < p <= p23 and 623.15 < t <= 863.15:
        props = {
                "v": region2(p, t, desc="v"),
                "u": region2(p, t, desc="u"),
                "h": region2(p, t, desc="h"),
                "s": region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp")
        }
        return props
    elif (p23 := Boundary23.getPress(t)) and (t23 := Boundary23.getTemp(p)) and p23 < p <= 1e5 and 623.15 < t <= t23:
        rho = Region3VPT.singleRho(p, t)
        props = {
                "v": 1/rho,
                "u": Region3.region3(rho, t, desc="u"),
                "h": Region3.region3(rho, t, desc="h"),
                "s": Region3.region3(rho, t, desc="s"),
                "cv": Region3.region3(rho, t, desc="cv"),
                "cp": Region3.region3(rho, t, desc="cp")
        }
        return props
    elif 0 < p <= 1e5 and 863.15 < t <= 1073.15:
        props = {
                "v": region2(p, t, desc="v"),
                "u": region2(p, t, desc="u"),
                "h": region2(p, t, desc="h"),
                "s": region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp")
        }
        return props
    elif 0 < p <= 5e4 and 1073.15 < t <= 2273.15:
        props = {
                "v": region5(p, t, desc="v"),
                "u": region5(p, t, desc="u"),
                "h": region5(p, t, desc="h"),
                "s": region5(p, t, desc="s"),
                "cv": region5(p, t, desc="cv"),
                "cp": region5(p, t, desc="cp")
        }
        return props


def if97(p=None, t=None, x=None):
    """Implementation of IAPWS-IF97 to calculate ordinary/pure water properties at mixed and single phase

    Range of validity
    -----------------
    Mixed phase
        273.15 K <= t <= 647.096 K or 0 C <= t <= 373.946 C and

        0.6112127 KPa <= p <= 22064 KPa and

        0 <= x <= 1
    Single phase
        273.15 K <= t <= 1073 K or 0 C <= t <= 800 C for 0 < p <= 100 MPa or 0 < p <= 100000 KPa,

        1073.15 K <= t <= 2273 K or 800 C <= t <= 2000 C for 0 < p <= 50 MPa or 0 < p <= 50000 KPa

    Parameters
    ----------
    p: float or None
        pressure (KPa)
    t: float or None
        temperature (K)
    x: float or None
        quality of vapor

    Returns
    -------
    v: float
        specific volume (m^3/Kg)
    u: float
        specific internal energy (KJ/Kg)
    h: float
        specific enthalpy (KJ/Kg)
    s: float
        specific entropy (KJ/Kg*K)
    cp: float or inf
        specific isobaric heat capacity (KJ/Kg*K),
        return inf when t near critical temperature, because near critical temperature value of cp is not accurate
    cv: float or inf
        specific isohoric heat capacity (KJ/Kg*K),
        return inf when t near critical temperature, because near critical temperature value of cv is not accurate

    Raises
    ------
    ValueError
        when value of inputs exceed or not in range of validity.
    """

    ans = dict()
    if (not p) and t and (x is not None) and 273.15 <= t <= TEMPC and 0. <= x <= 1. and (props := saturationT(tsat=t)) is not None:

        v = props["v"]
        u = props["u"]
        h = props["h"]
        s = props["s"]
        cp = props["cp"]
        cv = props["cv"]

        ans["psat"] = props["psat"]
        ans["tsat"] = props["tsat"]
        ans["v"] = v[0] + x*(v[1]-v[0])
        ans["u"] = u[0] + x*(u[1]-u[0])
        ans["s"] = s[0] + x*(s[1]-s[0])
        ans["h"] = h[0] + x*(h[1]-h[0])
        if all(math.isfinite(_) for _ in cp) and all(math.isfinite(_) for _ in cv):
            ans["cp"] = cp[0] + x*(cp[1]-cp[0])
            ans["cv"] = cv[0] + x*(cv[1]-cv[0])
        else:
            ans["cp"] = math.inf
            ans["cv"] = math.inf
        return ans
    elif p and (not t) and (x is not None) and 0.6112127 <= p <= PRESSC and 0. <= x <= 1. and (props := saturationP(psat=p)) is not None:

        v = props["v"]
        u = props["u"]
        h = props["h"]
        s = props["s"]
        cp = props["cp"]
        cv = props["cv"]

        ans["psat"] = props["psat"]
        ans["tsat"] = props["tsat"]
        ans["v"] = v[0]+x*(v[1]-v[0])
        ans["u"] = u[0]+x*(u[1]-u[0])
        ans["s"] = s[0]+x*(s[1]-s[0])
        ans["h"] = h[0]+x*(h[1]-h[0])
        if all(math.isfinite(_) for _ in cp) and all(math.isfinite(_) for _ in cv):
            ans["cp"] = cp[0] + x*(cp[1]-cp[0])
            ans["cv"] = cv[0] + x*(cv[1]-cv[0])
        else:
            ans["cp"] = math.inf
            ans["cv"] = math.inf
        return ans
    elif p and t and (not x) and 0 < p <= 1e5 and 273.15 <= t <= 2273.15 and (props := singlephase(p, t)) is not None:
        return props
    elif (x is not None) and (x < 0 or x > 1):
        raise ValueError(f"Quality(x) value exceed or not in range of validity")
    elif (p is None) and (t is not None) and (t < 273.15 or t > TEMPC):
        raise ValueError(f"Saturation temperature(t) value exceed or not in range of validity")
    elif (t is None) and (p is not None) and (p < 0.6112127 or p > PRESSC):
        raise ValueError(f"Saturation pressure(p) value exceed or not in range")
    elif (p <= 0 or p > 1e5) or (t < 273.15 or t > 2273.15) and x is None:
        raise ValueError(f"Temperature(t) or pressure(p) value exceed or not in range of validity")
