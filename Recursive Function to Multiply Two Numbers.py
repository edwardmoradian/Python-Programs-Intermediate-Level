# Description of Program: Use Recursion to Multiply Two Nonnegative Numbers

def Main():
    # Ask for the user input
    Num1 = int(input("Please enter your first number: " ))
    Num2 = int(input("Please enter your second number: " ))
    Total = 0
    
    print()
    print("The two numbers multiplied by one another is: ", end= "")
    Multiply(Num1, Num2, Total)
    
    
def Multiply(Num1, Num2, Total):
    
    
    if Num1 > 0:
        Total += Num2
        return Multiply(Num1-1,Num2, Total)
    
    print(Total)
    
Main()