# Description of Program: Using recursive functions to find the first 10 elements of a Fibonacci series

def Fibonacci(N):
    
    if N == 0: # There are two base cases with no recursion
        return 0
    elif N == 1:
        return 1 
    else:      # In the recursive case, the Fibonacci series is calculated as follows
        return Fibonacci(N-1) + Fibonacci(N-2)

def Main():
    print("The first 10 numbers in the Fibonacci series are: ")
    
    for Number in range(0,10):
        print(Fibonacci(Number))

Main()

# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 13
# =============================================================================
