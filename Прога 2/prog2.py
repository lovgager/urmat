from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

def f(x, a, t):
    if t == 0:
        y = []
        for i in x:
            if (i <= 1) and (i >= -1):
                y.append(1)
            else:
                y.append(0)
        return np.array(y)
    return (erf((x + 1) / (2 * a * np.sqrt(t))) - erf((x - 1) / (2 * a * np.sqrt(t)))) / 2

a_min = 0.01
a_max = 5
a_init = 1 
t_min = -1
t_max = 10
t_init = 0

cur_a = a_init
cur_t = t_init

x = np.linspace(-10, 10, 500)

fig = plt.figure(figsize=(13,8))

ax = plt.axes([0.1, 0.3, 0.8, 0.65])
slider_ax = plt.axes([0.1, 0.2, 0.8, 0.03])
slider_ax2 = plt.axes([0.1, 0.15, 0.8, 0.03])

ax.grid(True)
ax.axhline(y=0, color='k', linewidth=1)
ax.axvline(x=0, color='k', linewidth=1)


plt.sca(ax)
graph, = plt.plot(x, f(x, a_init, t_init), 'r')
plt.xlim(-5, 5)
plt.ylim(-2, 2)


a_slider = Slider(slider_ax, 'a', a_min, a_max, valinit=a_init, valstep=0.01, valfmt="%f")
t_slider = Slider(slider_ax2, 't', t_min, t_max, valinit=t_init, valstep=0.01, valfmt="%f")


def update_a(new_a):
    global cur_a
    cur_a = new_a
    graph.set_ydata(f(x, cur_a, cur_t)) 
    fig.canvas.draw_idle()          

def update_t(new_t):
    global cur_t
    cur_t = new_t
    graph.set_ydata(f(x, cur_a, cur_t)) 
    fig.canvas.draw_idle()
    

t_slider.on_changed(update_t)
a_slider.on_changed(update_a)

plt.show()