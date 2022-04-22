from numpy import exp
from ..koefisien import IJnSubReg3


def region3PT(p, t, desc=None):

    if desc and desc.lower() != "3n":
        a = IJnSubReg3[desc.lower()]["a"]
        b = IJnSubReg3[desc.lower()]["b"]
        c = IJnSubReg3[desc.lower()]["c"]
        d = IJnSubReg3[desc.lower()]["d"]
        e = IJnSubReg3[desc.lower()]["e"]
        I = IJnSubReg3[desc.lower()]["I"]
        J = IJnSubReg3[desc.lower()]["J"]
        n = IJnSubReg3[desc.lower()]["n"]
        v0 = IJnSubReg3[desc.lower()]["vol0"]
        p0 = IJnSubReg3[desc.lower()]["press0"]
        t0 = IJnSubReg3[desc.lower()]["temp0"]

        pi = p/p0
        theta = t/t0

        omega = 0.
        for Ii, Ji, ni, in zip(I, J, n):
            omega += ni*(((pi-a)**c)**Ii)*(((theta-b)**d)**Ji)

        return v0*(omega**e)
    elif desc and desc.lower() == "3n":
        a = IJnSubReg3["3n"]["a"]
        b = IJnSubReg3["3n"]["b"]
        I = IJnSubReg3["3n"]["I"]
        J = IJnSubReg3["3n"]["J"]
        n = IJnSubReg3["3n"]["n"]
        v0 = IJnSubReg3["3n"]["vol0"]
        p0 = IJnSubReg3["3n"]["press0"]
        t0 = IJnSubReg3["3n"]["temp0"]

        pi = p/p0
        theta = t/t0

        omega = 0.
        for Ii, Ji, ni, in zip(I, J, n):
            omega += ni*((pi-a)**Ii)*((theta-b)**Ji)

        return v0*exp(omega)
    else:
        return None