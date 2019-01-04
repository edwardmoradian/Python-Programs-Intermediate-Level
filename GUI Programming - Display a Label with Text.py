# Description of Program: Display a label with text

import tkinter

class MyGUI:
    def __int__(self):
        
        # Create the main window widget.
        self.MainWindow = tkinter.Tk() 
        
        # Create a Label widget containing the text Hello World
        self.label = tkinter.Label(self.MainWindow, text="Hello World!") 
        
        # Call the Label widget's pack method.
        self.label.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()
        
# Create an instance of the MyGUI class.
mygui = MyGUI()


# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 14
# =============================================================================