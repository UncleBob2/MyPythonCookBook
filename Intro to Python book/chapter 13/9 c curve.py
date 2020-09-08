from turtle import right, left, forward, speed, exitonclick, hideturtle
import math

# Define function to draw pattern
def go(level, length):
    # Use if statement to execute statement according to value of level.
    if level <= 0:
        forward(length)
    else:
        right(45)
        # recursively call the same function
        go(level - 1, length / math.sqrt(2))
        left(90)
        # recursively call the same function
        go(level - 1, length / math.sqrt(2))
        right(45)


# define the speed of creating a pattern
speed(1000)
hideturtle()
right(90)
go(12, 100)

# click to exit

exitonclick()
