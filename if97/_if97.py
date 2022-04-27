from .koefisien import BIGR, TEMPC, RHOC, TEMPT, PRESSC, PRESST
from .cores.basic import region1, region2, supp_region2, region3, region4, region5, saturRho
from .cores.backwardPT import Reg3RhoPT
from .cores.boundary import Boundary23, temp3


def saturationT(tsat=None):

    props = dict()

    if tsat and 273.15 <= tsat <= 623.15:
        psat = region4(tsat=tsat)

        if psat and psat > 0.:
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
    elif tsat and 623.15 < tsat < TEMPC:
        psat = region4(tsat=tsat)
        rhoL = rhoV = 1.

        if psat:
            rhoL, rhoV = saturRho(psat, tsat)

        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhoL, 1/rhoV],
                "u": [region3(rho=rhoL, t=tsat, desc="u"), region3(rho=rhoV, t=tsat, desc="u")],
                "h": [region3(rho=rhoL, t=tsat, desc="h"), region3(rho=rhoV, t=tsat, desc="h")],
                "s": [region3(rho=rhoL, t=tsat, desc="s"), region3(rho=rhoV, t=tsat, desc="s")],
                "cv": [region3(rho=rhoL, t=tsat, desc="cv"), region3(rho=rhoV, t=tsat, desc="cv")],
                "cp": [region3(rho=rhoL, t=tsat, desc="cp"), region3(rho=rhoV, t=tsat, desc="cp")]
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

    props = dict()

    if psat and 0.6112127 <= psat <= 16529.2:
        tsat = region4(psat=psat)
        if tsat:
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
    elif psat and 16529.2 < psat < PRESSC:

        tsat = region4(psat=psat)
        rhoL = rhoV = 1.

        if psat:
            rhoL, rhoV = saturRho(psat, tsat)

        props = {
                "psat": psat,
                "tsat": tsat,
                "v": [1/rhoL, 1/rhoV],
                "u": [region3(rho=rhoL, t=tsat, desc="u"), region3(rho=rhoV, t=tsat, desc="u")],
                "h": [region3(rho=rhoL, t=tsat, desc="h"), region3(rho=rhoV, t=tsat, desc="h")],
                "s": [region3(rho=rhoL, t=tsat, desc="s"), region3(rho=rhoV, t=tsat, desc="s")],
                "cv": [region3(rho=rhoL, t=tsat, desc="cv"), region3(rho=rhoV, t=tsat, desc="cv")],
                "cp": [region3(rho=rhoL, t=tsat, desc="cp"), region3(rho=rhoV, t=tsat, desc="cp")]
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

    if 0 < p <= region4(tsat=t) and 273.15 <= t <= 623.15:
        props = {
                "v" : region2(p, t, desc="v"),
                "u" : region2(p, t, desc="u"),
                "h" : region2(p, t, desc="h"),
                "s" : region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp"),
        }
        return props
    elif region4(tsat=t) <= p <= 1e5 and 273.15 <= t <= 623.15:
        props = {
                "v" : region1(p, t, desc="v"),
                "u" : region1(p, t, desc="u"),
                "h" : region1(p, t, desc="h"),
                "s" : region1(p, t, desc="s"),
                "cv": region1(p, t, desc="cv"),
                "cp": region1(p, t, desc="cp"),
        }
        return props
    elif Boundary23.getTemp(p) and Boundary23.getPress(t) and 0 < p <= Boundary23.getPress(t) and 623.15 < t <= 863.15:
        props = {
                "v" : region2(p, t, desc="v"),
                "u" : region2(p, t, desc="u"),
                "h" : region2(p, t, desc="h"),
                "s" : region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp"),
        }
        return props
    elif Boundary23.getTemp(p) and Boundary23.getPress(t) and Boundary23.getPress(t) <= p <= 1e5 and 623.15 < t <= Boundary23.getTemp(p):
        rho = Reg3RhoPT.singleRho(p, t)
        props = {
                "v" : 1/rho,
                "u" : region3(rho, t, desc="u"),
                "h" : region3(rho, t, desc="h"),
                "s" : region3(rho, t, desc="s"),
                "cv": region3(rho, t, desc="cv"),
                "cp": region3(rho, t, desc="cp"),
        }
        return props
    elif 0 < p <= 1e5 and 863.15 < t <= 1073.15:
        props = {
                "v" : region2(p, t, desc="v"),
                "u" : region2(p, t, desc="u"),
                "h" : region2(p, t, desc="h"),
                "s" : region2(p, t, desc="s"),
                "cv": region2(p, t, desc="cv"),
                "cp": region2(p, t, desc="cp"),
        }
        return props
    elif 0 < p <= 5e4 and 1073.15 < t <= 2273.15:
        props = {
                "v" : region5(p, t, desc="v"),
                "u" : region5(p, t, desc="u"),
                "h" : region5(p, t, desc="h"),
                "s" : region5(p, t, desc="s"),
                "cv": region5(p, t, desc="cv"),
                "cp": region5(p, t, desc="cp"),
        }
        return props
    else:
        return None


def allphase(**kwargs):
    default_keys = ["p", "t", "x"]
    inputs = list(kwargs.keys())
    ans = dict()
    if len(inputs) == 2:
        if inputs[0].lower() in default_keys and inputs[1].lower() in default_keys:
            if inputs[0].lower() == "t" and inputs[1].lower() == "x":
                props = saturationT(tsat=kwargs[inputs[0]])
                vf, vg = props["v"]
                ans["v"] = vf + kwargs[inputs[1]]*(vg-vf)
                return ans