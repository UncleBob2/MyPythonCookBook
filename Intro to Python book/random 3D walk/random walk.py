import random
import matplotlib.pyplot as plt


n = eval(input("Input number of blocks: "))
x_axis, y_axis = 0, 0
path = []
for i in range(n + 1):
    x = random.uniform(0.0001, 1.0001)
    path.append(tuple((x_axis, y_axis)))
    # print(x)
    if x > 0.0001 and x <= 0.25001:
        y_axis -= 1
        # print("down")
    elif x > 0.25001 and x <= 0.5001:
        y_axis += 1
        # print("up")
    elif x > 0.5001 and x <= 0.75001:
        x_axis -= 1
        # print("left")
    else:
        # print("right")
        x_axis += 1
# print(path)
print("(", x_axis, ",", y_axis, ")")
print("Steps from origin", abs(x_axis) + abs(y_axis))
x_val = [x[0] for x in path]
y_val = [x[1] for x in path]
plt.plot(x_val, y_val)
plt.plot(x_val, y_val, "or")
plt.show()
