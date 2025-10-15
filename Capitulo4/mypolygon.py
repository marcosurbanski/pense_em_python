import turtle
bob = turtle.Turtle()
print(bob)

bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

for i in range(4):
    bob.fd(100)
    bob.lt(90)
    bob.fd(50)
    bob.circle(10)
    bob.color("red")
    bob.speed(6)
    bob.shape("monkey")
    bob.color("blue")
turtle.mainloop()
