class Account :
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance


    def deposit(self,amount):
            if amount>0:
                    print(f"{amount} deposited  ")
                    self.__balance+=amount
            else:
                 print("Insufficient amount")

    def showbalance(self)  :
         print(f"{self.name} , Your Total balance is : {self.__balance}")

    def _get_balance(self):
     return self.__balance
    
    def _set_balance(self, new_balance):
        self.__balance = new_balance


class SavingsAccount(Account):
        def __init__(self,name, balance):
            super().__init__(name, balance)
        def withdraw(self,amount):
         if self._get_balance()-amount<500:
              print("Withdraw denied ,Minimum balance should remain ₹500 ")
         else:
              self._set_balance(self._get_balance() - amount)
              print(f"{amount} withdrawn from your acount")
              

class CurrentAccount(Account):
     def __init__(self, name, balance):
          super().__init__(name, balance)
     def withdraw(self,amount):
          if amount<=self._get_balance():
               
               self._set_balance(self._get_balance() - amount)
               
               print(f"{amount} withdraw")
account = None

while True:
    print("\n------ BANK SYSTEM ------")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Show Balance")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Thank you. Goodbye!")
        break

    elif choice == 1:
        name = input("Enter account holder name: ")
        account = SavingsAccount(name, 0)
        print("Savings Account created successfully")

    elif choice == 2:
        name = input("Enter account holder name: ")
        account = CurrentAccount(name, 0)
        print("Current Account created successfully")

    elif choice == 3:
        if account is None:
            print("Please create an account first")
        else:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)

    elif choice == 4:
        if account is None:
            print("Please create an account first")
        else:
            amount = int(input("Enter withdrawal amount: "))
            account.withdraw(amount)

    elif choice == 5:
        if account is None:
            print("Please create an account first")
        else:
            account.showbalance()

    else:
        print("Invalid choice. Try again.")
