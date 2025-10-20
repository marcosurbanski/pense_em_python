import math
import turtle

def polygon(t, length, n):
    """Desnha um poligono regular com n lados."""
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Desenha um arco de círculo de raio r e ângulo 'angle' (em graus)."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle / 2)
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    t.rt(step_angle / 2)

def circle(t, r):
    """Desenha um círculo completo de raio r."""
    arc(t, r, 360)