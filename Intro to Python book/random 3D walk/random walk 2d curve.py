import random
import math
import matplotlib.pyplot as plt


def angle():
    x = random.uniform(0.0001, 1.0001) * 2 * math.pi
    return x


def randomDirection():
    # generates a random angle Uses the random() function to generate a random angle
    randomNo = random.random()
    angle = 2 * randomNo * math.pi
    return angle


n = eval(input("Input number of blocks: "))
x_axis = 0.0
y_axis = 0.0
path = []


for i in range(n + 1):
    path.append(tuple((x_axis, y_axis)))
    x_axis = x_axis + math.cos(angle())
    y_axis = y_axis + math.sin(angle())


# print(path)
print("(", x_axis, ",", y_axis, ")")
print("Steps from origin", abs(x_axis) + abs(y_axis))
x_val = [x[0] for x in path]
y_val = [x[1] for x in path]

plt.title("Random Curve")

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x_val, y_val)
plt.plot(x_val, y_val, "or")
plt.show()
