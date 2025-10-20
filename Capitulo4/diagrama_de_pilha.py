import turtle
import math

# Função auxiliar para imprimir com indentação de "nível da pilha"
def log(msg, level):
    print("  " * level + msg)

# Função polygon
def polygon(t, length, n, level=0):
    log("→ Entrou em polygon()", level)
    log(f"  t = {t}", level)
    log(f"  length = {length}", level)
    log(f"  n = {n}", level)

    for i in range(n):
        log(f"    Loop {i+1}/{n}", level)
        t.fd(length)
        t.lt(360 / n)

    log("← Saindo de polygon()", level)

# Função circle
def circle(t, r, level=0):
    log("→ Entrou em circle()", level)
    log(f"  t = {t}", level)
    log(f"  r = {r}", level)

    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n

    log(f"  circumference = {circumference}", level)
    log(f"  n = {n}", level)
    log(f"  length = {length}", level)
    log("  Chamando polygon()", level)

    polygon(t, length, n, level + 1)

    log("← Saindo de circle()", level)

# Programa principal
bob = turtle.Turtle()
log("Criou a tartaruga 'bob'", 0)
circle(bob, 100, level=0)
turtle.mainloop()
