import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'projection' : '3d'})

phi = np.linspace(0, 6*np.pi, 100)
theta = np.linspace(0, 6*np.pi, 100)
l=1
m=1
n=1

x = np.outer(phi, np.cos(theta)) + l * theta
y = np.outer(phi, np.sin(theta)) + m * theta
z = np.outer(np.ones(len(phi)), theta) * n

ax.plot_surface(x, y, z)

plt.savefig('fig_6.png')