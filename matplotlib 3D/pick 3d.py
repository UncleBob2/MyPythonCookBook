import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")


def on_pick(event, data):
    indexes = event.ind
    print(indexes)
    print(data[indexes, :])


# data = np.random.random([10, 3])
# ax.scatter(data[:, 0], data[:, 1], data[:, 2], picker=5)

xpos = [2, 5, 8, 0, 0, 0, 0, 0, 0, 0]
ypos = [2, 5, 8, 0, 0, 0, 0, 0, 0, 0]
zpos = [2, 5, 8, 0, 0, 0, 0, 0, 0, 0]
data = [xpos, ypos, zpos]
dx = np.ones(10)  # the changes
dy = np.ones(10)

dz = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color="red", picker=5)


fig.canvas.mpl_connect("pick_event", lambda event: on_pick(event, data))

ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_zticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

plt.show()
