import sys
sys.path.append("..")

import torch
import numpy as np
import matplotlib.pyplot as plt
from animate import run_animation

X = torch.arange(-5, 5, 0.1).view(-1, 1)
Y = 3*(X**2) + 2*X + 1 + 0.4 * torch.randn(X.size())

# defining the function for forward pass for prediction
def forward(x):
    return w1 * (x**2) + w2*x + b

# evaluating data points with Mean Square Error (MSE)
def criterion(y_pred, y):
    return torch.mean((y_pred - y) ** 2)

w1 = torch.tensor(1.0, requires_grad=True)
w2 = torch.tensor(1.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)

step_size = 0.0005
loss_BGD = []
n_iter = 200

weights = []

for i in range (n_iter):
    # making predictions with forward pass
    Y_pred = forward(X)
    # calculating the loss between original and predicted data points
    loss = criterion(Y_pred, Y)
    # storing the calculated loss in a list
    loss_BGD.append(loss.item())
    # backward pass for computing the gradients of the loss w.r.t to learnable parameters
    loss.backward()
    # updateing the parameters after each iteration
    w1.data = w1.data - step_size * w1.grad.data
    w2.data = w2.data - step_size * w2.grad.data
    b.data = b.data - step_size * b.grad.data
    # zeroing gradients after each iteration
    w1.grad.data.zero_()
    w2.grad.data.zero_()
    b.grad.data.zero_()
    # priting the values for understanding
    weights.append([w1.item(), w2.item(), b.item()])
    # print('{}, \t{}, \t{}, \t{}'.format(i, loss.item(), w1.item(), b.item()))

print(weights[-1])
# w1, w2, b = weights[-1]
# y_pred = w1*(X**2) + w2*X + b
# y_pred = y_pred.detach().numpy()
# plt.style.use('seaborn')
# plt.scatter(X,Y, marker='+', c='red')
# plt.plot(X,y_pred,c='blue')
# plt.show()

run_animation(weights)