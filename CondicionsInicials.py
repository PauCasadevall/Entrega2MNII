"""
Noves condicions inicials:
x0=0                  km
y0=147174559.75198743 km
v0x=-30282.79395186   km/s
v0y=-189.84151149     km/s
"""

# farem un canvi de sistema de referència de les condicions inicials de la web d'Horizons per tal de poder-les usar en els nostres codis

import numpy as np

r=np.sqrt((9.2295898e05)**2 +(1.471716657e08)**2)
r_vec=np.array([9.2295898e05,1.471716657e08,0],dtype=float)

sin_a=(9.2295898e05)/r
a=np.arcsin(sin_a)

z=np.array([0,0,1],dtype=float)

vx=-3.0283389e04
vy=7.12429684e-02

v=np.array([vx,vy,0],dtype=float)

vp=v*np.cos(a) +(np.cross(z,v))*sin_a

print("y'= ",r)

print("v'= ",vp)
