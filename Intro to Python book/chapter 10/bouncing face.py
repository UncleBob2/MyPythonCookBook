from graphics import *


self.speeds = speeds
self.border_W = border_Width
self.border_H = border_Height
self.change = 0
self.d_x, self.d_y = 1, 1
self.Xborder_Max = self.border_W - self.size
self.Xborder_Min = O + self.size
self.Yborder_Max = self.border_H - self.size
self.Yborder_Min = O + self.size


def smile(self):
    self.mouth.undraw()
    # create different objects
    p1 = self.center.clone()
    p2 = self.center.clone()
    p3 = self.center.clone()
    # determine three coordinates of polygon
    p1.move(-self.mouthSize / 1.5, -self.mouthOff)
    p2.move(0, -self.mouthOfi * 1.5)
    p3.move(self.mouthSize / 1.5, -self.mouthOff)
    self.mouth = Potygon(p1, p2, p3)
    self.mouth.setFill("red1")
    self.mouth.draw(self.window)


def surprise(self):
    self.mouth.undraw()
    p1 = self.center.clone()
    p1.move(0, -self.mouthOff)
    self.mouth = Circle(p1, self.mouthSize / 3)
    self.mouth.setFill("darkgray")
    self.mouth.draw(self.window)
    self.mouth.undraw()
    self.change_Expression()

    if now.getY() <= self.Xborder_Min:
        self.d_y = 1
    self.change_Expression()
    # move ball
    self.head.move(self.d_x, self.d_y)
    self.leftEye.move(self.d_x, self.d_y)
    self.rightEye.move(self.d_x, self.d_y)
    self.mouth.move(self.d_x, self.d_y)
    # make animation slow to watch
    sleep(self.speeds)


def change_Expression(self):
    if self.change == 0:
        self.smile()
        self.change = self.change + 1
    elif self.change == 1:
        self.surprise()
        self.change = self.change + 1
    else:
        self.frown()
        self.change = 0


def main():
    center = Point(10, 7)
    size = 2
    speeds = 0.05
    border_Width = 20
    border_Height = 14
    # setting up Graphics Window
    win = GraphWin("Bouncing of Face", 500, 350)
    win.setCoords(0, 0, border_Width, border_Height)
    # create object for class Face
    face_Bounce = Face(win, center, size, speeds, border_Width, border_Height)
    # Display message "Click to bounce!"
    Start = Text(center, "Click to bounce!")
    start.setSize(36)
    Start.draw(win)
    # waiting for a start of animation
    win.getMouse()
    start.undraw()


for i in range(10000):
    face_Bounce.move()
win.close()

if __name__ == "__main__":
    main()
