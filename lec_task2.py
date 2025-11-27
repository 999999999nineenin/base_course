import numpy as np


def func(a):
    s=a[0]
    for element in a:
        s*=element
    s=s/a[0]
    print(s)

test=np.array([2, 3, 5, 7, 11, 13, 17, 19])
func(test)