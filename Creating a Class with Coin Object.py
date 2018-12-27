# Description of Program: Simulate a coin toss with a Coin class
# A class is code that specifies the data attributes and methods for a particular type of object.
# Coin class has three methods: __init__, toss, get_sideup


import random

class Coin:
    
    # the self parameter is required for every method of a class - this references the specific object
    # that the method is supposed to operate on
    
    # __intit__ method is the initializer method that initializes the object's data attributes
    # Usually the first method in a class definition
    def __init__(self): 
        self.__sideup = "Heads"  
        # side up attribute is initialized with "Heads"
        # Has __ before it to make this attribute private so that only the Coin class has access to it and
        # cannot be changed in the Main function
    
    # create a toss method that randomly generates a number of either
    # 0 or 1. 0 is defined as Heads and 1 is defined as Tails     
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
            
    # create get_sideup method to return the value of sideup
    def get_sideup(self):
        return self.__sideup

def Main():
    
    MyCoin = Coin() # create an object from the coin class
    print('This side is up:', MyCoin.get_sideup()) # Display the side of the coin that is facing up which will be Heads
    
    # Toss the coin.
    print('I am tossing the coin...')
    MyCoin.toss()
        
    # Display the side of the coin that is facing up.
    print('This side is up:', MyCoin.get_sideup())

Main() # Call the main function.
    

# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 11
# =============================================================================
    
    
    
    
    
    
    
    
    