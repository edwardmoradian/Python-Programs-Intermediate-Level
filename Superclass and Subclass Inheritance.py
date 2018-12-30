# Description of the Program: Employee Superclass with ProductionWorker Subclass
# Illustration of inheritance and the use of an object's accessor methods

class Employee: # Employee is the superclass
    
    def __init__(self,Name,Number):
        # Initialize the __Name and __Number attributes
        self.__Name = Name
        self.__Number = Number
    
    # Two mutator methods: SetName and SetNumber
    def SetName(self,Name):
        self.__Name = Name
    
    def SetNumber(self,Number):
        self.__Number = Number
    
    # Two accessor methods: GetName and GetNumber
    def GetName(self):
        return self.__Name
    
    def GetNumber(self):
        return self.__Number
        
class ProductionWorker(Employee): # ProductionWoerker is the subclass of the Employee superclass
    
    def __init__(self,Name,Number,ShiftNumber,HourlyRate):
        Employee.__init__(self,Name,Number) # ProductionWorker inherits Name and Number methods from Employee
        # Initialize the __ShiftNumber and __HourlyRate attributes
        self.__ShiftNumber = ShiftNumber
        self.__HourlyRate = HourlyRate
    
    # Two mutator methods: SetShiftNumber and SetHourlyRate
    def SetShiftNumber(self,ShiftNumber):
        self.__ShiftNumber = ShiftNumber
        
    def SetHourlyRate(self,HourlyRate):
        self.__HourlyRate = HourlyRate
        
    # Two accessor methods: GetShiftNumber and GetHourlyRate
    def GetShiftNumber(self):
        return self.__ShiftNumber
        
    def GetHourlyRate(self):
        return self.__HourlyRate
        
def Main():
    
    Name = input("Please enter the employee's name: ")
    Number = input("Please enter the employee's number: ")
    ShiftNumber = input("Please enter the employee's shift number (either 1 for day or 2 for night): ")
    HourlyRate = input("Please enter the employee's hourly rate: ")
    
    # Create an instance of ProductionWorker with user input for the attributes
    ProductionWorker1 = ProductionWorker(Name,Number,ShiftNumber,HourlyRate)
    print()
    
    # Using the object's accessor methods to display the object's data attributes
    print("The employee's name is:", ProductionWorker1.GetName())
    print("The employee's number is:", ProductionWorker1.GetNumber())
    print("The employee's shift number is:", ProductionWorker1.GetShiftNumber())
    print("The employee's hourly rate is:", ProductionWorker1.GetHourlyRate())
    
Main()







