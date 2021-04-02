# Introducing Python 2nd Edition in Safari


## Slicing to get substrings
letters = 'abcdefghijklmnopqrstuvwxyz'


# [:] extracts the entire sequence from start to end
print(letters[:])


# [start:] specifies from the start offset to the end
print(letters[20:])


# [:end] specifies from the beginning to the end offset minus 1
print(letters[:5])


# [start:end] indicates from the srtart offset to the end offset minus 1
print(letters[12:15])


# [start:end:step] extracts from the start offset to the end offset minus 1, skipping characters by step
print(letters[0:4:2])


## While and For Loops

# for loop
nums = [3,2,1,0]
print(nums)
type(nums)

for i in nums:
    print(i)


# while loop
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 ==0:
        print('Found even number',number)
        break
    position += 1
else: # break not called
    print('No even number found')
    
    
## Iterate multiple sequences with zip()

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day,": drink",drink,"- eat",fruit,"- enjoy",dessert)
    
    
## List Comprehensions: [expression for item in iterable]

number_list = [number for number in range(1,6)]
number_list

# with a conditional statement
a_list = [number for number in range(1,6) if number % 2 == 1]
a_list


rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]

for row, col in cells:
    print(row,col)
    
## Functions

# Positional Arguments
def menu(wine,entree,dessert):
    return{'wine':wine,'entree':entree,'dessert':dessert}

# Keyword Arguments
menu(entree='beef',dessert='bagel',wine='bordeaux')
    
# Explode/Gather positional argument with *
def print_args(*args):
    print('Positional tuple:', args)
    
print_args(3,2,1,'wait','uh')

# Explode/Gather positional argument with **
# Use two asterisks to group keyword arguments into a dictionary, where the argument
# names are the keys and their values are the corresponding dictionary values

def print_kwargs(**kwargs):
    print('Keyword arguments:',kwargs)
    
print_kwargs(wine='merlot',entree='mutton',dessert='macroon')

# Lambdas
# A lambda has 0 or more comma-separated arguments followed by a colon and then the definition
# of the function. Use for when having many tiny functions
stairs = ['thud', 'meow', 'thud', 'hiss']

def edit_story(words, func):
    for word in words:
        print(func(word))
        
edit_story(stairs,lambda word:word.capitalize() + '!')


## Objects, Classes, Methods, Attributes

# An object is a custom data structure containing both variables called attributes and
# functions called methods. An attribute is a variable inside a class or object
# a method is a function in a class or object

# instance method = no preceding decorator, first argument as self to refer to the individual object itself
# class method = preceding @classmethod decorator, first argument as cls referrring to the class itself
# static method = preceding @staticmethod decorator and first argument not an object or class

# instance method
class Car():
    def exclaim(self):
        print("I'm a Car!")
        
give_me_a_car.exclaim()

# class method
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has",cls.count,"little objects.")
        
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
A.exclaim(True)

# static method

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
            
CoyoteWeapon.commercial()


# Magic methods = Special methods

__init__() # initializes a newly created object from its class definition and any arguments passed in
__eq__(self,other) # self == other
__add__(sell,other) # self + other

class Word():
    def __init__(self,text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    
first = Word('ha')
second = Word('blue')
first == second








    
    
    
    
    
    
    
    
    
    
    
    
