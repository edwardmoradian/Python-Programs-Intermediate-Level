# Description of Program: Create Labels in Two Different Frames

import tkinter

class MyGUI:
    def __init__(self):
        
        # Create the main window widget.
        self.MainWindow = tkinter.Tk()
        
        # Create two frames (frame objects), one for the top of the window, and one for the bottom.
        self.TopFrame = tkinter.Frame(self.MainWindow)
        self.BottomFrame = tkinter.Frame(self.MainWindow)
        
        # Create three Label widgets for the top frame
        self.Label1 = tkinter.Label(self.TopFrame, text = "First Label")
        self.Label2 = tkinter.Label(self.TopFrame, text = "Second Label")
        self.Label3 = tkinter.Label(self.TopFrame, text = "Third Label")
        
        # Pack the Labels that are in the top frame.
        # Using the top argument to stack each label on top of another inside the frame
        self.Label1.pack(side="top")
        self.Label2.pack(side="top")
        self.Label3.pack(side="top")
        
        # Create three Label widgets for the bottom frame
        self.Label4 = tkinter.Label(self.TopFrame, text = "Third Label")
        self.Label5 = tkinter.Label(self.TopFrame, text = "Fourth Label")
        self.Label6 = tkinter.Label(self.TopFrame, text = "Fifth Label")
        
        # Pack the Labels that are in the bottom frame.
        # Using the left argument to arrange the labels to the left of the frame
        self.Label4.pack(side="left")
        self.Label5.pack(side="left")
        self.Label6.pack(side="left")
        
        # Pack both the TopFrame and BottomFrame
        self.TopFrame.pack()
        self.BottomFrame.pack()
        
        # Enter the tkinter main loop
        tkinter.mainloop()

# Create an instance of the MyGUI class.
mygui = MyGUI()


# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 14
# =============================================================================


