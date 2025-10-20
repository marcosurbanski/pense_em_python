import turtle
import math

def polyline(t, n, length, angle):
    """Desenha n segmentos de reta."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Desenha um arco com raio r e ângulo em graus."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = angle / n

    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def isosceles(t, r, angle):
    """Desenha uma fatia de torta (triângulo isósceles)."""
    y = r * math.sin(math.radians(angle / 2))
    t.rt(angle / 2)
    t.fd(r)
    t.lt(90 + angle / 2)
    t.fd(2 * y)
    t.lt(90 + angle / 2)
    t.fd(r)
    t.lt(180 - angle / 2)

def pie(t, n, r):
    """Desenha uma torta de n fatias com raio r."""
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle)
        t.lt(angle)

# Exemplo de uso
bob = turtle.Turtle()
bob.speed(0)
pie(bob, 8, 100)  # 8 fatias

turtle.done()
