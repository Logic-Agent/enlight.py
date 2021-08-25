# *****************************************************
# * Complication: 
# * Execution: 
# * 
# * @author: Jiaxu Hu
# * Date: 2021/6/14 7:20
# *
# *****************************************************
import turtle

def up(): #up
    yuyi.setheading(90)
    yuyi.forward(l)
def left(): #left
    yuyi.setheading(180)
    yuyi.forward(l)
def right(): #right
    yuyi.setheading(0)
    yuyi.forward(l)
def down(): #down
    yuyi.setheading(270)
    yuyi.forward(l)

def opdown(n):
    if n == 0:
        pass
    else:
        opleft(n - 1)
        up()
        opdown(n - 1)
        right()
        opdown(n - 1)
        down()
        opright(n - 1)

def opleft(n):
    if n == 0:
        pass
    else:
        opdown(n - 1)
        right()
        opleft(n - 1)
        up()
        opleft(n - 1)
        left()
        opup(n - 1)
def opright(n):
    if n == 0:
        pass
    else:
        opup(n - 1)
        left()
        opright(n - 1)
        down()
        opright(n - 1)
        right()
        opdown(n - 1)
def opup(n):
    if n == 0:
        pass
    else:
        opright(n - 1)
        down()
        opup(n - 1)
        left()
        opup(n - 1)
        up()
        opleft(n - 1)


level = int(input("level:"))
wn = turtle.Screen()
yuyi = turtle.Turtle()
l=2**(8-level)

if level >= 5:
    yuyi.speed(10)

if level//2:
    opdown(level)
else:
    opleft(level)

wn.exitonclick()