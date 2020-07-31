# Given two strings, write a function to decide if one is a permutation of the other
# https://www.youtube.com/watch?v=71UjBGz-o0w&list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg&index=2


# driving <= original
# drivign  <- permutation
# ddriving  not permutation
# riving    not permutation
# criving   not permutation
listA = ["driving", "criving", "ddriving", "riving", "drivign"]

# listA = [
#     "the cow jumps over the moon.",
#     "the moon jumps over the moon.",
#     "the moon jumps over the cow.",
#     "the cow  the moon. jumps over",
#     "jumps the cow over the moon.",
# ]

for i in range(len(listA)):
    if sorted(listA[i]) == sorted(listA[0]):
        print("permutation word with", listA[0], ":", listA[i])

