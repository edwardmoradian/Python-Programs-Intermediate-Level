# Description of Program: Create a Pet class that creates a pet object for which the user
# will input the name, type and age of the pet. Accessor methods are used to retrieve these attributes.
# Mutator methods are used to modify these attributes

class Pet():
    
    # the __init__ method accepts three arguments for the pet object - PetName, PetType and PetAge
    # This method intializes the attribtues all of which are private attributes
    
    def __init__(self, PetName, PetType, PetAge):
        self.__Name = PetName
        self.__Type = PetType
        self.__Age= PetAge
        
    # There are three mutator methods: SetName, SetType and SetAge
    # Mutator methods store a value in a data attribute or changes the value
    
    # SetName method accepts an argument for the pet's name
    def SetName(self, PetName):
        self.__Name = PetName
        
    # SetType method accepts an argument for the pet's type
    def SetType(self, PetType):
        self.__Type = PetType
    
    # SetAge method accepts an argument for the pet's age
    def SetAge(self, PetAge):
        self.__Age = PetAge
        
    # There are three accessor methods: GetName, GetType and GetAge
    # Accessor methods return a value from a class’s attribute but does not change it
    
    # GetName method returns the name of the pet
    def GetName(self):
        return self.__Name
    
    # GetType method returns the type of the pet
    def GetType(self):
        return self.__Type 
    
    # GetAge method returns the age of the pet
    def GetAge(self):
        return self.__Age
        
def Main():
    
    PetName = input("Enter your pet's name: ")
    PetType = input("Enter the type of animal your pet is: ")
    PetAge = input("Enter your pet's age: ")
    PetInstance = Pet(PetName,PetType,PetAge)
    
    print("\nHere is your entered pet's information:")
    print("Pet Name: ",PetInstance.GetName())
    print("Pet Type: ",PetInstance.GetType())
    print("Pet Age: ",PetInstance.GetAge())

Main()
    
        