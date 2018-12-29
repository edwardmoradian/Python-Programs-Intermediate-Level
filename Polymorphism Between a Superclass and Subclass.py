# Polymorphism allows subclasses and sueprclasses to have methods with the same names.
# It allows for the either of the methods to be called

# Description of Program: Illustrate polymorphism between a subclass and superclass
# Use of the isinstance function

# The Mammal class represents a generic mammal.

class Mammal: # Mammal is the superclass
    
    # __init__ method accepts the argument species for the type of species of the mammal
    def __init__(self,species):
        self.__species = species
        
    # ShowSpecies method displays the type of species of the mammal    
    def ShowSpecies(self):
        print("I am a", self.__species)
    
    # MakeSound method is the sound the mammal makes
    def MakeSound(self):
        print("Grrr!")
        
class Dog(Mammal): # Dog is the subclass of the Mammal superclass
    
    # The Dog subclass calls the Mammal superclass's __init__ method passing "Dog" as the argument for
    # the species
    def __init__(self):
        Mammal.__init__(self,"dog")
    
    # Method MakeSound is in both the superclass and subclass
    # In this case the subclass's MakeSound method overrides the superclass's MakeSound method
    # We need a dog to make a Woof sound and not a Grrr sound
    def MakeSound(self):
        print("Woof!")
        
# Can use this function to get mammal information if the object has these methods
# In other words, this method accepts an object as an argument and calls its ShowSpecies and MakeSound methods
def ShowMammalInfo(creature): 
    if isinstance(creature, Mammal): # use isinstance to determine if an object is an instance of a specified class
        creature.ShowSpecies()    
        creature.MakeSound()
    else:
        print("That is not a mammal.")
    
    
def Main():
    print("Here are some animals and the sounds they make.")
    print("------------------------------")
    
    MaxDog = Dog()
    MaxDog.ShowSpecies()
    MaxDog.MakeSound()
    
    print()
    MammalOne = Mammal("regular animal") # MammalOne is a Mammal object, pass regular animal as the species
    ShowMammalInfo(MammalOne)
    
    print()
    NotAMammal = "I am a string"
    ShowMammalInfo(NotAMammal)
    
Main()
    
# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 12
# =============================================================================




