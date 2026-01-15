import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

t = np.arange(0.01, 4*np.pi, 0.01)
R = 1

x = R * np.cos(t)
y = R * np.sin(t)
z = R * np.log10(t)

ax.plot(x, y, z, label='dich')

ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set(xlim3d=(-edge, edge), xlabel='X')
ax.set(ylim3d=(0, edge), ylabel='Y')
ax.set(zlim3d=(-edge, edge), zlabel='Z')

ax.legend()
ax.set_title('3D Test')

# plt.show()
plt.savefig('curve.png')