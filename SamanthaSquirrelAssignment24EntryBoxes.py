#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 24 Lab Creating entry boxes

from graphics import *

import tkinter

class EntryBoxes:

    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()

        #Creates the 4 frames
        self.checkBox = tkinter.Frame(self.main_window)
        self.loadCode = tkinter.Frame(self.main_window)
        self.codeLoaded = tkinter.Frame(self.main_window)

        #Create and pack the widgets for check box
        self.checkBox_label = tkinter.Label(self.checkBox_frame,
                                            text = 'Enter yes to see if checkbox work')
        self.loadCode_label = tkinter.Label(self.loadCode_frame,
                                            text = 'Enter a python code you want to load')
        self.codeLoaded = tkinter.Label(self.codeLoaded_frame,
                                        text = 'A window might display?')
        #Create and pack the button widget
        self.checkButton = tkinter.Button(self.button_frame,
                                          text='Check',
                                          command=self.checkAnswer)
        self.LoadButton = tkinter.Button(self.button_frame,
                                          text = 'Load code',
                                          command=self.checkLoad)
        self.checkLoadButton = tkinter.Button(self.button_frame,
                                          text = 'Check code',
                                          command=self.checkCode)
        
        #Pack the frames
        self.checkBox_frame.pack()
        self.loadCode_frame.pack()
        self.codeLoad_frame.pack()
        self.button_frame.pack()


    #The checkAnswer method is callback for the checkBox widget
    def checkAnswer(self):
        self.checkBox = (self.checkBox_entry.get())
        self.loadCode = (self.loadCode_entry.get())
        self.codeLoaded = (self.codeLoaded_entry.get())

    entry_boxes = EntryBoxes()

time.sleep(3)
