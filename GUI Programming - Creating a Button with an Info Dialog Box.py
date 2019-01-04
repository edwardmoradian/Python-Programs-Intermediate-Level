# Description of Program: Create a click button that has an info dialog box displayed when clicked.
# Also create a quit button to terminate program

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        
        # Create the main window widget.
        self.MainWindow = tkinter.Tk()
        
        # Create a Button widget. The text "Click Me" should appear on the button
        # the DoSomething method executes when the user clicks the button (this is the callback function)
        self.MyButton = tkinter.Button(self.MainWindow, text = "Click Me", command=self.DoSomething)
        
        # Create a Quit button
        # when this is clicked this calls the root widget's destroy method (this is the callback function)
        self.QuitButton = tkinter.Button(self.MainWindow, text="Quit", command = self.MainWindow.destroy)
        
        # Pack the Click Button and Quit Button.
        self.MyButton.pack()
        self.QuitButton.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()
        
    def DoSomething(self):
        
        # Display an info dialog box.
        tkinter.messagebox.showinfo("Response", "Thanks for clicking the button.")

# Create an instance of the MyGUI class.
mygui = MyGUI()

# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 14
# =============================================================================
