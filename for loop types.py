
colors = ["red", "green", "blue", "purple"]


for color in colors:
    print(color)

print(colors,"\n")

for i in colors:
    print(i)

# For example, let’s say we’re printing out president names along with their numbers (based on list indexes).
# range of length

print("\nrange len indexes example")
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
    print("President {}: {}".format(i + 1, presidents[i]))

print("\nenumerate example")
#Python’s built-in enumerate function allows us to loop over a list and retrieve
# both the index and the value of each item in the list:
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))

#Here we’re looping over two lists at the same time using indexes
# to look up corresponding elements:
print("\nUse indexes to look something up in another list.")
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))

#Python’s zip function allows us to loop over multiple lists at the same time without indexes:
print("\nUse zip instead of indexes to look something up in another list.")
colors = ["red", "purple", "green", "blue"]
ratios = [0.3, 0.1, 0.4, 0.2 ]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))