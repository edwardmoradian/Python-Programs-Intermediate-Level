# Description of Program: Create a BankAccount class to simulate a bank account
# Uses the __str__ method to indicate the object's state

class BankAccount:
    
    # the __init__ method accepts two arguments for the account's balance - self and bal
    # bal is assigned to the balance private attribute
    def __init__(self, bal):
        self.__balance = bal
        
    # The deposit method makes a deposit into the account summing the current balance with the deposit
    # The deposit is the amount parameter
    def deposit(self, amount):
        self.__balance += amount
        
    # The withdraw method withdraws an amount from the account. This amount is the amount argument.
    # Checks to see if there are enough funds to withdraw chosen amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')
    
    # The get_balance method returns the account balance.
    def get_balance(self):
        return self.__balance
    
    # The __str__ method returns a string indicating the object's state.
    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
    
def Main():
    # Get the starting balance.
    start_bal = float(input('Enter your starting balance: '))
    
    # Create a BankAccount object named savings, this will be an instance of the class BankAccount
    savings = BankAccount(start_bal) # start_bal gets passed into the bal parameter in the __init__ method
    
    # Deposit the user's paycheck.
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay) # pay gets passed into the amount parameter in the deposit method
    
    # Display the balance using the print method with the savings argument
    # This automatiicaly calls the __str__ method to give the state of the object savings
    print(savings)
    
    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash) # cash gets passed into the amount parameter in the withdraw method
    
    # Display the balance.
    print(savings)
    
# Call the main function.
Main()
    
# =============================================================================
# This program is a modified version of the code that appears in "Starting Out with Python" by Tony Gaddis
# (Second Edition), Chapter 11
# =============================================================================