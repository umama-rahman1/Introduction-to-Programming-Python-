#Assignment 7 (Dictionary) - Umama Rahman ; ID: 202000915

#global balances
balances = {"Andy" : 10} #dictionary for accounts

'''
Given a person's name and amount of money, adds amount to their account
If the person does not have an account, one is created for them.
Parameters:
    name - string
    amount - float, amount >= 0
Returns:
    present - True if account existed, False if account had to be created
    newBalance - new balance for person
'''

def depositMoney(name, amount):
    present = False
    newBalance = 0
    
    for i in balances:
        if (name == i):
            present = True
            
    if (present == True):
        newBalance = float(balances.get(name) + amount)
        balances[name] = newBalance
    if (present == False):
        newBalance = amount
        balances[name] = newBalance
    
    return present,newBalance
   
"""

Given a person's name and amount of money, withdraws amount from their account.
If person does not have enough balance, function indicates overdraft
If person does not have an account, function indicates error

Parameters:
    name - string
    amount - float, amount >= 0
Returns: 
    present - True if account existed, False if not
    overdraft - False if existing account had enough balance for withdrawal, True if account went in to overdraft or didn't exist
    float - New balance for person (or 0 if account did not exist)
""" 

def withdrawMoney(name, amount):
    present = False
    overdraft = False
    newBalance = 0
    
    for i in balances:
        if (name == i):
            present = True
            
    if (present == True):
        if (amount > balances.get(name)):
            overdraft = True
            newBalance = float(balances.get(name) - amount)
            balances[name] = newBalance
        elif (amount < balances.get(name)):
            newBalance = float(balances.get(name) - amount)
            balances[name] = newBalance
    if (present == False):
        overdraft = True
        print("Error: Account not found")
        newBalance = 0
        
    return present, overdraft, newBalance
        
        
    
    
    
    
    
    
    
    
    
    
    
    