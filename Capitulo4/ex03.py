import turtle
import math

def circle(t, r):
    """Desenha um círculo completo de raio r."""
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1  # número de segmentos
    step_length = circumference / n
    step_angle = 360 / n
    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)

def arc(t, r, angle):
    """Desenha um arco de círculo de raio r e ângulo 'angle' (em graus)."""
    # comprimento da circunferência total
    circumference = 2 * math.pi * r
    # fração correspondente ao ângulo desejado
    arc_length = circumference * angle / 360
    n = int(arc_length / 3) + 1  # número de segmentos
    step_length = arc_length / n
    step_angle = angle / n
    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)

def arclength(radius, angle_radians):
    """Calcula o comprimento de um arco dado raio e ângulo (em radianos)."""
    return radius * angle_radians

if __name__ == "__main__":
    r = 5
    angle_rad = math.pi / 2  # 90 graus em radianos
    print(f"Arc length with radius {r} and angle {angle_rad} radians is {arclength(r, angle_rad)}")

    bob = turtle.Turtle()
    bob.color("green")
    bob.shape("turtle")

    # Círculo completo
    circle(bob, 50)

    # Move para o lado
    bob.penup()
    bob.goto(150, 0)
    bob.pendown()

    # Arco de 90 graus
    arc(bob, 100, 360)

    turtle.mainloop()
