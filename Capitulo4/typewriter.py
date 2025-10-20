# typewriter.py moderno para Python 3
import turtle
from letters import *

def typewriter(text, t, start_x=-200, start_y=200, size=50, spacing=10):
    """
    Desenha o texto passado usando funções draw_x do letters.py
    text: string a ser desenhada
    t: objeto Turtle
    start_x, start_y: posição inicial da tartaruga
    size: tamanho da letra
    spacing: espaço entre letras
    """
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    for char in text.upper():
        if char == " ":
            t.penup()
            t.forward(size + spacing)
            t.pendown()
        else:
            func_name = f"draw_{char.lower()}"
            if func_name in globals():
                globals()[func_name](t)
            else:
                print(f"A função {func_name} não existe no letters.py")
            t.penup()
            t.forward(size + spacing)
            t.pendown()

# --- TESTE ---
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Typewriter - Think Python Adaptado")
    bob = turtle.Turtle()
    bob.speed(0)

    # Exemplo de texto
    typewriter("HELLO WORLD", bob)

    screen.mainloop()
