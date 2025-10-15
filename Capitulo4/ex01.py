import turtle

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

if __name__ == "__main__":
    bob = turtle.Turtle()
    bob.color("Red")
    bob.shape("turtle")
    square(bob)
    turtle.mainloop()