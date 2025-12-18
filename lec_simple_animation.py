import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#Создание пространства и подпространства для анимации
fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2) #запятая создает кортеж или убирает внешние скобки
                         #linestyle, lineweight

x, y = [], [] #Координаты обьекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi) #пределы изменения переменной X
ax.set_ylim(-5, 5) #пределы изменения переменной Y

# функция подстановки параметра в обьект анимации
def update(frame):
    x.append(frame) #Расчет координаты X
    y.append(np.sin(frame)) #Расчет координаты Y

    #Передача координат обьекту анимации
    anim_object.set_data(x, y) #Подставляет значения в plt.plot

    return anim_object


ani = FuncAnimation(fig, #вызов пространства для анимации
                    update, #вызов функции подстановки координат
                    frames=frames_interval, #интервал значений
                    interval=50) #интервал между кадрами, по умолчанию 200 миллисекунд

ani.save('animation_1.gif', writer='pillow')