# letters.py
import turtle

# ---------- FUNÇÕES BASE ----------
def vertical(t, length):
    t.setheading(90)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length)

def horizontal(t, length):
    t.setheading(0)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length)

def diagonal(t, length, angle=45):
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length)

def semicircle(t, radius, extent=180):
    t.pendown()
    t.circle(radius, extent)
    t.penup()

# ---------- LETRAS ----------
def draw_a(t, size=50):
    start_pos = t.pos()
    t.setheading(75)
    t.pendown()
    t.forward(size)
    t.backward(size)
    t.setheading(105)
    t.forward(size)
    t.backward(size)
    t.setheading(0)
    t.forward(size / 2)
    t.backward(size / 2)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_b(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    semicircle(t, size/4, 180)
    t.goto(start_pos[0], start_pos[1]+size/2)
    semicircle(t, size/4, 180)
    t.penup()
    t.goto(start_pos[0] + size*0.6, start_pos[1])

def draw_c(t, size=50):
    start_pos = t.pos()
    t.goto(start_pos[0]+size, start_pos[1]+size)
    semicircle(t, size/2, 180)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_d(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    semicircle(t, size/2, 180)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_e(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    horizontal(t, size)
    t.goto(start_pos[0], start_pos[1]+size/2)
    horizontal(t, size*0.8)
    t.goto(start_pos[0], start_pos[1]+size)
    horizontal(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_f(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    horizontal(t, size)
    t.goto(start_pos[0], start_pos[1]+size/2)
    horizontal(t, size*0.8)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_g(t, size=50):
    start_pos = t.pos()
    t.goto(start_pos[0]+size, start_pos[1]+size)
    semicircle(t, size/2, 270)
    horizontal(t, size/2)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_h(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos[0]+size, start_pos[1])
    vertical(t, size)
    t.goto(start_pos[0], start_pos[1]+size/2)
    horizontal(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_i(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.penup()
    t.goto(start_pos[0] + size/2, start_pos[1])
    
def draw_j(t, size=50):
    start_pos = t.pos()
    t.goto(start_pos[0]+size/2, start_pos[1]+size)
    vertical(t, size)
    semicircle(t, size/4, 180)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_k(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos[0], start_pos[1]+size/2)
    diagonal(t, size/2, 45)
    t.goto(start_pos[0], start_pos[1]+size/2)
    diagonal(t, size/2, -45)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_l(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    horizontal(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_m(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    diagonal(t, size, 60)
    diagonal(t, size, -60)
    vertical(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_n(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    diagonal(t, size, 45)
    vertical(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_o(t, size=50):
    start_pos = t.pos()
    semicircle(t, size/2, 360)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_p(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    semicircle(t, size/4, 180)
    t.penup()
    t.goto(start_pos[0] + size*0.6, start_pos[1])

def draw_q(t, size=50):
    start_pos = t.pos()
    semicircle(t, size/2, 360)
    diagonal(t, size/4, -45)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_r(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos)
    semicircle(t, size/4, 180)
    diagonal(t, size/2, -45)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_s(t, size=50):
    start_pos = t.pos()
    semicircle(t, size/4, 180)
    t.goto(start_pos[0]+size/2, start_pos[1]+size/2)
    semicircle(t, size/4, -180)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_t(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos[0]-size/2, start_pos[1]+size)
    horizontal(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_u(t, size=50):
    start_pos = t.pos()
    vertical(t, size)
    t.goto(start_pos[0]+size, start_pos[1])
    vertical(t, size)
    semicircle(t, size/2, 180)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_v(t, size=50):
    start_pos = t.pos()
    diagonal(t, size, 60)
    diagonal(t, size, -60)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_w(t, size=50):
    start_pos = t.pos()
    diagonal(t, size, 60)
    diagonal(t, size, -60)
    diagonal(t, size, 60)
    diagonal(t, size, -60)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_x(t, size=50):
    start_pos = t.pos()
    diagonal(t, size, 45)
    diagonal(t, size, -45)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_y(t, size=50):
    start_pos = t.pos()
    diagonal(t, size/2, 45)
    diagonal(t, size/2, -45)
    t.goto(start_pos[0]+size/2, start_pos[1])
    vertical(t, size/2)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])

def draw_z(t, size=50):
    start_pos = t.pos()
    horizontal(t, size)
    t.goto(start_pos[0], start_pos[1]+size)
    diagonal(t, size, -45)
    horizontal(t, size)
    t.penup()
    t.goto(start_pos[0] + size, start_pos[1])
