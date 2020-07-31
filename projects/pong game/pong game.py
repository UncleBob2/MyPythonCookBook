import turtle
import os
import subprocess


current_path = os.path.dirname(__file__)  # Where your .py file is located
# resource_path = os.path.join(current_path, "Media")  # The resource folder path
# image_path = os.path.join(resource_path, "bubbles")  # The image folder path


print(os.getcwd())
print("current_path", current_path)
# print("resource_path", resource_path)
# print("image_path", image_path)


window = turtle.Screen()
window.title("Pong by Lala")
window.bgcolor("gray")
window.setup(width=800, height=600)
window.tracer()

# Score
score_a = 0
score_b = 0


# Paddle left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("aqua")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color("aqua")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# print('before mainloop')
# window.mainloop()
# print('after mainloop')


while True:
    window.update()

    # Move the ball
    ball.setx((ball.xcor()) + ball.dx)
    ball.sety((ball.ycor()) + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay out.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay out.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("afplay out.wav&")

        score_a += 1
        pen.clear()
        pen.write(
            "Player A: {}   Player B: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        os.system("afplay out.wav&")

        pen.clear()
        pen.write(
            "Player A: {}   Player B: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.setx(340)
        os.system("afplay out.wav&")
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.setx(-340)
        os.system("afplay out.wav&")
        ball.dx *= -1
