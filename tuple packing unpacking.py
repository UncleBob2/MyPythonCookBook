my_dic = {
    0: ("0.7162", "0.6957"),
    1: ("0.7927", "0.8256"),
    2: ("0.6409", "0.5615"),
    3: ("0.8976", "0.9602"),
    4: ("0.3584", "0.1489"),
    5: ("0.8968", "0.4942"),
    6: ("0.3610", "0.9749"),
    7: ("0.8996", "0.0956"),
    8: ("0.3522", "0.3371"),
    9: ("0.8898", "0.8714"),
}

for index in my_dic.keys():
    (var1, var2) = my_dic[index]  # tuple unpacking
    print(
        str(index)
        + "\t"
        + str("{:.1f}".format(float(var1) * 1000))
        + "\t"
        + str("{:.1f}".format(float(var2) * 1000))
    )

b = ("Bob", 19, "CS")  # tuple packing
(name, age, studies) = b  # tuple unpacking

print(name)
print(age)
print(studies)


print("==# tuples as return values   =====================")

import math


def circum_area(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)


print(circum_area(10))

print("=======================")
# Tuple assignment
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
(name, surname, bYear, movie, mYear, profession, birthplace) = julia

print(name)
print(surname)
print(bYear)
print(movie)
print(mYear)
print(profession)
print(birthplace)

