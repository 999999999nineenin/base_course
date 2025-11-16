import numpy as np
print('введите размерность массива:')
a=int(input())
b=int(input())
max=-999999999
print('заполните массив:')
c=np.zeros((a, b))
e=0
f=0
while a>e:
    f=0
    while b>f:
        d=int(input())
        c[e, f]=d
        f+=1
    e+=1
print(c)
g=0
h=0
while b>h:
    while a>g:
        if c[g, h]>max:
            max=c[g, h]
        g+=1
    print(max)
    h+=1
    g=0
    max=0