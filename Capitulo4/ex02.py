import turtle
def circle(t, r):
    """Desenha um círculo de raio r."""
    circumference = 2 * 3.14159 * r
    n = int(circumference / 3) + 1  # número de segmentos
    step_length = circumference / n
    step_angle = 360 / n
    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)




if __name__ == "__main__":
    bob = turtle.Turtle()
    bob.color("Green")
    bob.shape("turtle")
    circle(bob, 50)
    bob.penup()
    bob.goto(150, 0)
    bob.pendown()
    circle(bob, 100)
    turtle.mainloop()