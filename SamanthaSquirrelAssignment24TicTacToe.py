#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 24 tic tac toe

from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

import time

buttonClick = True

def checkButtons(buttons):
    #Global click for the user to click the squares for their shape
    global buttonClick
    if buttons['text'] == "" and buttonClick == True:
        buttons['text'] == "X"
        buttonClick = False
    elif buttons['text'] == "" and buttonClick == False:
        buttons['text'] = "O"
        buttonClick = True

    #Determines the turns for the players
    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
         button4["text"] == "X" and button4["text"] == "X" and button6["text"] == "X" or
         button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
         button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
         button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or                                                       
         button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
         button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X") :
         tkinter.messagebox.showinfo("X player is the winner", "Good job!")

    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button4["text"] == "O" and button4["text"] == "O" and button6["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or                                                       
         button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O") :
         tkinter.messagebox.showinfo("O player is the winner", "Good job!")

buttons=StringVar()

#Variables for input for squares
button1 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button1.grid(row=1, column=0,sticky = S+N+E+W)

button2 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button2.grid(row=1, column=1,sticky = S+N+E+W)

button3 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button3.grid(row=1, column=2,sticky = S+N+E+W)

button4 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button4.grid(row=1, column=0,sticky = S+N+E+W)

button5 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button5.grid(row=1, column=1,sticky = S+N+E+W)

button6 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button6.grid(row=1, column=2,sticky = S+N+E+W)

button7 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button7.grid(row=1, column=0,sticky = S+N+E+W)

button8 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button8.grid(row=1, column=1,sticky = S+N+E+W)

button9 = Button(tk,tect=" ",font=('Times 24 bold'), height = 4, width = 8, command=lambda:checker(button1))

button9.grid(row=1, column=2,sticky = S+N+E+W)

tk.mainloop()

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




         
time.sleep(3)
