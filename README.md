# IMPLEMENTATION OF IAPWS-IF97 IN PYTHON
## What is IAPWS-IF97?
IAPWS-IF97 is formulation to calculate thermodynamical properties of ordinary/pure water for industrial use (primarily in the steam power industry). It approximate IAPWS-95 (formulation for general and scientific use) but with faster computational speed. The formulation is valid fro 273.15 K to 1073.15 K at pressure to 100 MPa and from 1073.15 K to 2273.15 K at 50 MPa.

## Examples
Calculate properties at mixed phase using temperature(t) and quality(x) as inputs:

```Python
From IF97 import if97


ans = if97(t=273.15, x=0.)
print(ans)
```
Calculate properties at mixed phase using presssure(p) and quality(x) as inputs:
```Python
From IF97 import if97


ans = if97(p=101.325, x=0.)
print(ans)
```
Calculate properties at single phase:
```Python
From IF97 import if97


ans = if97(p=101.325, t=373.1243)
print(ans)
```
Note: temperature must be in kelvin(K), pressure must be in kilopascal(KPa)

## References
