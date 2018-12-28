# Demonstration of Inheritance of a subclass from its superclass of its methods and data attributes

# Description of Program: Create an automobile superclass to store general data about a car in the inventory
# For a program to store specific data about a car, we will write subclasses that inherit from the Automobile class

class Automobile: # Superclass Automobile
    
    # __init__ method accepts four  arguments - make, model, mileage and price of a car
    # Initializes these private attributes
    
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        
    # There are four mutator methods: SetMake, SetModel, SetMileage and SetPrice
    
    def SetMake(self, make):
        self.__make = make
        
    def SetModel(self, model):
        self.__model = model
    
    def SetMileage(self, mileage):
        self.__mileage = mileage
    
    def SetPrice(self, price):
        self.__price= price
        
    # There are four accessor methods: GetMake, GetModel, GetMileage, GetPrice
    
    def GetMake(self):
        return self.__make
    
    def GetModel(self):
        return self.__model
    
    def GetMileage(self):
        return self.__mileage
    
    def GetPrice(self):
        return self.__price
    
# Create a car subclass called Car that has the Automobile class as the superclass
# Create an attribute called doors that will be specific to each car
        
class Car(Automobile): # subclass Car inherits from the Automobile superclass 
                       # (methods inherited: make, model, mileage and price)
    
    def __init__(self, make, model, mileage, price, doors):
        
        # Call the superclass's __init__ method and pass the required arguments
        Automobile.__init__(self, make, model, mileage, price) 
        
        # initialize the __doors attribute
        self.__doors = doors
        
    # Mutator method for modifying value of doors
    def SetDoors(self, doors):
        self.__doors = doors
    
    # Accessor method for calling the value of doors
    def GetDoors(self):
        return self.__doors
    
# Call the Car class

def Main():
    
    UsedCar = Car('Audi', 2007, 12500, 21500.00, 4) # create an instance of the Car class with these attributes
    print('Make:', UsedCar.GetMake()) # use the accessor methods to get values of the attributes
    print('Model:', UsedCar.GetModel())
    print('Mileage:', UsedCar.GetMileage())
    print('Price:', UsedCar.GetPrice())
    print('Number of doors:', UsedCar.GetDoors())

Main()
    
    
# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 12
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    