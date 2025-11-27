import numpy as np


def f(a, b, n):
    x=np.linspace(a, b, n)
    y=x**2
    return y


y=f(-10, 10, 100)
print(y)