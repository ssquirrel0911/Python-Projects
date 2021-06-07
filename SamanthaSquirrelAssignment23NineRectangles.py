#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 23 9 rectangles

import time

from graphics import *

mouseClick = True

def main():
    #Coordinates for window
    win = GraphWin("Grid", 300, 300)

    #Rectangles
    pt1 = Point(0, 100)
    rect1 = Rectangle(Point(100, 0), pt1)
    rect1.draw(win)
    pt2 = Point(0, 100)
    rect2 = Rectangle(Point(200, 0), pt2)
    rect2.draw(win)
    pt3 = Point(0, 100)
    rect3 = Rectangle(Point(300, 0), pt3)
    rect3.draw(win)
    pt4 = Point(0, 100)
    rect4 = Rectangle(Point(100, 200), pt4)
    rect4.draw(win)
    pt5 = Point(0, 100)
    rect5 = Rectangle(Point(200, 200), pt5)
    rect5.draw(win)
    pt6 = Point(0, 100)
    rect6 = Rectangle(Point(300, 200), pt6)
    rect6.draw(win)
    pt7 = Point(0, 100)
    rect7 = Rectangle(Point(100, 300), pt7)
    rect7.draw(win)
    pt8 = Point(0, 100)
    rect8 = Rectangle(Point(200, 300), pt8)
    rect8.draw(win)
    pt9 = Point(0, 100)
    rect9 = Rectangle(Point(200, 0), pt8)
    rect9.draw(win)

    #Texts
    number1 = Text(Point(50, 50), '1')
    number1.draw(win)
    number2 = Text(Point(150, 50), '2')
    number2.setFill("red")
    number2.draw(win)
    number3 = Text(Point(250, 50), '3')
    number3.draw(win)
    number4 = Text(Point(50, 150), '4')
    number4.setFill("red")
    number4.draw(win)
    number5 = Text(Point(150, 150), '5')
    number5.draw(win)
    number6 = Text(Point(250, 150), '6')
    number6.setFill("red")
    number6.draw(win)
    number7 = Text(Point(50, 250), '7')
    number7.draw(win)
    number8 = Text(Point(150, 250), '8')
    number8.setFill("red")
    number8.draw(win)
    number9 = Text(Point(250, 250), '9')
    number9.draw(win)


main()

