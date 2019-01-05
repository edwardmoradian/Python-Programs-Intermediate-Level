# Description of Program: Create a check button program
# Check buttons allow the user to select any or all of the buttons

import tkinter
import tkinter.messagebox

class MyGUI:
    
    def __init__(self):
        
        # Create the main window.
        self.main_window = tkinter.Tk()
        
        # Create two frames. One for the check buttons and another for the regular button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create three IntVar objects to use with the check button.
        # A different IntVar object is associated with each check button
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        
        # Set the intVar objects to 0 - this means that they are not selected for
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        
        # Create the check button widgets in the top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Option 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Option 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Option 3', variable=self.cb_var3)
        
        # Pack the check buttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        
        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        
        # Pack the buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Start the mainloop.
        tkinter.mainloop()
        
        # The show_choice method is the callback function for the Ok button
        
    def show_choice(self):
        
        # Create a message string.
        self.message = 'You selected:\n'
        
        # Determine which check buttons are selected and build the message string accordingly.
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'
        
        # Display the message in an info dialog box.
        tkinter.messagebox.showinfo('Selection', self.message)

# Create an instance of the MyGUI class.
my_gui = MyGUI()




# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 14
# =============================================================================
