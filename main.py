from turtle import Turtle, Screen
import colorgram
import random


rgb_colors = [(194, 220, 237), (126, 182, 215), (48, 38, 20), (74, 99, 113), (113, 90, 56), (28, 43, 34), (30, 37, 42), (88, 81, 14), (40, 30, 34), (75, 91, 80), (95, 82, 87), (195, 152, 112), (176, 143, 24), (48, 75, 54), (234, 238, 237), (151, 201, 230), (87, 55, 46), (79, 141, 170), (240, 218, 201), (154, 141, 147), (75, 57, 61), (37, 72, 86), (146, 158, 153), (157, 117, 103), (119, 126, 140), (57, 63, 73), (155, 198, 229), (245, 191, 113), (137, 122, 129), (114, 136, 123)]
screen = Screen()
screen.colormode(255)
timmy = Turtle()


def extract_colors():
    colors = colorgram.extract('pexels-michael-block-3225517.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)


def draw_shape(n):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    for _ in range(n):
        angle = 360 / n
        timmy.color(r, g, b)
        timmy.pensize(10)
        timmy.forward(100)
        timmy.right(angle)


def draw_hirst_a_line():
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(50)


# for i in range(3, 11):
#     draw_shape(i)
# extract_colors()
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for _ in range(10):
    draw_hirst_a_line()
    # move back to the beginning spot and move up a line
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen.exitonclick()