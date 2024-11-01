import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Birthday Animation")

# Create turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("yellow")
pen.speed(2)

# Function to write Happy Birthday
def write_message(message, font_size, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.write(message, move=False, align="center", font=("Arial", font_size, "bold"))
    pen.penup()

# Animation of a cake
def draw_cake():
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.color("pink")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()
    pen.penup()

# Draw candles
def draw_candles():
    pen.goto(-80, 60)
    pen.color("blue")
    pen.begin_fill()
    pen.pendown()
    for _ in range(4):
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.penup()

# Animation with message
def birthday_animation():
    write_message("Happy Birthday!", 36, 0, 100)
    time.sleep(2)
    draw_cake()
    draw_candles()
    write_message("Have a wonderful year!", 24, 0, -200)

# Start animation
birthday_animation()

# Wait before closing the screen
time.sleep(5)
screen.bye()
