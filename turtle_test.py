import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.pensize(3)
t.pencolor("blue")

for i in range(4):
    t.forward(100)
    t.right(90)

screen.mainloop() 