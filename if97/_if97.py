import math
from .koefisien import BIGR, TEMPC, RHOC, TEMPT, PRESSC, PRESST
from .cores.basic import region1, region2, region3, region4_satpress, region4_sattemp, region5
from .cores.backwardPT import region3PT
from .cores.boundary import Boundary23, temp3


def saturation(psat0=None, tsat0=None):

    props = dict()

    if tsat0 and 273.15 <= tsat0 <= 623.15:

        psat = region4_satpress(tsat0)

        if psat and psat > 0.:

            props = {
                "psat": psat,
                "tsat": tsat0,
                "Liquid": {
                        "v": region1(p=psat, t=tsat0, desc="v"),
                        "u": region1(p=psat, t=tsat0, desc="u"),
                        "h": region1(p=psat, t=tsat0, desc="h"),
                        "s": region1(p=psat, t=tsat0, desc="s"),
                        "cv": region1(p=psat, t=tsat0, desc="cv"),
                        "cp": region1(p=psat, t=tsat0, desc="cp")
                },
                "Vapor": {
                        "v" : region2(p=psat, t=tsat0, desc="v"),
                        "u" : region2(p=psat, t=tsat0, desc="u"),
                        "h" : region2(p=psat, t=tsat0, desc="h"),
                        "s" : region2(p=psat, t=tsat0, desc="s"),
                        "cv": region2(p=psat, t=tsat0, desc="cv"),
                        "cp": region2(p=psat, t=tsat0, desc="cp")
                }
            }

        return props

    elif tsat0 and 623.15 < tsat0 <= 643.15:

        psat = region4_satpress(tsat0)
        pmin = region4_satpress(tsat=623.15)
        pmax = region4_satpress(tsat=643.15)
        p3cd = 1.900881189173920e4
        t3cd = temp3(p=psat, desc="3cd")
        t3jk = temp3(p=psat, desc="3jk")

        rhoL = None
        rhoV = None

        if psat and pmin < psat <= p3cd:
            rhoL = 1/region3PT(p=psat, t=tsat0, desc="3c")
            rhoV = 1/region3PT(p=psat, t=tsat0, desc="3t")
        elif psat and p3cd < psat <= 20.5e3:
            if tsat0 <= t3cd:
                rhoL = 1/region3PT(p=psat, t=tsat0, desc="3c")
            elif tsat0 > t3cd:
                rhoL = 1/region3PT(p=psat, t=tsat0, desc="3s")
            rhoV = 1/region3PT(p=psat, t=tsat0, desc="3t")
        elif psat and 20.5e3 < psat <= pmax:
            if tsat0 <= t3cd:
                rhoL = 1/region3PT(p=psat, t=tsat0, desc="3c")
            elif tsat0 > t3cd:
                rhoL = 1/region3PT(p=psat, t=tsat0, desc="3s")

            if tsat0 <= t3jk:
                rhoV = 1/region3PT(p=psat, t=tsat0, desc="3r")
            elif tsat0 > t3jk:
                rhoV = 1/region3PT(p=psat, t=tsat0, desc="3k")

        props = {
            "psat": psat,
            "tsat": tsat0,
            "Liquid": {
                    "v" : 1/rhoL,
                    "u" : region3(rho=rhoL, t=tsat0, desc="u"),
                    "h" : region3(rho=rhoL, t=tsat0, desc="h"),
                    "s" : region3(rho=rhoL, t=tsat0, desc="s"),
                    "cv": region3(rho=rhoL, t=tsat0, desc="cv"),
                    "cp": region3(rho=rhoL, t=tsat0, desc="cp")
            },
            "Vapor": {
                    "v" : 1/rhoV,
                    "u" : region3(rho=rhoV, t=tsat0, desc="u"),
                    "h" : region3(rho=rhoV, t=tsat0, desc="h"),
                    "s" : region3(rho=rhoV, t=tsat0, desc="s"),
                    "cv": region3(rho=rhoV, t=tsat0, desc="cv"),
                    "cp": region3(rho=rhoV, t=tsat0, desc="cp")
            }
        }

        return props
    elif tsat0 and 643.15 < tsat0 <= TEMPC:
        psat = region4_satpress(tsat0)
        pmin = region4_satpress(tsat=643.15)
        pmidL = 21.93161551e3
        pmidV = 21.90096265e3

        volL = None
        rhoV = None

        if pmidL < psat < PRESSC or math.isclose(psat, PRESSC, abs_tol=1e-6):
            if temp3(p=psat, desc="3qu") < tsat0 <= temp3(p=psat, desc="3uv"):
                volL = region3PT(p=psat, t=tsat0, desc="3u")
            elif tsat0 > temp3(p=psat, desc="3uv"):
                volL = region3PT(p=psat, t=tsat0, desc="3y")
        elif pmin < psat <= pmidL:
            if temp3(p=psat, desc="3qu") < tsat0:
                volL = region3PT(p=psat, t=tsat0, desc="3u")

        if pmin < psat <= pmidV:
            if tsat0 <= temp3(p=psat, desc="3rx"):
                rhoV = 1/region3PT(p=psat, t=tsat0, desc="3x")
        elif pmidV < psat < PRESSC or math.isclose(psat, PRESSC, abs_tol=1e-6):
            if tsat0 <= temp3(p=psat, desc="3wx"):
                rhoV = 1/region3PT(p=psat, t=tsat0, desc="3z")
            elif temp3(p=psat, desc="3wx") < tsat0 <= temp3(p=psat, desc="3rx"):
                rhoV = 1/region3PT(p=psat, t=tsat0, desc="3x")

        props = {
                "psat"  : psat,
                "tsat"  : tsat0,
                "Liquid": {
                        "v" : volL,
                        "u" : region3(rho=(1/volL), t=tsat0, desc="u"),
                        "h" : region3(rho=(1/volL), t=tsat0, desc="h"),
                        "s" : region3(rho=(1/volL), t=tsat0, desc="s"),
                        "cv": region3(rho=(1/volL), t=tsat0, desc="cv"),
                        "cp": region3(rho=(1/volL), t=tsat0, desc="cp")
                },
                "Vapor" : {
                        "v" : 1/rhoV,
                        "u" : region3(rho=rhoV, t=tsat0, desc="u"),
                        "h" : region3(rho=rhoV, t=tsat0, desc="h"),
                        "s" : region3(rho=rhoV, t=tsat0, desc="s"),
                        "cv": region3(rho=rhoV, t=tsat0, desc="cv"),
                        "cp": region3(rho=rhoV, t=tsat0, desc="cp")
                }
        }

        return props
    else:
        return None