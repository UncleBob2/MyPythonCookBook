import matplotlib.pyplot as plt
import numpy as np


def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e


# build up the numpy logo
structure = np.zeros((5, 5, 5), dtype=bool)
# structure (x,y,z)
structure[0, 0, :] = True
structure[-1, 0, :] = True
structure[1, 0, 2] = False
structure[2, 0, 1] = False
facecolors = np.where(structure, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(structure, '#BFAB6E', '#7D84A6')
filled = np.ones(structure.shape)

# upscale the above voxel image, leaving gaps
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)

# Shrink the gaps
x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
x[0::2, :, :] += 0.05
y[:, 0::2, :] += 0.05
z[:, :, 0::2] += 0.05
x[1::2, :, :] += 0.95
y[:, 1::2, :] += 0.95
z[:, :, 1::2] += 0.95

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)


# plt.title("Voxels Numpy Logo")
# ax.set_xticks([0, 1, 2, 3, 4, 5])
# ax.set_yticks([0, 1, 2, 3, 4, 5])
# ax.set_zticks([0, 1, 2, 3, 4, 5])
# ax.set_xlim(0, 5)
# ax.set_ylim(0, 5)
# ax.set_zlim(0, 5)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')

plt.show()
