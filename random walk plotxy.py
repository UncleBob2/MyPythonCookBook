import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import random


x_axis = 0
y_axis = 0
D_1 = [0]


def walk(x_ax, y_ax):
    x = x_ax
    y = y_ax
    path = random.choice(['North', 'South', 'West', 'East'])
    if path == 'North':
        y = y + 1
    if path == 'South':
        y = y - 1
    return(x, y)


for x in range(1000):
    result = walk(x_axis, y_axis)
    D_1.append(D_1[-1] + result[1])

print(D_1)


plt.plot(D_1)
plt.show()

# fig, ax = plt.subplots()

# Path = mpath.Path
# path_data = [
#     (Path.MOVETO, (0, 0)),
#     (Path.MOVETO, (3, 4)),
#     (Path.MOVETO, (-3, 4)),
#     (Path.MOVETO, (-3, -5)),
#     (Path.MOVETO, (4, 4)),
# ]
# codes, verts = zip(*path_data)
# path = mpath.Path(verts, codes)
# patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
# ax.add_patch(patch)

# # plot control points and connecting lines
# x, y = zip(*path.vertices)
# line, = ax.plot(x, y, 'go-')

# ax.grid()
# ax.axis('equal')
# plt.show()
