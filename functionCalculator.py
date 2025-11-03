def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print("You cannot divide with Zero")

    else:
        return a/b
def modulous(a,b):
    return a%b
    
a=int(input("Enter your first value : "))
b=int(input("Enter your second value : "))

operation=input("Choose operation (+,-,*,/,%) : ").strip()

if operation=="+":
    print(f"Result : {add(a,b)}")
elif operation=="-":
    print(f"Result : {sub(a,b)}")
elif operation=="*":
    print(f"Result : {multiply(a,b)}")
elif operation=="/":
    print(f"Result : {divide(a,b)}")
elif operation=="%":
    print(f"Result : {modulous(a,b)}")
else:
    print("There is a mistake by user check again ")
