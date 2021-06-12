import turtle
import os
import random
from random import choice



"""setting up the screen"""
win = turtle.Screen()
win.bgcolor("black")
win.title('space-invaders')
win.screensize(800,800)


"""Drawing the border"""
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('pink')
border_pen.penup()
border_pen.setposition(-380, -380)
border_pen.pendown()
#border_pen.goto(-300,-250) 
border_pen.pensize(3)
for x in range(4):
    border_pen.forward(750)
    border_pen.left(90)
border_pen.hideturtle()

"""player"""
player = turtle.Turtle()
colors = random.choice(['red', 'blue', 'green'])
player.color(colors)
player.setheading(90)
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -300)


"""creting the INVADERS"""
invader = turtle.Turtle()
invader.color('red')
invader.shape("circle")
invader.shapesize(0.50,0.50)
invader.penup()
invader.speed(0)
invader.setposition(-300,300)
invaderspeed = 2
invader.setheading(135)



"""player's armor"""
defense = turtle.Turtle()
defense.color('yellow')
defense.shape('triangle')
defense.penup()
defense.speed(0)
defense.setheading(90)
defense.shapesize(0.50, 0.50)
defense.hideturtle()

defensespeed = 30
"""defining state"""
#ready 
#fire 
defensestate = "ready"

"""functions for moving the players"""
playerspeed = 20
def goto_left():
    x = player.xcor()
    x -= playerspeed
    """boundary checking"""
    if x< -355:
        x = -355
    player.setx(x)
def goto_right():
    x = player.xcor()
    x += playerspeed
    """boundary checking"""
    if x> 355:  
        x =355
    player.setx(x)

"""function for firing"""
def fire_defense():
    global defensestate
    if defensestate == "ready":      #if its state is ready then its going to fire.
        defensestate = "fire"
        """move the defense just above the player"""
        x = player.xcor()
        y = player.ycor()
        defense.setposition(x, y+10)
        defense.showturtle()

"""For keyboard bindings"""
turtle.listen()
turtle.onkeypress(goto_left, "Left")
turtle.onkeypress(goto_right, "Right")
turtle.onkeypress(fire_defense, "space")


"""Main game loop area"""
while True:
    #moving the invaders"""
    x= invader.xcor()
    x += invaderspeed 
    invader.setx(x)


    """moving the invader back and down & boundary checking"""
    if invader.xcor() > 355: 
        y = invader.ycor()
        y -= 40 
        invaderspeed *= -1
        invader.sety(y)

    if invader.xcor() < -355:
        y = invader.ycor()
        y -= 40
        invaderspeed *= -1
        invader.sety(y)



    """move the defense"""
    if defensestate == "fire":
        y = defense.ycor()
        y += defensespeed
        defense.sety(y)










delay = input("enter to enter to close the screen")