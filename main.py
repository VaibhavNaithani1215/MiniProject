

print("------MENU DRIVEN CALCULATOR------")

while True:
    print("Select operation")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for division")
    print("4 for multiplication")
    print("0 for exit")
    choice=int(input("Enter your operation : "))

    if choice==0:
        print("EXIT")
        break

    elif choice==1:
        a=int(input("Enter your number : "))
        b=int(input("Enter your number : "))
        print(f"Addition : {a+b}")
        
    elif choice==2:
        a=int(input("Enter your number : "))
        b=int(input("Enter your number : "))
        print(f"Subtraction : {a-b}")
        
    elif choice==3:
        a=int(input("Enter your number : "))
        b=int(input("Enter your number : "))
        if b==0:
            print("Division by zero is not defined")
        else:
            print(f"Division : {a/b}")

        
        
    elif choice==4:
        a=int(input("Enter your number : "))
        b=int(input("Enter your number : "))
        print(f"Multiplication : {a*b}")


    else:
        print("invalid input")
        

        
        