def FtoC():
    choice=input("Enter 'F' to convert Fahrenheit → Celsius or 'C' for Celsius → Fahrenheit: ").strip().upper()
    temp=float(input("Enter your temperature value : "))

    if choice=="F":
        print((temp-32)*5/9)

    elif choice=="C":
        print(((temp)*9/5)+32)

    else:
        print("PLEASE CHOOSE BETWEEN F AND C!! ")

FtoC()