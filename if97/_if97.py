from .koefisien import BIGR, TEMPC, RHOC, TEMPT, PRESSC, PRESST
from .cores.basic import region1, region2, supp_region2, region3, region4, region5, region3SatRho
from .cores.backwardPT import region3PT
from .cores.boundary import Boundary23, temp3


def saturationT(tsat=None):

    props = dict()

    if tsat and 273.15 <= tsat <= 623.15:

        psat = region4(tsat=tsat)

        if psat and psat > 0.:

            props = {
                "psat": psat,
                "tsat": tsat,
                "Liquid": {
                        "v": region1(p=psat, t=tsat, desc="v"),
                        "u": region1(p=psat, t=tsat, desc="u"),
                        "h": region1(p=psat, t=tsat, desc="h"),
                        "s": region1(p=psat, t=tsat, desc="s"),
                        "cv": region1(p=psat, t=tsat, desc="cv"),
                        "cp": region1(p=psat, t=tsat, desc="cp")
                },
                "Vapor": {
                        "v" : region2(p=psat, t=tsat, desc="v"),
                        "u" : region2(p=psat, t=tsat, desc="u"),
                        "h" : region2(p=psat, t=tsat, desc="h"),
                        "s" : region2(p=psat, t=tsat, desc="s"),
                        "cv": region2(p=psat, t=tsat, desc="cv"),
                        "cp": region2(p=psat, t=tsat, desc="cp")
                }
            }

        return props
    elif tsat and 623.15 < tsat < TEMPC:
        psat = region4(tsat=tsat)

        rhoL = rhoV = 1.

        if psat:
            rhoL, rhoV = region3SatRho(psat, tsat)

        props = {
                "psat"  : psat,
                "tsat"  : tsat,
                "Liquid": {
                        "v" : 1/rhoL,
                        "u" : region3(rho=rhoL, t=tsat, desc="u"),
                        "h" : region3(rho=rhoL, t=tsat, desc="h"),
                        "s" : region3(rho=rhoL, t=tsat, desc="s"),
                        "cv": region3(rho=rhoL, t=tsat, desc="cv"),
                        "cp": region3(rho=rhoL, t=tsat, desc="cp")
                },
                "Vapor" : {
                        "v" : 1/rhoV,
                        "u" : region3(rho=rhoV, t=tsat, desc="u"),
                        "h" : region3(rho=rhoV, t=tsat, desc="h"),
                        "s" : region3(rho=rhoV, t=tsat, desc="s"),
                        "cv": region3(rho=rhoV, t=tsat, desc="cv"),
                        "cp": region3(rho=rhoV, t=tsat, desc="cp")
                }
        }

        return props
    elif tsat and tsat == TEMPC:

        props = {
                "psat"  : PRESSC,
                "tsat"  : tsat,
                "Liquid": {
                        "v" : 1/RHOC,
                        "u" : region3(rho=RHOC, t=tsat, desc="u"),
                        "h" : region3(rho=RHOC, t=tsat, desc="h"),
                        "s" : region3(rho=RHOC, t=tsat, desc="s"),
                        "cv": None,
                        "cp": None
                },
                "Vapor" : {
                        "v" : 1/RHOC,
                        "u" : region3(rho=RHOC, t=tsat, desc="u"),
                        "h" : region3(rho=RHOC, t=tsat, desc="h"),
                        "s" : region3(rho=RHOC, t=tsat, desc="s"),
                        "cv": None,
                        "cp": None
                }
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
                    "psat"  : psat,
                    "tsat"  : tsat,
                    "Liquid": {
                            "v" : region1(p=psat, t=tsat, desc="v"),
                            "u" : region1(p=psat, t=tsat, desc="u"),
                            "h" : region1(p=psat, t=tsat, desc="h"),
                            "s" : region1(p=psat, t=tsat, desc="s"),
                            "cv": region1(p=psat, t=tsat, desc="cv"),
                            "cp": region1(p=psat, t=tsat, desc="cp")
                    },
                    "Vapor" : {
                            "v" : region2(p=psat, t=tsat, desc="v"),
                            "u" : region2(p=psat, t=tsat, desc="u"),
                            "h" : region2(p=psat, t=tsat, desc="h"),
                            "s" : region2(p=psat, t=tsat, desc="s"),
                            "cv": region2(p=psat, t=tsat, desc="cv"),
                            "cp": region2(p=psat, t=tsat, desc="cp")
                    }
            }

        return props
    elif psat and 16529.2 < psat < PRESSC:

        tsat = region4(psat=psat)

        rhoL = rhoV = 1.

        if psat:
            rhoL, rhoV = region3SatRho(psat, tsat)

        props = {
                "psat"  : psat,
                "tsat"  : tsat,
                "Liquid": {
                        "v" : 1/rhoL,
                        "u" : region3(rho=rhoL, t=tsat, desc="u"),
                        "h" : region3(rho=rhoL, t=tsat, desc="h"),
                        "s" : region3(rho=rhoL, t=tsat, desc="s"),
                        "cv": region3(rho=rhoL, t=tsat, desc="cv"),
                        "cp": region3(rho=rhoL, t=tsat, desc="cp")
                },
                "Vapor" : {
                        "v" : 1/rhoV,
                        "u" : region3(rho=rhoV, t=tsat, desc="u"),
                        "h" : region3(rho=rhoV, t=tsat, desc="h"),
                        "s" : region3(rho=rhoV, t=tsat, desc="s"),
                        "cv": region3(rho=rhoV, t=tsat, desc="cv"),
                        "cp": region3(rho=rhoV, t=tsat, desc="cp")
                }
        }

        return props
    elif psat and psat == PRESSC:
        props = {
                "psat"  : PRESSC,
                "tsat"  : TEMPC,
                "Liquid": {
                        "v" : 1/RHOC,
                        "u" : region3(rho=RHOC, t=TEMPC, desc="u"),
                        "h" : region3(rho=RHOC, t=TEMPC, desc="h"),
                        "s" : region3(rho=RHOC, t=TEMPC, desc="s"),
                        "cv": None,
                        "cp": None
                },
                "Vapor" : {
                        "v" : 1/RHOC,
                        "u" : region3(rho=RHOC, t=TEMPC, desc="u"),
                        "h" : region3(rho=RHOC, t=TEMPC, desc="h"),
                        "s" : region3(rho=RHOC, t=TEMPC, desc="s"),
                        "cv": None,
                        "cp": None
                }
        }

        return props
    else:
        return None


def singleReg12(p, t):
    """Fungsi untuk mencari propertis pada titik satu fase antara suhu 273.15 K sampai 623.15 K dan tekanan antara 0
    MPa sampai 100 MPa"""

    props = dict()
    if 273.15 <= t <= 623.15 and 0 < p <= 1e5:
        psat = region4(tsat=t)
        if psat < p <= 1e5:
            props = {
                    "v" : region1(p=p, t=t, desc="v"),
                    "u" : region1(p=p, t=t, desc="u"),
                    "h" : region1(p=p, t=t, desc="h"),
                    "s" : region1(p=p, t=t, desc="s"),
                    "cv": region1(p=p, t=t, desc="cv"),
                    "cp": region1(p=p, t=t, desc="cp"),
            }
        elif 0 < p < psat:
            props = {
                    "v" : region2(p=p, t=t, desc="v"),
                    "u" : region2(p=p, t=t, desc="u"),
                    "h" : region2(p=p, t=t, desc="h"),
                    "s" : region2(p=p, t=t, desc="s"),
                    "cv": region2(p=p, t=t, desc="cv"),
                    "cp": region2(p=p, t=t, desc="cp"),
            }
        return props
    else:
        return None


def singleReg23(p, t):
    props = dict()
    p23 = Boundary23.getPress(t=t)
    if p < p23:
        props = {
                "v" : region2(p=p, t=t, desc="v"),
                "u" : region2(p=p, t=t, desc="u"),
                "h" : region2(p=p, t=t, desc="h"),
                "s" : region2(p=p, t=t, desc="s"),
                "cv": region2(p=p, t=t, desc="cv"),
                "cp": region2(p=p, t=t, desc="cp"),
        }
    elif p23 < p <= 1e5:
        vol = 1.
        t23 = Boundary23.getTemp(p=p)
        pass

    return props