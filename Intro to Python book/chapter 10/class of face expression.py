"""
Program Plan:
* Define a class Face for drawing a default face on a screen.
* Define a method smile()which draw smile on a face.
* Define a method surprise() which gives surprised expression.
* Define a method frown()which gives frown expression.
* Define a class Button to draw buttons on screen for expressions and exit.
* Define a method setup_GUI()to set up a screen for playing a game.
* Define a method playing()which allows a user to click on a button to see different facial
expressions.
* Define a method main()to start a program.
* This method calls the playing() function.
"""
# Define a class Face provided in the question for drawing a default face on a screen. It will set up
# a face with both left and right eyes and head and mouth off.

# At first define three member variables self.center, self.size and self.window inside the constructor
# _init__() by the following lines:
from graphics import *


class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, ’Quit’) """
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """Returns true if button active and p is inside"""
        return (
            self.active
            and self.xmin <= p.getX() <= self.xmax
            and self.ymin <= p.getY() <= self.ymax
        )

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to ’active’."""
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to ’inactive’."""
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False


# required python3.6.8
class Face:
    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        p1 = center.clone()
        p1.move(-mouthSize / 2, -mouthOff)
        p2 = center.clone()
        p2.move(mouthSize / 2, -mouthOff)
        self.eyeSize = 0.15 * size
        self.eyeOff = size / 3.0
        self.mouthSize = 0.8 * size
        self.mouthOff = size / 2.0

        self.head = Circle(center, size)
        self.head.draw(window)

        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, eyeOff)
        self.leftEye.draw(window)

        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, eyeOff)
        self.rightEye.draw(window)

        self.mouth = Line(p1, p2)
        self.mouth.draw(window)

        self.center = center
        self.size = size
        self.window = window
        self.head.setFill("orange")
        self.leftEye.setFill("black")
        self.rightEye.setFill("black")

    def smile(self):
        self.mouth.undraw()
        # create different objects
        p1 = self.center.clone()
        p2 = self.center.clone()
        p3 = self.center.clone()
        # determine three coordinates of polygon
        p1.move(-self.mouthSize / 1.5, -self.mouthOff)
        p2.move(0, -self.mouthOff * 1.5)
        p3.move(self.mouthSize / 1.5, -self.mouthOff)
        # draw a polygon to show smile
        self.mouth = Polygon(p1, p2, p3)
        # fill red color in polygon
        self.mouth.setFill("red")
        self.mouth.draw(self.window)

    def surprise(self):
        self.mouth.undraw()
        p1 = self.center.clone()
        p1.move(0, -self.mouthOff)
        # draw a circle to show surprise expression
        self.mouth = Circle(p1, self.mouthSize / 3)
        self.mouth.setFill("darkgray")
        self.mouth.draw(self.window)

    def frown(self):
        self.mouth.undraw()
        # create different objects
        p1 = self.center.clone()
        p2 = self.center.clone()
        p3 = self.center.clone()
        p4 = self.center.clone()
        p1.move(-self.mouthSize / 1.5, -self.mouthOff)
        p2.move(0, -self.mouthOff * 0.6)
        p3.move(self.mouthSize / 1.5, -self.mouthOff)
        p4.move(0, -self.mouthOff * 0.4)
        self.mouth = Polygon(p1, p2, p3, p4)
        self.mouth.setFill("blue1")
        self.mouth.draw(self.window)


def main():
    win, x1, smile, surprise, frown, exit = setup_GUI()
    playing(win, x1, smile, surprise, frown, exit)
    win.close()


def setup_GUI():
    win = GraphWin("Expressions of Face", 300, 300)
    win.setCoords(0, 0, 100, 100)
    win.setBackground("lightgray")
    x1 = Face(win, Point(50, 60), 30)  # window, center(x,y), size
    sml_button = Button(win, Point(16.665, 7.5), 33, 15, "Smile")
    sml_button.activate()
    su_button = Button(win, Point(49.995, 7.5), 33, 15, "Surprise")
    su_button.activate()
    fr_button = Button(win, Point(83.325, 7.5), 33, 15, "Frown")
    fr_button.activate()
    e_button = Button(win, Point(90, 95), 15, 7, "Exit")
    e_button.activate()
    return win, x1, sml_button, su_button, fr_button, e_button


def playing(win, x1, smile, surprise, frown, exit):
    p = win.getMouse()

    while not exit.clicked(p):
        if smile.clicked(p):
            x1.smile()
        elif surprise.clicked(p):
            x1.surprise()
        elif frown.clicked(p):
            x1.frown()
        p = win.getMouse()


if __name__ == "__main__":
    main()
