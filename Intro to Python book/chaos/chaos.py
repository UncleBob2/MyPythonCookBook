import random

""" k(x)(1 − x), where k is 3.9. """
x_initial = random.uniform(0, 0.9)
x_deviation = x_initial + 0.01
k = 3.9
my_dic = {}
print("\n\nA simple program illustrating chaotic behavior")
print(
    "Input: "
    + "\t"
    + str("{:.4f}".format(x_initial))
    + "\t"
    + "{:.4f}".format(x_deviation)
)
print("--------------------------------")


for index in range(0, 10):
    x_initial = k * x_initial * (1 - x_initial)
    x_deviation = k * x_deviation * (1 - x_deviation)
    my_dic[index] = ("{:.4f}".format(x_initial), "{:.4f}".format(x_deviation))
    print(
        index,
        "\t"
        + str("{:.4f}".format(x_initial))
        + "\t"
        + str("{:.4f}".format(x_deviation)),
    )


print("--------------------------------\n")

for index in my_dic.keys():
    (var1, var2) = my_dic[index]  # tuple unpacking
    print(
        str(index)
        + "\t"
        + str("{:.1f}".format(float(var1) * 1000))
        + "\t"
        + str("{:.1f}".format(float(var2) * 1000))
    )
