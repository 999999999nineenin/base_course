import numpy as np
a=input()


def func(a):
    if a=='круг':
        r=int(input())
        s=np.pi*(r**2)
        print(s)
    if a=='прямоугольник':
        b=int(input())
        c=int(input())
        s=b*c
        print(s)
    if a=='треугольник':
        d=int(input())
        h=int(input())
        s=(d*h)/2
        print(s)


func(a)


def area(figure, *arg):
    if figure=='circle':
        s=np.pi * arg[0]**2
    elif figure=='triangle':
        s=0.5 * arg[0] * arg[1]
    else:
        s=arg[0]**2
    return s
s_circle = area('triangle', 4, 7, 8)
print(s_circle)
