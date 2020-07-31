import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


n = eval(input("Input number of blocks: "))
x_axis, y_axis, z_axis = 0, 0, 0
path = []
for i in range(n + 1):
    x = random.uniform(0.0001, 1.0001)
    path.append(tuple((x_axis, y_axis, z_axis)))
    # print(x)
    if x > 0.0001 and x <= 0.166666:
        y_axis -= 1
        # print("down")
    elif x > 0.166666 and x <= 0.333333:
        y_axis += 1
        # print("up")
    elif x > 0.333333 and x <= 0.5:
        x_axis -= 1
        # print("left")
    elif x > 0.5 and x <= 0.66666666:
        x_axis += 1
        # print("right")
    elif x > 0.6666666 and x <= 0.8333333:
        z_axis -= 1
        # print("down")
    else:
        z_axis += 1
        # print("up")


print(path)
print("(", x_axis, ",", y_axis, ",", z_axis, ")")

x_val = [x[0] for x in path]
y_val = [x[1] for x in path]
z_val = [x[2] for x in path]
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")
for x_v, y_v, z_v in zip(x_val, y_val, z_val):
    label = "(%d, %d, %d)" % (x_v, y_v, z_v,)
    ax.text(x_v, y_v, z_v, label)

plt.title("Random 3D")
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_yticks([0, 1, 2, 3, 4, 5])
ax.set_zticks([0, 1, 2, 3, 4, 5])
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.plot(x_val, y_val, z_val)
ax.plot(x_val, y_val, z_val, "or")
plt.show()
