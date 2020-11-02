#Assignment 4 by Umama Rahman Student ID: 202000915

finalBalance = float(input("Please provide your current bank balance: "))
overdraftCount = 0

choice = input("Do you wish to: Deposit (d) or Withdraw (w)? ")

while (choice != "q"):
    transactionAmt = float(input("Please provide transaction amount: "))
    if (choice == "d"):
        finalBalance = finalBalance + transactionAmt
        
    if (choice == "w"):
        finalBalance = finalBalance - transactionAmt
        if (transactionAmt > finalBalance):
            overdraftCount = overdraftCount + 1
        
    choice = input("Do you wish to: Deposit (d) or Withdraw (w) or Quit (q)? ")
    

