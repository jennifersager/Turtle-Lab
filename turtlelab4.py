import turtle
import time
import random
turtle.showturtle()

#climbing a mountain
def Climbing(pencolor,pensize):
    turtle.shape("turtle")
    turtle.pencolor(pencolor)
    turtle.pensize(pensize)
    turtle.penup()
    turtle.goto(90,150)
    turtle.pendown()
    for i in range (4):
        #climb mountain
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.forward(30)
    turtle.pencolor("black")
    turtle.write("Hurray! Made it to the top!", align='right', font=('ariel', 16))

#swimming
def Swimming(pencolor,pensize):
    time.sleep(3)
    turtle.reset()
    turtle.penup()
    turtle.goto(-230,125)
    turtle.pendown()
    #draw pond
    turtle.shape("classic")
    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(70)
    turtle.end_fill()
    #draw path
    turtle.penup()
    turtle.goto(-230,118)
    turtle.pendown()
    turtle.shape("turtle")
    turtle.pencolor(pencolor)
    turtle.pensize(pensize)
    turtle.circle(90)
    #go swimming
    turtle.pencolor("blue")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(55)
    turtle.pencolor("black")
    turtle.write("Yeah! I'm swimming!", align='left', font=('ariel', 16))

#eating
def Eating():
    time.sleep(3)
    turtle.reset()
    turtle.shape("classic")
    vertical = -150
    color = ["red","blue","green","yellow"]
    turtle.penup()
    turtle.goto(-230,-150)
    turtle.pendown()
    #make food
    for count in range(4):
        turtle.pencolor(color[count])
        turtle.fillcolor(color[count])
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        vertical = vertical + 10
        turtle.penup()
        turtle.goto(-230,vertical)
        turtle.pendown()
    turtle.shape("turtle")
    vertical = -150
    turtle.penup()
    turtle.goto(-230,-150)
    turtle.pendown()
    #eat food
    for count in range(4):
        turtle.pensize(3)
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        vertical = vertical + 10
        turtle.penup()
        turtle.goto(-230,vertical)
        turtle.pendown()
        turtle.fillcolor("green")
        time.sleep(1)
    turtle.pencolor("black")
    turtle.write("Wow! What a great meal!", align='left', font=('ariel', 16))

#sleeping
def Sleeping():
    time.sleep(3)
    turtle.reset()
    turtle.shape("classic")
    turtle.penup()
    turtle.goto(200,-150)
    turtle.pendown()
    #make bed
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(230,-130)
    turtle.pendown()
    #make pillow
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(230,-180)
    turtle.pendown()
    #get in bed
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.shape("turtle")
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.write("Good Night!", align='right', font=('ariel', 16))

#main
def main():
    turtle.setup(800,600)
    print(Climbing("blue", 7))
    print(Swimming("pink", 3))
    print(Eating())
    print(Sleeping())
main()
    

$ git init
$ git status
$ git add .

        

        
