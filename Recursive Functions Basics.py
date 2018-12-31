# Description of Program: Illustration of a recursive function

# A recursive function is a function that calls itself
# Because it is recursive it must have some may to control the number of times it repeats

def Message(repetitions):
    if repetitions > 0:
        print("This is a recursive function.")
        Message(repetitions-1) # subtract 1 from repetitions to have only 5 repeats
    
def Main():
    Message(5) # Pass 5 as the argument to the function call to have 5 repeats of the function
               # The number of times a function repeats itself is called the depth of the function
    
Main()
