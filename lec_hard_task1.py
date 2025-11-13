import numpy as np
print("введите размерность массивов:")
a=int(input())
b=int(input())
c=np.zeros((a, b))
g=0
print("введите значения 1 массива:")
for i in range (2):
    d=0
    e=0
    while a>d:
        while b>e:
            c[d, e]=int(input())
            e+=1
        d+=1
        e=0
    if g==0:
        f=np.array(c)
        g+=1
        print("введите значения 2 массива:")
d=0
e=0
for i_1 in range(a*b):
    while a>d:
        while b>e:
            if c[d, e] > f[d, e]:
                f[d, e] = c[d, e]
            e+=1
        d+=1
print(f)