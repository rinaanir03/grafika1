import turtle
import colorsys
def spiral():
    shape = turtle.Turtle()
    bg = turtle.Screen()
    bg.bgcolor("black")
    n = 36
    h = 0
    boki = eval(input("Wprowadz liczbe bokow:"))
    for i in range(361):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h += 1/n
        shape.color(c)
        shape.forward(i * 2/3 + i)
        shape.left(360/int(boki) + 1.50)
        shape.hideturtle()
        shape.pensize(2)
        shape.speed("fastest")

spiral()
turtle.exitonclick()