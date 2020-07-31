# triangle.pyw
from graphics import *


def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 50.0, 50.0)
    message = Text(Point(5, 0.5), "Build a house")
    message.draw(win)
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)

    # Use Polygon object to draw the triangle
    #
    triangle = Polygon(p1, p2, p3, p4)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Get and draw three vertices of triangle
    p11 = win.getMouse()
    p11.draw(win)
    p21 = win.getMouse()
    p21.draw(win)
    p31 = win.getMouse()
    p31.draw(win)
    p41 = win.getMouse()
    p41.draw(win)

    # Use Polygon object to draw the triangle
    #
    triangle1 = Polygon(p11, p21, p31, p41)
    triangle1.setFill("peachpuff")
    triangle1.setOutline("cyan")
    triangle1.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()


main()
