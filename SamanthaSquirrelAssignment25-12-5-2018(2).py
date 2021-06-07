#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 25 Chapter 13 Programming Exercise 4

import tkinter

class TempConverterGUI:
    def __init__(self):
        #Create the root widget
        self.main_window = tkinter.Tk()

        #Organize the window into 3 frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #Promt the user for a Celsisus temperature and provide a texxt box
        #for the input
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text='Enter a temperature in Celsius:')
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)

        #Arrange the label and entry side by side
        self.prompt_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        #Create 2 labels, one to describe reult and one to display
        self.describe_label = tkinter.Label(self.mid_frame, text='Converted ' + \
                                            'to Fahrenheight:')
        self.value = tkinter.StringVar()
        self.fahrenheit_label = tkinter.label(self.mid_frame, \
                                              textvariable=self.value)

        #Pack these two labels side by side
        self.describe_label.pack(side='left')
        self.fahrenheit_label.pack(side='left')

        #Create two buttons one to calculate Fahrenheit
        #one to to quit
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', \
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
                                          command=self.main_window.destroy)

        #Pack these two buttons side to side
        self.calculate_button.pack(side='left')
        self.quit_button.pacl(side='left')

        #Pack the frames top to bottom
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #Initiate the main loop
        tkinter.mainloop()

    #Void function that converts Celsius to Fahrenheit
    def convert(self):
        celsius = float(Self.celsius_entry.get())
        fahrenheit = form(celsius * 9/5 + 32, ',.1f').rstrip('0').rstrip('.')
        self.value.set(fahrenheit)

temp_conv = TempConverterGUI()
