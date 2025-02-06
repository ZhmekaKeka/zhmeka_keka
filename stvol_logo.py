import turtle
import math


turtle.hideturtle()
turtle.speed(0)


c_inside_radius = 10
delta = 0.3
thickness = 0.18

c_outside_radius = 1.4 * c_inside_radius
web_1_radius = 2.24 * c_inside_radius
web_2_radius = 3.46 * c_inside_radius
pen_size = 0.1 * c_inside_radius


def inside_parts(radius):
    turtle.fd(radius * 0.5)
    turtle.right(90)
    turtle.fd(2 * radius * thickness)
    turtle.right(90)
    turtle.fd(radius * 0.5)


def outside_parts(radius):
    turtle.fd(radius * 2.78)
    turtle.right(90)
    turtle.fd(2 * radius * thickness)
    turtle.right(90)
    turtle.fd(radius * 2.78)


def web_part_between_315_360(radius):
    for angle in range(135, 180):
        x = radius * math.cos(math.radians(angle)) + (1 + 0.7) * radius
        y = radius * math.sin(math.radians(angle)) - 0.7 * radius
        turtle.goto(x, y)


def web_part_between_270_315(radius):
    for angle in range(90, 135):
        x = radius * math.cos(math.radians(angle)) + 0.7 * radius
        y = radius * math.sin(math.radians(angle)) - (1 + 0.7) * radius
        turtle.goto(x, y)


def web_part_between_225_270(radius):
    for angle in range(45, 90):
        x = radius * math.cos(math.radians(angle)) - 0.7 * radius
        y = radius * math.sin(math.radians(angle)) - (1 + 0.7) * radius
        turtle.goto(x, y)


def web_part_between_180_225(radius):
    for angle in range(0, 45):
        x = radius * math.cos(math.radians(angle)) - (1 + 0.7) * radius
        y = radius * math.sin(math.radians(angle)) - 0.7 * radius
        turtle.goto(x, y)


def web_part_between_135_180(radius):
    for angle in range(315, 360):
        x = radius * math.cos(math.radians(angle)) - (1 + 0.7) * radius
        y = radius * math.sin(math.radians(angle)) + 0.7 * radius
        turtle.goto(x, y)


def web_part_between_90_135(radius):
    for angle in range(270, 315):
        x = radius * math.cos(math.radians(angle)) - 0.7 * radius
        y = radius * math.sin(math.radians(angle)) + (1 + 0.7) * radius
        turtle.goto(x, y)


def web_part_between_45_90(radius):
    for angle in range(225, 270):
        x = radius * math.cos(math.radians(angle)) + 0.7 * radius
        y = radius * math.sin(math.radians(angle)) + (1 + 0.7) * radius
        turtle.goto(x, y)


def web_part_between_0_45(radius):
    for angle in range(180, 225):
        x = radius * math.cos(math.radians(angle)) + (1 + 0.7) * radius
        y = radius * math.sin(math.radians(angle)) + 0.7 * radius
        turtle.goto(x, y)


def web_clockwise(radius):

    turtle.penup()
    turtle.goto(radius, 0)
    turtle.pendown()

    web_part_between_315_360(radius)
    web_part_between_270_315(radius)
    web_part_between_225_270(radius)
    web_part_between_180_225(radius)
    web_part_between_135_180(radius)
    web_part_between_90_135(radius)
    web_part_between_45_90(radius)
    web_part_between_0_45(radius)


#  Буква С
## Внутренний радиус
turtle.begin_fill()
turtle.penup()
x = c_inside_radius * math.cos(math.radians(30))
y = c_inside_radius * math.sin(math.radians(30))
turtle.goto(x, y)
turtle.pendown()


start = 30
end = round(math.degrees(math.acos(thickness)))
for angle in range(start, end):
    x = c_inside_radius * math.cos(math.radians(angle))
    y = c_inside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

turtle.right(90)
inside_parts(c_inside_radius)
turtle.right(90)


start = round(math.degrees(math.acos(-thickness)))
end = 180 + round(math.degrees(math.asin(-thickness)))
for angle in range(start, end):
    x = c_inside_radius * math.cos(math.radians(angle))
    y = c_inside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

inside_parts(c_inside_radius)
turtle.right(180)


start = 180 + round(math.degrees(math.asin(thickness)))
end = 180 + round(math.degrees(math.acos(thickness)))
for angle in range(start, end):
    x = c_inside_radius * math.cos(math.radians(angle))
    y = c_inside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

turtle.left(90)
inside_parts(c_inside_radius)
turtle.left(90)


start = 180 + round(math.degrees(math.acos(-thickness)))
end = 330
for angle in range(start, end):
    x = c_inside_radius * math.cos(math.radians(angle))
    y = c_inside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

x = c_outside_radius * math.cos(math.radians(330))
y = c_outside_radius * math.sin(math.radians(330))
turtle.goto(x, y)

## Внешний радиус
start = 330
end = 180 + round(math.degrees(math.acos(-thickness / (1.4 + delta))))
for angle in range(start, end, -1):
    x = c_outside_radius * math.cos(math.radians(angle))
    y = c_outside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

turtle.right(90)
outside_parts(c_inside_radius)
turtle.right(90)


start = 180 + round(math.degrees(math.acos(thickness / 1.4)))
end = 180 + round(math.degrees(math.asin(thickness / (1.4 + delta))))
for angle in range(start, end, -1):
    x = c_outside_radius * math.cos(math.radians(angle))
    y = c_outside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

turtle.right(180)
outside_parts(c_inside_radius)


start = 180 + round(math.degrees(math.asin(-thickness / 1.4)))
end = round(math.degrees(math.acos(-thickness / (1.4 + delta))))
for angle in range(start, end, -1):
    x = c_outside_radius * math.cos(math.radians(angle))
    y = c_outside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

turtle.left(90)
outside_parts(c_inside_radius)
turtle.left(90)


start = round(math.degrees(math.acos(thickness / 1.4)))
end = 30
for angle in range(start, end, -1):
    x = c_outside_radius * math.cos(math.radians(angle))
    y = c_outside_radius * math.sin(math.radians(angle))
    turtle.goto(x, y)

x = c_inside_radius * math.cos(math.radians(30))
y = c_inside_radius * math.sin(math.radians(30))
turtle.goto(x, y)

turtle.end_fill()

# Паутина
## Перекрестие
turtle.penup()
x = c_inside_radius * math.cos(math.asin(thickness)) - c_inside_radius * 0.5
y = c_inside_radius * math.sin(math.asin(thickness))
turtle.goto(x, y)

turtle.pendown()

turtle.begin_fill()
turtle.fd(c_inside_radius * 3.6)
turtle.right(90)
turtle.fd(2 * c_inside_radius * thickness)
turtle.right(90)
turtle.fd(c_inside_radius * 3.6)
turtle.right(90)
turtle.fd(2 * c_inside_radius * thickness)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.pensize(pen_size)

x = 4 * c_inside_radius * math.cos(math.radians(45))
y = 4 * c_inside_radius * math.sin(math.radians(45))
turtle.goto(x, y)

turtle.goto(0, 0)
x = 4 * c_inside_radius * math.cos(math.radians(3 * 45))
y = 4 * c_inside_radius * math.sin(math.radians(3 * 45))
turtle.goto(x, y)

turtle.goto(0, 0)
x = 4 * c_inside_radius * math.cos(math.radians(5 * 45))
y = 4 * c_inside_radius * math.sin(math.radians(5 * 45))
turtle.goto(x, y)

turtle.goto(0, 0)
x = 4 * c_inside_radius * math.cos(math.radians(7 * 45))
y = 4 * c_inside_radius * math.sin(math.radians(7 * 45))
turtle.goto(x, y)

## Соединительные
web_clockwise(web_1_radius)
web_clockwise(web_2_radius)

turtle.exitonclick()  # закрытие окна с рисунками по клику
