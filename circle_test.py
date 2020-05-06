# to run unittest need to run in python console
# must run in terminal
# C:\Users\Winsor\Desktop\python\MyCookBook>python -m unittest circle_test
import unittest
from circle import circle_area #original module before testing failures:
#from circle2 import circle_area #import filename: pythonUnitTests_circle
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5J)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius text")


