## About
This repository contains program of implementation IAPWS-IF97 using python. This program can be used to calculate ordinary/pure water properties such as specific volume, specific internal energy, specific enthalpy, specific entropy, etc. This program is still in raw script, there is no wheel package yet.

## What is IAPWS-IF97?
IAPWS-IF97 is formulation to calculate thermodynamical properties of ordinary/pure water for industrial use (primarily in the steam power industry). It approximate IAPWS-95 (formulation for general and scientific use) but with faster computational speed. The formulation is valid fro 273.15 K to 1073.15 K at pressure to 100 MPa and from 1073.15 K to 2273.15 K at 50 MPa.

## Examples
Calculate properties at mixed phase using temperature(t) and quality(x) as inputs:

```Python
From IF97 import if97


ans = if97(t=273.15, x=0.)
print(ans)
```

Output
```Python
{'psat': 0.6112126774443449, 'tsat': 273.15, 'v': 0.0010002069773244189, 'u': -0.04219916517226274, 's': -0.00015454959194117582, 'h': -0.04158782598765377, 'cp': 4.219933568165597, 'cv': 4.217446063578165}
```

Calculate properties at mixed phase using presssure(p) and quality(x) as inputs:

```Python
From IF97 import if97


ans = if97(p=101.325, x=0.)
print(ans)
```

Output
```Python
{'psat': 101.325, 'tsat': 373.12430000048056, 'v': 0.0010434353664161007, 'u': 418.8849917156877, 's': 1.3067239783648374, 'h': 418.99071780418984, 'cp': 4.216612690426814, 'cv': 3.7678305778810395}
```

Calculate properties at single phase:

```Python
From IF97 import if97


ans = if97(p=101.325, t=373.1243)
print(ans)
```

Output
```Python
{'v': 0.0010434353664157238, 'u': 418.88499171366203, 'h': 418.9907178021641, 's': 1.306723978359408, 'cv': 3.7678305778834753, 'cp': 4.216612690426204}
```

Note: temperature must be in kelvin(K), pressure must be in kilopascal(KPa)

## References
