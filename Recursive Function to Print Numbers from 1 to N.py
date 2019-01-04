# Description of Program: Using Recursion to print the numbers from 1 to N

def Main():
    # Ask for the user input
    Num = int(input("Please enter an integer to print the integers from 1 to this integer: " ))
    
    print("The numbers from 1 to the integer inputted are:")
    
    PrintToInt(Num)
    
def PrintToInt(Num):
    if Num > 0:
        print(Num, end=" ")
        return PrintToInt(Num-1) # Do recursion untill Num reaches 1 
    
Main()