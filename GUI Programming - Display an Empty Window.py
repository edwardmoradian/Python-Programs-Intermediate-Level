# Description of Program: Display an empty window

import tkinter # import the tkinter module to create GUI programs

class MyGUI:
    def __init__(self):
        self.MainWindow = tkinter.Tk() # create a root widget and assign it to the class attribute MainWindow
        tkinter.mainloop() # execute the mainloop function of the tkinter module
        
# create an instance of the MyGUI class
mygui = MyGUI()


# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 14
# =============================================================================