# Description of Program: Convert Celsius to Fahrenheit

import tkinter
import tkinter.messagebox

class CelsiusConverterGUI:
    def __init__(self):
        
        # Create the main window
        self.main_window = tkinter.Tk()
        
        # Create three frames to group widgets - top, middle and bottom.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a temperature in Celsius: ")
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)
        
        # Pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.celsius_entry.pack(side="left")
        
        # Create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text = "Converted to Fahrenheit:")
        
        # Create a StringVar object to associate with output label
        self.value = tkinter.StringVar()
        
        # Create a label and associate it with the StringVar object
        self.celsius_label = tkinter.Label(self.mid_frame, textvariable = self.value)
        
        # Pack the middle frame's widgets
        self.descr_label.pack(side="left")
        self.celsius_label.pack(side="left")
        
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
        
        # Get the value entered by the user into the celsius_entry widget (by using the get method)
        celsius = float(self.celsius_entry.get())
        
        # Convert Celsius to Fahrenheit
        fahrenheit = (9/5) * celsius + 32
        
        # Convert Fahrenheit to a string and store it in the StringVar object
        self.value.set(fahrenheit)
                
# Create an instance of the CelsiusConverterGUI class
celsius_conv = CelsiusConverterGUI()
