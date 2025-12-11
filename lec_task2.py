import matplotlib.pyplot as plt
import numpy as np

def hyperbolla(k=1):
    x = np.linspace(int(input('введите предел:')), int(input('введите предел:')), int(input('введите кол-во точек:')))
    y = k / x
    plt.plot(x, y, color='g', label='my parabola', ms=1)
    plt.savefig('fig_5.png')

hyperbolla()