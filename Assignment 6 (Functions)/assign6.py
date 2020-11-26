#Assignment 6 by Umama Rahman; ID: 202000915

def setStartingBalance():
    startingBalance = float(input("Please provide your bank balance? "))
    return startingBalance

#print(setStartingBalance())

def depositAmount(depositAmt, currentBalance):
    if (depositAmt < 0):
        currentBalance = currentBalance
    if (depositAmt > 0):
        currentBalance += depositAmt
    
    return currentBalance

#print(depositAmount(10,100))

def withdrawAmount(withdrawAmt, currentBalance):
    overdraft = False
    if (withdrawAmt < 0):
        currentBalance = currentBalance
    elif (withdrawAmt > currentBalance):
        currentBalance -= withdrawAmt
        overdraft += 1
        overdraft = True
    elif (withdrawAmt <= currentBalance):
        currentBalance -= withdrawAmt
        
    return currentBalance, overdraft

#print(withdrawAmount(100,10))