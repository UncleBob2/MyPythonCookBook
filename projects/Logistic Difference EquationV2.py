import random
import matplotlib.pyplot as plt

# x(n+1) = r * x(n) * (1-x(n))
# x = 0.5
# n <= 500
# r[1,4] in 1000 steps

r_start = 1
r_end = 4
scale_step = 1000
N = 500

results = [(0, 0.5)]
r_list = []


def logisticmap(r_value, n_result):
    r_value = r_value
    x = n_result
    return (r_value * x * (1 - x))


for r_value in range(r_start * scale_step, r_end * scale_step, 1):
    for i in range(1, N):
        tuplex = results[-1]
        prev_value = tuplex[1]
        new_value = logisticmap((r_value / scale_step), prev_value)
        results.append([i, new_value])
        r_list.append([(r_value / scale_step), new_value])


# xlist, ylist = zip(*results)
xlist, ylist = zip(*r_list)

plt.scatter(xlist, ylist, s=0.01)
plt.show()
