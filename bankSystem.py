
balance=0.0

print("_______SIMPLE BANK SYSTEM_______\n")



def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient funds!"
    balance -= amount
    return balance

def check_balance():
    return balance


while True:
    print("\nChoose what you want to do \n")
    print("To DEPOSIT MONEY, Print 1 ")
    print("To WITHDRAWL MONEY, Print 2 ")
    print("To CHECK BALANCE, Print 3")
    print("To exit, Print 0 \n")
    choice=int(input("Enter your choice :"))
    

    if choice==0:
        print("EXIT")
        break
    elif choice==1: 
           amount=float(input("Enter yur amount : "))
           new_b=deposit(amount)
           print(f"\nDeposited ₹{amount}.Total Balance ₹{new_b}")
           
    elif choice==2:
           amount=float(input("Enter yur amount : "))
           result=withdraw(amount)

           if result is None:
                print("Insufficient Funds")

           else:
                print(f"\nWithdrawn ₹{amount}.Remaining ₹{result} ")
           
    elif choice==3:
           c=check_balance()
           print(f"Total balance ₹{c}\n")

    else:
         print("ERROR")
    
        

