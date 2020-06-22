from math import pi

def circle_area(r):
    return pi*(r**2)


# move these tests into circle_test
# # Test function with inputs within the list
# radii = [2,0,-3, 2+5j, True, "radius"]
# message = "Areas of circles with r = {radius} is {area}." # create a message format for each test display this message
#
# for r in radii:  #move over the list of radii
#     A = circle_area(r) #comput the area
#     print(message.format(radius=r, area=A)) # print the formatted message
