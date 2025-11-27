import numpy as np


def func(a):
    s=0
    for element in a:
        s+=element
    print(s/len(a))
    return s/len(a)


test = np.array([3, 8, 9, 34, 8])
func(test)