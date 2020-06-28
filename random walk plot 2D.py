import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import random


x_axis = 0
y_axis = 0

XY_cord = [(0, 0)]


def walk(x_ax, y_ax):
    x = x_ax
    y = y_ax
    path = random.choice(['North', 'South', 'West', 'East'])
    if path == 'North':
        y = y + 1
    if path == 'South':
        y = y - 1
    if path == 'West':
        x = x + 1
    if path == 'East':
        x = x - 1
    return(x, y)


for x in range(10_000):
    result = walk(x_axis, y_axis)
    tuplex = XY_cord[-1]
    x_old = tuplex[0]
    y_old = tuplex[1]
    x_new = result[0] + x_old
    y_new = result[1] + y_old
    XY_cord.append([x_new, y_new])

    # D_1.append(D_1[-1] + result[1])

# print(XY_cord)
x, y = zip(*XY_cord)
plt.plot(x, y)
plt.show()
