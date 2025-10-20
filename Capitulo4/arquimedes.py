import turtle

# Configuração da tela e da tartaruga
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Espiral de Arquimedes")

t = turtle.Turtle()
t.speed(0)  # máxima velocidade
t.color("blue")
t.pensize(2)

# Parâmetros da espiral
step = 1      # distância inicial
angle = 20    # ângulo de giro em graus
n_turns = 50  # número de passos (quanto maior, mais extensa a espiral)

# Desenhar a espiral
distance = 0
for i in range(n_turns):
    distance += step
    t.forward(distance)
    t.right(angle)

# Finalização
turtle.done()
