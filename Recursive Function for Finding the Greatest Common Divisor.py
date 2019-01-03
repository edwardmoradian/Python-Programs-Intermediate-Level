# Description of Program: Using recursion to find the greatest common divisor of two numbers

def GCD(x, y):
    if x % y == 0: # In the base case, when x mod y equals 0, the gcd is y.
        return y
    else:
        return GCD(x,x % y) # In the recursive case, we need this recursive call
    
def Main():
    
    # Ask the user for two different numbers
    Num1 = int(input("Enter you first integer: " ))
    Num2 = int(input("Enter your second integer: "))
    
    print()
    print("The greatest common divisor of your two numbers is ",GCD(Num1,Num2))
    
Main()

# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 13
# =============================================================================