import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# x = np.random.normal(-1, 1, 400)
# plt.hist(x)
# plt.show()

# figure, subplot


t = np.linspace(0, 6 * np.pi, 300)

x = np.cos(t)
y = np.sin(t)
z = t

fig = plt.figure("parametric curves")
sub = fig.add_subplot(111, projection="3d")
sub.plot(x, y, z)

plt.show()
