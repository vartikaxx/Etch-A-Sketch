from turtle import Turtle,Screen

myturtle=Turtle()
screen = Screen()

def move_forward():
    myturtle.forward(10)

def move_backward():
    myturtle.backward(10)

def move_left():
    left = myturtle.heading()+10
    myturtle.setheading(left)

def move_right():
    right=myturtle.heading()-10
    myturtle.setheading(right)

def clear():
    myturtle.clear()
    myturtle.penup()
    myturtle.home()
    myturtle.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()