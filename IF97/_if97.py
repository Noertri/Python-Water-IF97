import math
from .cores.backwardPT import Region3VPT
from .cores.basic import Region1, Region2, SuppRegion2, Region3, Region4, Region5
from .cores.boundary import Boundary23
from .visco import visc
from .constants import PRESSC, RHOC, TEMPC


def saturationT(tsat):
    """Calculate properties at saturation phase using saturation temperature as input

    Available Properties
    --------------------
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
    mu: float or inf
        dynamic viscosity (Pa*s), return inf when tsat near critical temperature, because near critical temperature value of mu is not accurate

    Limit
    -----
    273.15 K <= tsat <= 647.096 K or 0 C <= tsat <= 373.946 C


    Parameters
    ----------
    tsat: float
       saturation temperature (K)

    Returns
    -------
    props: dict
        return all available properties, see Available Properties

    Raises
    ------
    ValueError
        if value of saturation temperature(tsat) exceed or not in range of limit, see Limit
    """

    # psat = 0.
    if tsat and (psat := Region4.getSaturPress(tsat=tsat)) and 273.15 <= tsat <= 623.15 and 0. < psat < PRESSC:
        vf = Region1.props(p=psat, t=tsat, desc="v")
        vg = Region2.props(p=psat, t=tsat, desc="v")
        rhof = 1/vf
        rhog = 1/vg
        props = {
            "psat": psat,
            "tsat": tsat,
            "v": [vf, vg],
            "u": [Region1.props(p=psat, t=tsat, desc="u"), Region2.props(p=psat, t=tsat, desc="u")],
            "h": [Region1.props(p=psat, t=tsat, desc="h"), Region2.props(p=psat, t=tsat, desc="h")],
            "s": [Region1.props(p=psat, t=tsat, desc="s"), Region2.props(p=psat, t=tsat, desc="s")],
            "cv": [Region1.props(p=psat, t=tsat, desc="cv"), Region2.props(p=psat, t=tsat, desc="cv")],
            "cp": [Region1.props(p=psat, t=tsat, desc="cp"), Region2.props(p=psat, t=tsat, desc="cp")],
            "mu": [visc(rho=rhof, t=tsat), visc(rho=rhog, t=tsat)]
        }
        return props
    elif tsat and (psat := Region4.getSaturPress(tsat=tsat)) and 623.15 < tsat < TEMPC and 0. < psat < PRESSC:
        rhof, rhog = Region3.saturRho(psat, tsat)
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhof, 1/rhog],
                "u": [Region3.props(rho=rhof, t=tsat, desc="u"), Region3.props(rho=rhog, t=tsat, desc="u")],
                "h": [Region3.props(rho=rhof, t=tsat, desc="h"), Region3.props(rho=rhog, t=tsat, desc="h")],
                "s": [Region3.props(rho=rhof, t=tsat, desc="s"), Region3.props(rho=rhog, t=tsat, desc="s")],
                "cv": [Region3.props(rho=rhof, t=tsat, desc="cv"), Region3.props(rho=rhog, t=tsat, desc="cv")],
                "cp": [Region3.props(rho=rhof, t=tsat, desc="cp"), Region3.props(rho=rhog, t=tsat, desc="cp")],
                "mu": [visc(rho=rhof, t=tsat), visc(rho=rhog, t=tsat)]
        }
        return props
    elif tsat and tsat == TEMPC:
        props = {
                "psat": PRESSC,
                "tsat": tsat,
                "v": [1/RHOC, 1/RHOC],
                "u": [Region3.props(rho=RHOC, t=tsat, desc="u"), Region3.props(rho=RHOC, t=tsat, desc="u")],
                "h": [Region3.props(rho=RHOC, t=tsat, desc="h"), Region3.props(rho=RHOC, t=tsat, desc="h")],
                "s": [Region3.props(rho=RHOC, t=tsat, desc="s"), Region3.props(rho=RHOC, t=tsat, desc="s")],
                "cv": [math.inf, math.inf],
                "cp": [math.inf, math.inf],
                "mu": [math.inf, math.inf]
        }
        return props
    else:
        raise ValueError("Value of saturation temperature(tsat) exceed or not in range of limit")


def saturationP(psat):
    """Calculate properties at saturation phase using saturation pressure as input

    Available Properties
    --------------------
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
    mu: float or inf
        dynamic viscosity (Pa*s), return inf when tsat near critical temperature, because near critical temperature value of mu is not accurate

    Limit
    -----
    0.6112127 KPa <= psat <= 22064 KPa or 0.6112127e-3 MPa <= psat <= 22.064 MPa


    Parameters
    ----------
    psat: float
       saturation pressure (KPa)

    Returns
    -------
    props: dict
        return all available properties, see Available Properties

    Raises
    ------
    ValueError
        if value of saturation pressure(psat) exceed or not in range of limit, see Limit
    """

    # tsat = 0.
    if psat and (tsat := Region4.getSaturTemp(psat=psat)) and 0.6112127 <= psat <= 16529.2 and 273.15 <= tsat < TEMPC:
        vf = Region1.props(p=psat, t=tsat, desc="v")
        vg = Region2.props(p=psat, t=tsat, desc="v")
        rhof = 1/vf
        rhog = 1/vg
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [vf, vg],
                "u": [Region1.props(p=psat, t=tsat, desc="u"), Region2.props(p=psat, t=tsat, desc="u")],
                "h": [Region1.props(p=psat, t=tsat, desc="h"), Region2.props(p=psat, t=tsat, desc="h")],
                "s": [Region1.props(p=psat, t=tsat, desc="s"), Region2.props(p=psat, t=tsat, desc="s")],
                "cv": [Region1.props(p=psat, t=tsat, desc="cv"), Region2.props(p=psat, t=tsat, desc="cv")],
                "cp": [Region1.props(p=psat, t=tsat, desc="cp"), Region2.props(p=psat, t=tsat, desc="cp")],
                "mu": [visc(rho=rhof, t=tsat), visc(rho=rhog, t=tsat)]

        }
        return props
    elif psat and (tsat := Region4.getSaturTemp(psat=psat)) and 16529.2 < psat < PRESSC and 273.15 <= tsat < TEMPC:
        rhof, rhog = Region3.saturRho(psat, tsat)
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhof, 1/rhog],
                "u": [Region3.props(rho=rhof, t=tsat, desc="u"), Region3.props(rho=rhog, t=tsat, desc="u")],
                "h": [Region3.props(rho=rhof, t=tsat, desc="h"), Region3.props(rho=rhog, t=tsat, desc="h")],
                "s": [Region3.props(rho=rhof, t=tsat, desc="s"), Region3.props(rho=rhog, t=tsat, desc="s")],
                "cv": [Region3.props(rho=rhof, t=tsat, desc="cv"), Region3.props(rho=rhog, t=tsat, desc="cv")],
                "cp": [Region3.props(rho=rhof, t=tsat, desc="cp"), Region3.props(rho=rhog, t=tsat, desc="cp")],
                "mu": [visc(rho=rhof, t=tsat), visc(rho=rhog, t=tsat)]
        }
        return props
    elif psat and psat == PRESSC:
        props = {
                "psat": psat,
                "tsat": TEMPC,
                "v": [1/RHOC, 1/RHOC],
                "u": [Region3.props(rho=RHOC, t=TEMPC, desc="u"), Region3.props(rho=RHOC, t=TEMPC, desc="u")],
                "h": [Region3.props(rho=RHOC, t=TEMPC, desc="h"), Region3.props(rho=RHOC, t=TEMPC, desc="h")],
                "s": [Region3.props(rho=RHOC, t=TEMPC, desc="s"), Region3.props(rho=RHOC, t=TEMPC, desc="s")],
                "cv": [math.inf, math.inf],
                "cp": [math.inf, math.inf],
                "mu": [math.inf, math.inf]
        }
        return props
    else:
        raise ValueError("Value of saturation pressure(psat) exceed or not in range limit")


def singlephase(p, t):
    """Calculate properties at single phase using pressure and temperature as inputs

    Available Properties
    --------------------
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
    mu: float or None
        dynamic viscosity (Pa*s), if value of temperature(t) exceed and/or not in range limit return None instead, see Limits

    Limits
    ------
    273.15 K <= t <= 1073 K or 0 C <= t <= 800 C for 0 < p <= 100 MPa or 0 < p <= 100000 KPa and 1073.15 K <= t <= 2273 K or 800 C <= t <= 2000 C
    for 0 < p <= 50 MPa or 0 < p <= 50000 KPa

    *mu: 273.15 K <= t <= 1173.15 K or 0 C <= t <= 900 C


    Parameters
    ----------
    p: float
        pressure (KPa)
    t: float
        temperature (K)

    Returns
    -------
    props: dict
        return all available properties, see Available Properties

    Raises
    ------
    ValueError
        if value of pressure(p) or temperature(t) exceed or not in range of limits, see Limits
    """

    # t23 = 0.
    if 0 < p < (psat := Region4.getSaturPress(tsat=t)) and 273.15 <= t <= 623.15:
        v = Region2.props(p, t, desc="v")
        rho = 1/v
        props = {
                "v": v,
                "u": Region2.props(p, t, desc="u"),
                "h": Region2.props(p, t, desc="h"),
                "s": Region2.props(p, t, desc="s"),
                "cv": Region2.props(p, t, desc="cv"),
                "cp": Region2.props(p, t, desc="cp"),
                "mu": visc(rho, t)
        }
        return props
    elif (psat := Region4.getSaturPress(tsat=t)) <= p <= 1e5 and 273.15 <= t <= 623.15:
        v = Region1.props(p, t, desc="v")
        rho = 1/v
        props = {
                "v": v,
                "u": Region1.props(p, t, desc="u"),
                "h": Region1.props(p, t, desc="h"),
                "s": Region1.props(p, t, desc="s"),
                "cv": Region1.props(p, t, desc="cv"),
                "cp": Region1.props(p, t, desc="cp"),
                "mu": visc(rho, t)
        }
        return props
    elif (p23 := Boundary23.getPress(t)) and 0 < p <= p23 and 623.15 < t <= 863.15:
        v = Region2.props(p, t, desc="v")
        rho = 1/v
        props = {
                "v": v,
                "u": Region2.props(p, t, desc="u"),
                "h": Region2.props(p, t, desc="h"),
                "s": Region2.props(p, t, desc="s"),
                "cv": Region2.props(p, t, desc="cv"),
                "cp": Region2.props(p, t, desc="cp"),
                "mu": visc(rho, t)
        }
        return props
    elif (p23 := Boundary23.getPress(t)) and (t23 := Boundary23.getTemp(p)) and p23 < p <= 1e5 and 623.15 < t <= t23:
        rho = Region3VPT.singleRho(p, t)
        props = {
                "v": 1/rho,
                "u": Region3.props(rho, t, desc="u"),
                "h": Region3.props(rho, t, desc="h"),
                "s": Region3.props(rho, t, desc="s"),
                "cv": Region3.props(rho, t, desc="cv"),
                "cp": Region3.props(rho, t, desc="cp"),
                "mu": visc(rho, t)
        }
        return props
    elif 0 < p <= 1e5 and 863.15 < t <= 1073.15:
        v = Region2.props(p, t, desc="v")
        rho = 1/v
        props = {
                "v": v,
                "u": Region2.props(p, t, desc="u"),
                "h": Region2.props(p, t, desc="h"),
                "s": Region2.props(p, t, desc="s"),
                "cv": Region2.props(p, t, desc="cv"),
                "cp": Region2.props(p, t, desc="cp"),
                "mu": visc(rho, t)
        }
        return props
    elif 0 < p <= 5e4 and 1073.15 < t <= 1173.15:
        v = Region5.props(p, t, desc="v")
        rho = 1/v
        props = {
                "v": v,
                "u": Region5.props(p, t, desc="u"),
                "h": Region5.props(p, t, desc="h"),
                "s": Region5.props(p, t, desc="s"),
                "cv": Region5.props(p, t, desc="cv"),
                "cp": Region5.props(p, t, desc="cp"),
                "mu": visc(rho, t)
        }
        return props
    elif 0 < p <= 5e4 and 1173.15 < t <= 2273.15:
        props = {
                "v" : v,
                "u" : Region5.props(p, t, desc="u"),
                "h" : Region5.props(p, t, desc="h"),
                "s" : Region5.props(p, t, desc="s"),
                "cv": Region5.props(p, t, desc="cv"),
                "cp": Region5.props(p, t, desc="cp"),
                "mu": None
        }
        return props
    else:
        raise ValueError("Value of pressure(p) and/or temperature(t) exceed or not in range of limits")


def if97(p=None, t=None, x=None):
    """Calculate ordinary/pure water properties at mixed and single phase

    Available Properties
    --------------------
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
    mu: float or None
        dynamic viscosity (Pa*s), if value of temperature(t) exceed and/or not in range of limit return None instead, see Limits

    Limits
    ------
    Mixed phase
        273.15 K <= t <= 647.096 K or 0 C <= t <= 373.946 C and

        0.6112127 KPa <= p <= 22064 KPa and

        0 <= x <= 1
    Single phase
        273.15 K <= t <= 1073 K or 0 C <= t <= 800 C for 0 < p <= 100 MPa or 0 < p <= 100000 KPa,

        1073.15 K <= t <= 2273 K or 800 C <= t <= 2000 C for 0 < p <= 50 MPa or 0 < p <= 50000 KPa
    *mu
        273.15 K <= t <= 1173.15 K or 0 C <= t <= 900 C


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
    props: dict
        return all available properties, see Available Properties

    Raises
    ------
    ValueError
        when value of inputs exceed and/or not in range of limits, see Limits.
    """

    props = dict()
    if (not p) and t and (x is not None) and 273.15 <= t < TEMPC and 0. <= x <= 1.:
        ans = saturationT(tsat=t)
        v = ans["v"]
        u = ans["u"]
        h = ans["h"]
        s = ans["s"]
        cp = ans["cp"]
        cv = ans["cv"]
        vmix = v[0]+x*(v[1]-v[0])
        rho = 1/vmix
        props["psat"] = ans["psat"]
        props["tsat"] = ans["tsat"]
        props["v"] = vmix
        props["u"] = u[0]+x*(u[1]-u[0])
        props["s"] = s[0]+x*(s[1]-s[0])
        props["h"] = h[0]+x*(h[1]-h[0])
        props["cp"] = cp[0]+x*(cp[1]-cp[0])
        props["cv"] = cv[0]+x*(cv[1]-cv[0])
        props["mu"] = visc(rho, t)
        return props
    elif (not p) and t and (x is not None) and t == TEMPC and 0. <= x <= 1.:
        ans = saturationT(tsat=t)
        v = ans["v"]
        u = ans["u"]
        h = ans["h"]
        s = ans["s"]
        vmix = v[0]+x*(v[1]-v[0])
        props["psat"] = ans["psat"]
        props["tsat"] = ans["tsat"]
        props["v"] = vmix
        props["u"] = u[0]+x*(u[1]-u[0])
        props["s"] = s[0]+x*(s[1]-s[0])
        props["h"] = h[0]+x*(h[1]-h[0])
        props["cp"] = math.inf
        props["cv"] = math.inf
        props["mu"] = math.inf
        return props
    elif p and (not t) and (x is not None) and 0.6112127 <= p < PRESSC and 0. <= x <= 1.:
        ans = saturationP(psat=p)
        v = ans["v"]
        u = ans["u"]
        h = ans["h"]
        s = ans["s"]
        cp = ans["cp"]
        cv = ans["cv"]
        vmix = v[0]+x*(v[1]-v[0])
        rho = 1/vmix
        props["psat"] = ans["psat"]
        props["tsat"] = ans["tsat"]
        props["v"] = vmix
        props["u"] = u[0]+x*(u[1]-u[0])
        props["s"] = s[0]+x*(s[1]-s[0])
        props["h"] = h[0]+x*(h[1]-h[0])
        props["cp"] = cp[0]+x*(cp[1]-cp[0])
        props["cv"] = cv[0]+x*(cv[1]-cv[0])
        props["mu"] = visc(rho, t)
        return props
    elif p and (not t) and (x is not None) and p == PRESSC and 0. <= x <= 1.:
        ans = saturationT(tsat=t)
        v = ans["v"]
        u = ans["u"]
        h = ans["h"]
        s = ans["s"]
        vmix = v[0]+x*(v[1]-v[0])
        props["psat"] = ans["psat"]
        props["tsat"] = ans["tsat"]
        props["v"] = vmix
        props["u"] = u[0]+x*(u[1]-u[0])
        props["s"] = s[0]+x*(s[1]-s[0])
        props["h"] = h[0]+x*(h[1]-h[0])
        props["cp"] = math.inf
        props["cv"] = math.inf
        props["mu"] = math.inf
        return props
    elif p and t and (not x) and 0 < p <= 1e5 and 273.15 <= t <= 2273.15:
        props = singlephase(p, t)
        return props
    elif ((p is not None) or (t is not None)) and (x is not None) and (x < 0 or x > 1):
        raise ValueError("Quality(x) value exceed and/or not in range of validity")