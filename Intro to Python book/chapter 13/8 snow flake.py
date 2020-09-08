# import library
import turtle

# Declare and initialize a variable

koch_flake = "FRFRF"
iterations = 5
# Use for loop which iterate 5 times.

for i in range(iterations):
    # replace F with FLERFLF
    koch_flake = koch_flake.replace("F", "FLFRFLF")
    turtle.down()

# Use for loop to draw Koch_flakes.

for move in koch_flake:
    # use if statement to check value of move is F
    if move == "F":
        turtle.forward(100.0 / (3 ** (iterations - 1)))
    # use if statement to check value of move is L
    elif move == "L":
        turtle.left(60)
    # use if statement to check value of move is R
    elif move == "R":
        turtle.right(120)

exitonclick()
