# Description of Program: Illustrate a recursive function by creating a program to calculate fractorial of a number

def Factorial(Number):
    if Number == 0:
        return 1 # In the base case of Number being 0, recursion is not needed
    else:
        return Number * Factorial(Number-1) # Use recursion to find factorial, returns value after recursions are finished

def Main():
    Number = int(input("Enter a nonnegative integer: "))
    
    Fact = Factorial(Number) # The user input is passed as the argument to the Factorial function
    
    print("The fractorial of " ,Number, " is ", Fact,".",sep="")

Main()

# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 13
# =============================================================================
