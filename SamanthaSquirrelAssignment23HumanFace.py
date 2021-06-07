#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 23 Human face

import time

from graphics import *

def main():
    win = GraphWin("My circle", 200, 200)

    #Head
    head = Circle(Point(100, 100), 50)
    head.draw(win)
    head.setFill("yellow")

    #Eyes
    p1 = Point(80, 90)
    p2 = Point(120, 90)
    p1.draw(win)
    p2.draw(win)
    
    #Mouth
    mouth = Oval(Point(140, 100), Point(60, 120))
    mouth.setFill("red")
    mouth.draw(win)

    #Ears
    ear1 = Circle(Point(40, 90), 20)
    ear1.draw(win)
    ear1.setFill("yellow")

    ear2 = Circle(Point(160, 90), 20)
    ear2.draw(win)
    ear2.setFill("yellow")

    #Text
    label = Text(Point(100, 40), 'A face')
    label.draw(win)
    
    win.getMouse()
    win.close
    
main()

time.sleep(3)
