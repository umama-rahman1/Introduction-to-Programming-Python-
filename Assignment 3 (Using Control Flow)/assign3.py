#Umama Rahman; Student ID: 20200915

initial_balance = float(input("Please input starting balance: "))

print("")

choice = input("Please type letter - d -(for depositing) -\- w - (for withdrawing) " )

print("")

transaction_amount = float(input("Please input transaction amount: "))

print("")

if (transaction_amount < 0):
    print("ERROR: TRANSACTION AMOUNT CANNOT BE NEGATIVE VALUE")
    finalBalance = initial_balance
    print("")
    print("Final balance: ", finalBalance)
    
if (transaction_amount > 0):        
    if (choice == "d"):
        finalBalance = initial_balance + transaction_amount
        print("Final balance: ",finalBalance)
    elif (choice == "w"):
        finalBalance = initial_balance - transaction_amount
        print("Final balance: ",finalBalance)









