import numpy as np
import matplotlib.pyplot as plt

r_0 = 149597870.7 # 1 UA en km
GM = 132712440042 # El parametre solar en km^3/s^2
t_0 = np.sqrt(r_0**3/GM)/(86400*365.25636) # temps caracteristic en anys

t_final = 1/t_0 

dt = 0.001
N = int(np.round(t_final/dt)) # Nombre d'intervals

# condicions inicials, ja estan normalitzades pq estan en UA, i escollim que r_0 = 1 UA. La velocitat en canvi esta en UA/dia, passem a UA/any i després adimensionalitzem
x_0,y_0 = 1.686386301622458E-03, 9.826595562514578E-01

vx_0,vy_0 = -1.721848911038755E-02*365.25636*t_0,-1.075546096798359E-03*365.25636*t_0

x = [x_0]
y = [y_0]
vx = [vx_0]
vy = [vy_0]

for t in range(N+1): # apliquem el metode d'euler per components, reduint el problema de 2 EDOs de 2n ordre a un sistema de 4 EDOs de 1r ordre

    x_nou = x[t] + vx[t]*dt
    y_nou = y[t] + vy[t]*dt

    vx_nou = vx[t] - x[t]/(x[t]**2 + y[t]**2)**(3/2)*dt
    vy_nou = vy[t] - y[t]/(x[t]**2 + y[t]**2)**(3/2)*dt

    x.append(x_nou)
    y.append(y_nou)
    vx.append(vx_nou)
    vy.append(vy_nou)

plt.plot(x,y, color='black')

plt.axhline(0, color='gray', linestyle='-', linewidth=1.0)
plt.axvline(0, color='gray', linestyle='-', linewidth=1.0)

plt.scatter(0, 0, s=100, color='orange', zorder=2)

plt.grid(True, linestyle="--", linewidth=0.5)
plt.minorticks_on()
plt.tick_params(which='both', direction='in', right=True, top=True)
plt.xlabel("x (UA)",fontsize=14)  
plt.ylabel("y (UA)",fontsize=14)

plt.show()