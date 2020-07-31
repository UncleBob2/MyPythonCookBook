import random
import matplotlib.pyplot as plt

# x(n+1) = r * x(n) * (1-x(n))
# x = 0.5
# n <= 500
# r[1,4] in 1000 steps


N = 500

results = [(0, 0.5)]


def logisticmap(run, n_result):
    r = 3
    x = n_result
    return (r * x * (1 - x))


for i in range(1, N):
    tuplex = results[-1]
    prev_value = tuplex[1]
    new_value = logisticmap(i, prev_value)
    results.append([i, new_value])


xlist, ylist = zip(*results)

plt.plot(xlist, ylist)
plt.show()
