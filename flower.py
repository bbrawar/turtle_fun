import turtle
i=0
while i<100:
    #turtle.position()
    turtle.pensize(i/10)
    turtle.forward(i)
    turtle.pencolor(i/100,i*i/10000,i*i*i/10**6)
    turtle.right(45)
    turtle.forward(i)
    turtle.circle(i,270)
    #turtle.forward(i)
    i+=1

