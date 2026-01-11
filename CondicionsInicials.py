# farem un canvi de sistema de referència de les condicions inicials de la web d'Horizons per tal de poder-les usar en els nostres codis

import numpy as np

# 2461031.127083333 = A.D. 2025-Dec-21 15:03:00.0000 TDB 

# en km, km/s

X, Y, Z = 2.522797999003676E+05, 1.470037772382250E+08, 6.902310019117594E+04
VX, VY, VZ =-2.981307068964254E+01, -1.862261642601049E+00, -1.189866198980569E-01

r0 = np.array([X, Y, 0.0])
v0 = np.array([VX, VY, 0.0])

a = -np.abs(np.arcsin(X/np.sqrt(X**2+Y**2)))

print(a, a*180/np.pi) # imprimim l'angle que rotarem el SR

ez = np.array([0.0, 0.0, 1.0])

# el nou r0 i v0 calculats amb la formula de Rodrigues

rr0 = r0*np.cos(a) + np.cross(ez, r0)*np.sin(a) + ez*(ez@r0)*(1-np.cos(a))
vv0 = v0*np.cos(a) + np.cross(ez, v0)*np.sin(a) + ez*(ez@v0)*(1-np.cos(a))

