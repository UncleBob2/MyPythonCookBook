import numpy as np
from matplotlib import pyplot as plt

# print(plt.style.available)

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38500, 42000, 46700, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# line format '[marker][line][color]
plt.bar(x_indexes - width, dev_y, width=width,
        color='r', linestyle='--', label='All Devs')


py_dev_y = [45372, 48876, 53850, 57285, 63016,
            65998, 70000, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width=width, label='Python')

java_dev_y = [38500, 45000, 46700, 49320, 57200,
              59000, 65316, 66928, 68317, 69748, 77752]

plt.bar(x_indexes + width, java_dev_y, color='#444444',
        linestyle='-', linewidth=3, width=width, label='Java')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.legend()  # refer to labels above
# plt.grid(True)
plt.tight_layout()
plt.savefig('plot.png')
plt.show()
