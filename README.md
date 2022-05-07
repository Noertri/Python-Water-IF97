## About
This repository contains program of implementation IAPWS-IF97 using python. This program can be used to calculate ordinary/pure water properties such as specific volume, specific internal energy, specific enthalpy, specific entropy, etc. This program has been verified with values from journals/books in [References]. In folder GUI there is simple calculator as an example of implementaion of this program as backend/engine/library.

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
1. IAPWS, R7-97(2012), *Revised Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam (The revision only relates to the extension of region 5 to 50 MPa)* (August 2007), Available from http://www.iapws.org/relguide/IF97-Rev.pdf

2. IAPWS, SR5-05(2016), *Revised Supplementary Release on Backward Equations for Specific Volume as a Function of Pressure and Temperature v(p,T) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam* (June 2014), Available from http://www.iapws.org/relguide/Supp-VPT3-2016.pdf

3. Kretzschmar, Hans-Joachim, Wagner, Wolfgang. (2019). *International Steam Tables Properties of Water and Steam based on the Industrial Formulation IAPWS-IF97 (3rd Edition) Tables, Algorithms, and Diagrams*. Berlin: Springer Vieweg. Doi: https://doi.org/10.1007/978-3-662-53219-5
