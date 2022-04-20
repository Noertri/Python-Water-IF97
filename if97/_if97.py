from .koefisien import BIGR, TEMPC, RHOC, TEMPT, PRESSC, PRESST
from .cores import region1, region2, region3, region4, region5
from .cores.boundary import Boundary23


def saturation(psat=None, tsat=None):

    props = dict()

    if tsat and tsat >= 273.15 and tsat <= 623.15:

        psat = region4.get_satur_press(tsat)
        props["psat"] = psat
        props["tsat"] = tsat

        if psat and psat <= 1e5:
            reg1 = region1.Region1(p=psat, t=tsat)
            reg2 = region2.Region2(p=psat, t=tsat)

            props["Liquid"] = {
                    "v": reg1.get_properties("v"),
                    "u": reg1.get_properties("u"),
                    "h": reg1.get_properties("h"),
                    "s": reg1.get_properties("s"),
                    "cv": reg1.get_properties("cv"),
                    "cp": reg1.get_properties("cp")
            }

            props["Vapor"] = {
                    "v" : reg2.get_properties("v"),
                    "u" : reg2.get_properties("u"),
                    "h" : reg2.get_properties("h"),
                    "s" : reg2.get_properties("s"),
                    "cv": reg2.get_properties("cv"),
                    "cp": reg2.get_properties("cp")
            }

        return props

    elif tsat and tsat > 623.15 and tsat <= TEMPC:

        psat = region4.get_satur_press(tsat)

        props["psat"] = psat
        props["tsat"] = tsat
        props["p23"] = Boundary23.getPress(t=tsat)
        props["t23"] = Boundary23.getTemp(p=psat)

        return props

    else:
        return None