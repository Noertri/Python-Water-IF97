from .koefisien import BIGR, TEMPC, RHOC, TEMPT, PRESSC, PRESST
from .cores import region1, region2, region3, region4, region5, boundary


def saturation_temp(tsat):

    psat = region4.get_satur_press(tsat)

