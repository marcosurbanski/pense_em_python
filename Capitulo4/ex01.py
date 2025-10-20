import turtle

def square(t, length):
    for i in range(length):
        t.forward(100)
        t.left(90)

def polygon(t, length, n):
    for i in range(length):
        t.forward(200)
        t.left(90)
        t.left(360/n)

##os metodos acima coisas da minha cabeça hahahahah

def square_ai(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)
def polygon_ai(t, length, n):
    """Desenha um polígono regular com n lados."""
    angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

if __name__ == "__main__":
    bob = turtle.Turtle()
    bob.color("Red")
    bob.shape("turtle")
    square(bob, 5)
    bob.penup()
    bob.goto(180, 0)
    bob.pendown()
    polygon(bob, 200, 30)
    

    bob2 = turtle.Turtle()
    bob2.color("Blue")
    bob2.shape("circle")
    #bob2.speed(1)

    bob2.penup()
    bob2.goto(-200, -250)
    bob2.pendown()
    polygon_ai(bob2, 100, 5)
    bob2.penup()
    bob2.goto(-200, 0)
    bob2.pendown()
    polygon_ai(bob2, 80, 6)
    turtle.mainloop()