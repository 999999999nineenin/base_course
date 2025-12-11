import matplotlib.pyplot as plt
import numpy as np

n=tuple(input('введите кол-во точек:'))

def ellips(limit=10):
    x = (-2*limit, 2*limit, n)
    y = (-2*limit, 2*limit, n)

    X, Y = np.meshgrid(x, y)
    fxy = (x**2/a**2) + (y**2/b**2) - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')

    plt.savefig('fig_7.png')

ellips()
