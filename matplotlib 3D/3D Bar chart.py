import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax1 = fig.add_subplot(111, projection="3d")

xpos = [1, 2, 3, 4, 9, 0, 0, 0, 0, 0]
ypos = [2, 3, 4, 7, 3, 0, 0, 0, 0, 0]
zpos = [5, 3, 8, 1, 9, 0, 0, 0, 0, 0]

dx = np.ones(10)  # the changes
dy = np.ones(10)
dy = np.ones(10)

ax1.bar3d(xpos, ypos, zpos, dx, dy, dx, color="#00ceaa")
ax1.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax1.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax1.set_zticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_zlim(0, 10)
ax1.set_xlabel("X axis")
ax1.set_ylabel("Y axis")
ax1.set_zlabel("Z axis")
plt.show()
