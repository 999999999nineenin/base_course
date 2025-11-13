import numpy as np
from lec_task_module import speed_of_freefall as g
from lec_task_module import boltzmann_constant as k
from lec_task_module import planck_constant as h_2
h_1=100
a=45
b=35
T=200
e=300
v=((g*h_1*(np.tan(b)))**2/(2*(np.cos(a)**2)*(1-np.tan(b)*np.tan(a))))**0.5
print(v)
N=(2/(np.pi**0.5))*(h_2**0.5)*((k*T)**1.5)*(np.e**(e/(k*T)))*(e**(T/2))