import math
from .koefisien import BIGR, TEMPC, RHOC, TEMPT, PRESSC, PRESST
from .cores.basic import region1, region2, region3, region4_satpress, region4_sattemp, region5, Region3
from .cores.backwardPT import region3PT
from .cores.boundary import Boundary23, temp3


def saturation_temp(tsat=None):

    props = dict()

    if tsat and 273.15 <= tsat <= 623.15:

        psat = region4_satpress(tsat)

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
        psat = region4_satpress(tsat)

        rhoL = rhoV = 1.

        if psat:
            rhoL, rhoV = Region3.satur_rho(psat, tsat)

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
                        "cv": math.nan,
                        "cp": math.nan
                },
                "Vapor" : {
                        "v" : 1/RHOC,
                        "u" : region3(rho=RHOC, t=tsat, desc="u"),
                        "h" : region3(rho=RHOC, t=tsat, desc="h"),
                        "s" : region3(rho=RHOC, t=tsat, desc="s"),
                        "cv": math.nan,
                        "cp": math.nan
                }
        }

        return props
    else:
        return None