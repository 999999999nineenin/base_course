import numpy as np
from lec_task_module import speed_of_freefall as g
x0=50
y0=1500
t=0
v_0x=9
v_0y=18
for i in np.arange(0, 5, 0.01):
    x=x0+v_0x*t
    y=y0+v_0y*t-(g*(t**2))/2
    a=np.array(x)
    b=np.array(y)
    c=np.array(t)
    print(c, a, b)
    t+=0.01