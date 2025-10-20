import turtle
from polygon import arc

def petal(t, r, angle):
    """Desenha uma pétala usando dois arcos."""
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle):
    """Desenha uma flor com n pétalas."""
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

def move(t, length):
    """Move a tartaruga para frente sem desenhar."""
    t.pu()
    t.fd(length)
    t.pd()

if __name__ == "__main__":
    bob = turtle.Turtle()
    bob.speed(0)

    # Flor 1
    move(bob, -100)
    flower(bob, n=7, r=60.0, angle=60.0)

    # Flor 2
    move(bob, 100)
    flower(bob, n=10, r=40.0, angle=-80.0)

    # Flor 3
    move(bob, 100)
    flower(bob, n=20, r=40.0, angle=-80.0)

    turtle.hideturtle()
    turtle.mainloop()
    