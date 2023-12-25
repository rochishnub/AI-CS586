import matplotlib.pyplot as plt
import numpy as np
import torch

from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')
fig, ax = plt.subplots()

X = torch.arange(-5, 5, 0.1).view(-1, 1)
Y = 3*(X**2) + 2*X + 1 + 0.4 * torch.randn(X.size())
y_start = 0 * torch.randn(X.size())

scat = ax.scatter(X,Y, marker='+', c='red')
line, = ax.plot(X, y_start, c='blue')


def animate(i, w):
    st = i % len(w)
    w2, w1, b = w[st]
    y_new = w2*(X**2) + w1*X + b
    line.set_ydata(y_new)
    return line,

def run_animation(weights):
    ani = FuncAnimation(fig, animate, interval=50, blit=True, fargs=(weights,), save_count=len(weights))
    ani.save(f"SGD.gif", writer="pillow", dpi=200)