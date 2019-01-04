# Description of Program: This program uses a GUI to create a program to convert from kilometers to miles.
# The result is displayed in a label on the main window

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        
        # Create the main window
        self.main_window = tkinter.Tk()
        
        # Create three frames to group widgets - top, middle and bottom.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a distance in kilometers: ")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        
        # Pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")
        
        # Create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text = "Converted to miles:")
        
        # Create a StringVar object to associate with output label
        self.value = tkinter.StringVar()
        
        # Create a label and associate it with the StringVar object
        self.miles_label = tkinter.Label(self.mid_frame, textvariable = self.value)
        
        # Pack the middle frame's widgets
        self.descr_label.pack(side="left")
        self.miles_label.pack(side="left")
        
        # Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        
        # Pack the buttons
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # Enter the tkinter main loop
        tkinter.mainloop()
        
    # The convert method is a callback function for the Calculate function
    def convert(self):
        
        # Get the value entered by the user into the kilo_entry widget (by using the get method)
        kilo = float(self.kilo_entry.get())
        
        # Convert kilometers to miles
        miles = kilo * .6214
        
        # Convert miles to a string and store it in the StringVar object
        self.value.set(miles)
                
# Create an instance of the KiloConverterGUI class
kilo_conv = KiloConverterGUI()
        
# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 14
# =============================================================================

        
        
        
        
        
        
        
        
        
        
        
        