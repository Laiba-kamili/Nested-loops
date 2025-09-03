import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")

my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 150
while True:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        my_wn.bgcolor("aqua")
        my_pen.forward(100)
        my_wn.bgcolor("sky blue")
        
turtle.done()