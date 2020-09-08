""" 
Define gui() window for regression line
Define module data_Process() to input the data
Define a module regress_line() to calculate regression line
main()
"""
from graphics import *


def gui():

    # set up graphics window for drawing a line

    win = GraphWin("Regression Line Program", 400, 300)
    win.setCoords(0, 0, 40, 30)
    win.setBackground(color_rgb(215, 215, 215))

    lignt_grey = color_rgb(215, 215, 215)

    # draw bottom box

    box_pur_top = Rectangle(Point(0, 4), Point(40, 4.5))
    box_pur_top.setFill("black")
    box_pur_top.setWidth(0)
    box_pur_top.draw(win)
    box_pur_bottom = Rectangle(Point(0, 0), Point(40, 4))
    box_pur_bottom.setFill("purple")
    box_pur_bottom.setWidth(0)
    box_pur_bottom.draw(win)
    # box for writing description
    box_Text = Text(Point(18.5, 2.75), "Regression Line Program")

    box_Text.setFace("times roman")
    box_Text.setSize(11)
    box_Text.setTextColor("black")
    box_Text.draw(win)

    box_Text2 = Text(
        Point(23.20, 1), "Click inside to get point and click DONE for finish."
    )
    box_Text2.setFace("times roman")
    box_Text2.setSize(7)
    box_Text2.setTextColor("black")
    box_Text2.draw(win)

    # draw a button
    button_Border = Rectangle(Point(0.5, 0.4), Point(9.5, 3.7))
    button_Border.setFill("grey")
    button_Border.draw(win)
    button = Rectangle(Point(0.75, 0.65), Point(9.25, 3.5))
    button.setFill(lignt_grey)
    button.draw(win)
    button_Text = Text(Point(5, 2), "Done")
    button_Text.setFace("times roman")
    button_Text.setSize(12)
    button_Text.setTextColor("black")
    button_Text.draw(win)

    # Draw the X-axes and Y-axes with the points indicating on them.
    # draw x and y axes with indicator of points

    # indicationg 5 points for 1 bar
    Line(Point(2, 6.5), Point(2, 28)).draw(win)
    Line(Point(2, 6.5), Point(38, 6.5)).draw(win)

    # X axes points

    for i in range(36):  # 1 point
        Line(Point(i + 3, 6.25), Point(i + 3, 6.75)).draw(win)
    for i in range(0, 36, 5):  # Spoint
        Line(Point(i + 8, 6.05), Point(i + 8, 6.95)).draw(win)
    # Y axes points
    for i in range(21):  # 1point
        Line(Point(1.75, i + 7.5), Point(2.25, i + 7.5)).draw(win)
    for i in range(0, 21, 5):  # 5point
        Line(Point(1.55, i + 11.5), Point(2.45, i + 11.5)).draw(win)

    # If the mouse is not clicked inside a field then error will be raised or warning message.
    # display notification

    wam = Text(Point(20, 18), "to input data, click inside a field")
    wam.setSize(10)
    wam.setTextColor("red")
    # return back which will be used in main()
    return win, wam, button_Text


# Define a module data_Process()to input the data. First the points will be adjusting according to
# the center of the graphics axes and then the total number of points will be calculated. Then the
# total number of x points and y points should be calculated and the summation is to be done.


def data_Process(p_X, p_Y, num, x_Total, y_Total, xy_Sigma, x2):
    # adjust data with -2, -6.5 as the graph will span
    p_X = p_X - 2
    p_Y = p_Y - 6.5
    num = num + 1
    x_Total = x_Total + p_X
    y_Total = y_Total + p_Y
    xy_Sigma = xy_Sigma + (p_X * p_Y)
    x2 = x2 + p_X ** 2
    return num, x_Total, y_Total, xy_Sigma, x2

    # Define a module regress_Line{)to calculate the points through which the regression line will pass
    # through. Then the mean should be calculated for both x and y then the slope should be
    # calculated.


def regress_Line(num, x_Total, y_Total, xy_Sigma, x2, win):
    x_Mean = x_Total / num
    y_Mean = y_Total / num
    m = (xy_Sigma - (num * x_Mean * y_Mean)) / (x2 - (num * (x_Mean ** 2)))
    # Y position will found as per X = 0,36
    # IF the win.setCoords modified, this has to be
    # altered!!
    Y_min = y_Mean + m * (0 - x_Mean)
    Y_max = y_Mean + m * (36 - x_Mean)
    # Line should be drawn and pass though the maximum points coming to the way
    R_line = Line(Point(2, Y_min + 6.5), Point(38, Y_max + 6.5))
    R_line.draw(win)


# main() should be defined to set up a description text and warning messages to a user.


def main():
    win, warn, button_Text = gui()
    num, x_Total, y_Total, xy_Sigma, x2 = 0, 0, 0, 0, 0
    # Get the points from the window,
    while True:
        p = win.getMouse()
        p_X = p.getX()
        p_Y = p.getY()
        # if click is done inside a field then calculate
        # data
        if 38 >= p_X >= 2 and 28 >= p_Y >= 6.5:
            # warning should be reomoved if user click
            # appropriately
            warn.undraw()
            p.draw(win)

            num, x_Total, y_Total, xy_Sigma, x2 = data_Process(
                p_X, p_Y, num, x_Total, y_Total, xy_Sigma, x2
            )

        # if done button is clicked and data point > 2 then
        # line should be drawn
        elif num >= 2 and 9.5 >= p_X >= 0.5 and 3.7 >= p_Y >= 0.4:
            # warning should be reomoved if user click
            # appropriately
            warn.undraw()
            regress_Line(num, x_Total, y_Total, xy_Sigma, x2, win)
            break
        # if user click else
        else:
            # for second click it generates error if first
            # is not undraw
            warn.undraw()
            warn.draw(win)

            # click close to close
    button_Text.setText("Close")
    win.getMouse()


if __name__ == "__main__":
    main()
