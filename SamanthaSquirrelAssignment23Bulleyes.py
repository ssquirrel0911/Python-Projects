#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 23 Archery Target

import time

from graphics import *

def main():
    #Coordinates for window
    win = GraphWin("Grid", 400, 400)

    #BullEyes
    circle1 = Circle(Point(200, 200), 150)
    circle1.draw(win)
    circle1.setFill('white')
    
    circle2 = Circle(Point(200, 200), 125)
    circle2.draw(win)
    circle2.setFill('black')

    circle3 = Circle(Point(200, 200), 100)
    circle3.draw(win)
    circle3.setFill('blue')

    circle4 = Circle(Point(200, 200), 75)
    circle4.draw(win)
    circle4.setFill('red')

    circle5 = Circle(Point(200, 200), 50)
    circle5.draw(win)
    circle5.setFill('yellow')


main()

time.sleep(3)
