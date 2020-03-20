from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def phi(x):
    return (x - 1) ** 2

def f(x, N, t):
    res = 0.0
    for n in range(1, int(N) + 1):
        Cn = integrate.quad(lambda x: phi(x) * np.sin(n * x), 0, np.pi)[0] * 2 / np.pi
        res += Cn * np.exp(-n * n * t * 0.1) * np.sin(n * x)
    return res

n_min = 0
n_max = 100
n_init = 1 
t_min = -1
t_max = 10
t_init = 0

cur_n = n_init
cur_t = t_init

x = np.linspace(-7, 7, 500)

fig = plt.figure(figsize=(13,8))

ax = plt.axes([0.1, 0.3, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.2, 0.8, 0.03])
slider_ax2 = plt.axes([0.1, 0.15, 0.8, 0.03])

ax.grid(True)
ax.axhline(y=0, color='k', linewidth=1)
ax.axvline(x=0, color='k', linewidth=1)
ax.axvline(x=np.pi, color='k', linewidth=1)

plt.sca(ax)
graph, = plt.plot(x, f(x, n_init, t_init), 'r')
plt.xlim(-1, 4)
plt.ylim(-1, 5)
plt.xlabel("X-coordinate")
plt.ylabel("Temperature")

n_slider = Slider(slider_ax, 'adds in series', n_min, n_max, valinit=n_init, valstep=1, valfmt="%d")
t_slider = Slider(slider_ax2, 'time', t_min, t_max, valinit=t_init, valstep=0.01, valfmt="%f")


def update_n(new_n):
    global cur_n
    cur_n = new_n
    graph.set_ydata(f(x, cur_n, cur_t)) 
    fig.canvas.draw_idle()          

def update_t(new_t):
    global cur_t
    cur_t = new_t
    graph.set_ydata(f(x, cur_n, cur_t)) 
    fig.canvas.draw_idle()
    

t_slider.on_changed(update_t)
n_slider.on_changed(update_n)

plt.show()