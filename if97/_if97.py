from .cores.backwardPT import Reg3RhoPT
from .cores.basic import region1, region2, region3, region4, region5, saturRho
from .cores.boundary import Boundary23
from .koefisien import PRESSC, RHOC, TEMPC


def saturationT(tsat=None):
    """Fungsi untuk mencari propertis pada titik saturasi dengan input suhu saturasi"""

    psat = 0.
    if tsat and (psat := region4(tsat=tsat)) and 273.15 <= tsat <= 623.15 and 0. < psat < PRESSC:
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
    elif tsat and (psat := region4(tsat=tsat)) and 623.15 < tsat < TEMPC and 0. < psat < PRESSC:
        rhof, rhog = saturRho(psat, tsat)
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhof, 1/rhog],
                "u": [region3(rho=rhof, t=tsat, desc="u"), region3(rho=rhog, t=tsat, desc="u")],
                "h": [region3(rho=rhof, t=tsat, desc="h"), region3(rho=rhog, t=tsat, desc="h")],
                "s": [region3(rho=rhof, t=tsat, desc="s"), region3(rho=rhog, t=tsat, desc="s")],
                "cv": [region3(rho=rhof, t=tsat, desc="cv"), region3(rho=rhog, t=tsat, desc="cv")],
                "cp": [region3(rho=rhof, t=tsat, desc="cp"), region3(rho=rhog, t=tsat, desc="cp")]
        }
        return props
    elif tsat and tsat == TEMPC:
        props = {
                "psat": PRESSC,
                "tsat": tsat,
                "v": [1/RHOC, 1/RHOC],
                "u": [region3(rho=RHOC, t=tsat, desc="u"), region3(rho=RHOC, t=tsat, desc="u")],
                "h": [region3(rho=RHOC, t=tsat, desc="h"), region3(rho=RHOC, t=tsat, desc="h")],
                "s": [region3(rho=RHOC, t=tsat, desc="s"), region3(rho=RHOC, t=tsat, desc="s")],
                "cv": [None, None],
                "cp": [None, None]
        }
        return props
    else:
        return None


def saturationP(psat):
    """Fungsi untuk mencari propertis pada titik saturasi dengan input tekanan saturasi"""

    tsat = 0.
    if psat and (tsat := region4(psat=psat)) and 0.6112127 <= psat <= 16529.2 and 273.15 <= tsat < TEMPC:
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
    elif psat and (tsat := region4(psat=psat)) and 16529.2 < psat < PRESSC and 273.15 <= tsat < TEMPC:
        rhof, rhog = saturRho(psat, tsat)
        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhof, 1/rhog],
                "u": [region3(rho=rhof, t=tsat, desc="u"), region3(rho=rhog, t=tsat, desc="u")],
                "h": [region3(rho=rhof, t=tsat, desc="h"), region3(rho=rhog, t=tsat, desc="h")],
                "s": [region3(rho=rhof, t=tsat, desc="s"), region3(rho=rhog, t=tsat, desc="s")],
                "cv": [region3(rho=rhof, t=tsat, desc="cv"), region3(rho=rhog, t=tsat, desc="cv")],
                "cp": [region3(rho=rhof, t=tsat, desc="cp"), region3(rho=rhog, t=tsat, desc="cp")]
        }
        return props
    elif psat and psat == PRESSC:
        props = {
                "psat": psat,
                "tsat": TEMPC,
                "v": [1/RHOC, 1/RHOC],
                "u": [region3(rho=RHOC, t=TEMPC, desc="u"), region3(rho=RHOC, t=TEMPC, desc="u")],
                "h": [region3(rho=RHOC, t=TEMPC, desc="h"), region3(rho=RHOC, t=TEMPC, desc="h")],
                "s": [region3(rho=RHOC, t=TEMPC, desc="s"), region3(rho=RHOC, t=TEMPC, desc="s")],
                "cv": [None, None],
                "cp": [None, None]
        }
        return props
    else:
        return None


def singlephase(p, t):
    """Fungsi untuk mencari propertis pada titik satu fase dengan input tekanan dan suhu"""

    t23 = 0.
    if 0 < p < (psat := region4(tsat=t)) and 273.15 <= t <= 623.15:
        props = {
                "v": region2(p, t, desc="v"),
                "u": region2(p, t, desc="u"),
                "h": region2(p, t, desc="h"),
                "s": region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp")
        }
        return props
    elif (psat := region4(tsat=t)) <= p <= 1e5 and 273.15 <= t <= 623.15:
        props = {
                "psat": psat,
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
        rho = Reg3RhoPT.singleRho(p, t)
        props = {
                "v": 1/rho,
                "u": region3(rho, t, desc="u"),
                "h": region3(rho, t, desc="h"),
                "s": region3(rho, t, desc="s"),
                "cv": region3(rho, t, desc="cv"),
                "cp": region3(rho, t, desc="cp")
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
    else:
        return None


def if97(p=None, t=None, x=None):

    ans = dict()
    if (not p) and t and (x is not None) and 273.15 <= t <= TEMPC and 0. <= x <= 1.:
        props = saturationT(tsat=t)
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
        ans["cp"] = cp[0] + x*(cp[1]-cp[0])
        ans["cv"] = cv[0] + x*(cv[1]-cv[0])
        return ans
    elif p and (not t) and (x is not None) and 0.6112127 <= p <= PRESSC and 0. <= x <= 1.:
        props = saturationP(psat=p)
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
        ans["cp"] = cp[0]+x*(cp[1]-cp[0])
        ans["cv"] = cv[0]+x*(cv[1]-cv[0])
        return ans
    elif p and t and (not x) and p <= 1e5 and 273.15 <= t <= 2273.15:
        return singlephase(p, t)
    else:
        return None