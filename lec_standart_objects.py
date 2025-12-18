from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')

frames = 720
coords = np.zeros((frames, 2)) #массив 180 на 2


def animate(i):
    coords[i] = circle_move(R=2, angle_vel=1, time=i)
    ball.set_data([coords[i][0]], [coords[i][1]])#текущая точка
    ball_line.set_data(coords[:i, 0], coords[:i, 1])#все точки от нулевой до текущей
    return ball, ball_line


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=frames, interval=30) #frames передается в функцию
ani.save('animation_2.gif', writer="pillow")