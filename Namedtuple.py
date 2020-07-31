from collections import namedtuple
# a good compromise between tuple and dictionary

color = {'red': 55, 'green': 155, 'blue': 255}

print('Using dictionary for color', color['red'])

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)
white = Color(255, 255, 255)

print('Using namedtuple for color', color[0])

print('Using namedtuple for color', color.red)  # making the code more readable
print(white.blue)
