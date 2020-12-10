import turtle , random

def star():
    ok.begin_fill()
    boyut = random.randint(10, 100)
    for i in range(5):
        ok.forward(boyut)
        ok.right(144)
    ok.end_fill()



pencere = turtle.Screen()
pencere.bgcolor("black")
pencere.setup(700, 500)

ok = turtle.Turtle()
ok.speed(0)
colors = ["red","blue","orange","green","yellow","gray","pink","purple","lime","cyan"]

for i in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    ok.penup()
    ok.setposition(x, y)
    ok.color(colors[i])
    ok.pendown()
    star()


turtle.mainloop()