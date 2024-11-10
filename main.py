import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from io import BytesIO


def calculate_cycloid_path(R, V, time_steps, num_points):
    t = np.linspace(0, time_steps, num_points)
    x = V * t - R * np.sin(V * t / R)
    y = R - R * np.cos(V * t / R)
    return x, y


R = float(input("Введите радиус колеса: "))
V = float(input("Введите скорость центра масс: "))
time_steps = 10
num_points = 500


x, y = calculate_cycloid_path(R, V, time_steps, num_points)


frames = []
for i in range(1, len(x), 10):
    plt.figure(figsize=(8, 6))
    plt.plot(x[:i], y[:i], '#fa93eb', label='Траектория точки на ободе')
    plt.plot(x[i-1], y[i-1], '#9b14de')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Траектория точки на ободе колеса (Шаг {i})')
    plt.legend()
    plt.grid()
    plt.xlim(0, max(x))
    plt.ylim(0, 2 * R)


    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames.append(imageio.imread(buf))
    plt.close()


gif_path = 'animation.gif'
imageio.mimsave(gif_path, frames, duration=0.1)


