#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 25 Lab Chapter 13 Programming Exercise 1

import tkinter

class AddressGUI:
    def __init__(self)
    #Creates the root widget
    self.mainWindow = tkinter.Tk()

    #Organize the main window into a top and bottom frame
    self.topFrame = tkinter.Frame()
    self.bottomFrame = tkinter.Frame()

    #Places a label in the top frame with a variable text
    self.info = tkinter.StringVar()
    self.addressLabel = tkinter.Label(self.top_frame, \
                                      textvariable=self.info, \
                                      width = 35)
    self.addressLabel.pack()

    #Create a Show Info button and a Quite button. Show info calls the
    #showInfo method

    self.showButton = tkinter.Button(self.bottomFrame, \
                                     text ='Show Info', comman=self.showInfo)
    self.quitButton = tkinter.Button(self.bottomFrame, text ='Quite', \
                                     commant=self.mainWindow.destroy)
    self.showButton.pack(side='left')
    self.quitButton.pack(side='left')

    self.topFrame.pack()
    self.bottom_frame.pack()

    #State the main loop
    tkinter.mainloop()

    #This method takes no argument besides self and returns nothing
    #It only sets the value of the info object to a name and address
    def showInfo(self):
        name = "Samantha Squirrel"
        address = "123 My House Road"
        city_state_zip = "Philadelphia, PA 19139"
        self.info.set(name + "\n" + address + "\n" + city_state_zip)

#Creat my ShowAddressGUI object
myAddress = ShowAddressGUI()
