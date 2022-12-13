import turtle
import random

turtle.title('Turtle Graphics by Little_R') #program name
turtle.colormode(255) #for rgb color mode
t = turtle.Pen()
t.shape('turtle')

def random_colors():
    color_list = []
    for i in range(3): #r,g,b
        c = random.randint(0,255)
        color_list.append(c)
    return tuple(color_list)

def hexagon():
    for i in range(6):
        t.speed(5) #drawing speed
        t.fd(100)
        t.left(60)

t.pencolor(random_colors())
for i in range(180):
        hexagon()
        t.left(2)
t.hideturtle()

turtle.mainloop()