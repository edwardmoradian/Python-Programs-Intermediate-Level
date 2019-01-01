# Description of Program: The program sums the range of the elements of a predefined list

def RangeSum(NumList, Start, End):
    if Start > End:
        return 0 # If start is greater than end, then always return 0 (this is the base case)
    else:
        return NumList[Start] + RangeSum(NumList, Start + 1, End) # Add all elements from Start element to End element
                                                                  # This is the recursive case

def Main():
    Numbers = [1,2,3,4,5,6,7,8,9] # Predefined list
    
    MySum = RangeSum(Numbers, 2, 5) # Choosing the range of elements as 2 through 5 in the predefined list
    
    print("The sum of items 2 through 5 is", MySum)
    
Main()

# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 13
# =============================================================================
