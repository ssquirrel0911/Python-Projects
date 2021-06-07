#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 25 Chapter 13 Programming Exercise 3

import tkinter

class MPGCalculatorGUI:
    def __init__(self):
        #Create the root widget
        self.main_window = tkinter.Tk()

        #Organize the window into 4 frames
        self.top_frame = tkinter.Frame()
        self.upper_mid_frame = tkinter.Frame()
        self.lower_mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #In the top frame we have a prompt and ext entry
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text='Number of gallons the car ' + \
                                          'holds:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        #In the upper middle frame there will be a prompt and a text entry
        self.prompt2_label = tkinter.Label(self.upper_mid_frame, \
                                           text='Miles car can drive on' + \
                                           'full tank:')
        self.miles_entry = tkinter.Entry(self.upper_mid_frame, width=10)
        self.prompt2_label.pack(side='left')
        self.miles_entry.pack(side='left')

        #The lower middle frame will have 2 labels; ArithmeticError one with text
        #The other text is dynamic
        self.describe_label = tkinter.:abe;(self.lower_mid_frame, text='MPG.')
        self.value = tkinet.StringVar()
        self.mpg_label = tkinter.label(self.lower_mid_frame, \
                                       textvariable=self.value)
        self.describe_label.pack(side='left')
        self.mpg_label.pack(side='left')

        #The bottom labal contains a convert button and a quit button
        self.calculate_button = tkinter.Button(self.bottom_frame, \
                                               text='Calculate', \
                                               command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame text='Quit',
                                          command=self.main_window.destroy)
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        #pack the frames
        self.top_frame.pack()
        self.upper_mid_frame.pack()
        self.lower_mid_frame.pack()
        self.bottom_frame.pack()

        #Start the main loop
        tkinter.mainloop()

    #This method calculates the MPG of car based on the gallons held
    #and miles drive on a full tank of gas
    def calculate(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        mpg = format(miles / gallons, ',.1f').rstip('0').rstrip('.')
        self.value.set(mpg)

#Create our MPGCalculatorGUI object
mpg_calculator = MPGCalculatorGUI()
