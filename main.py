
password=input("Enter a strong password : ")

a=any(char.isupper() for char in password)
b=any(char.islower() for char in password)
c=any(char.isdigit() for char in password)
d=any(char in "!@#$%^&*()" for char in password)


score = 0
if a: score += 1
if b: score += 1
if c: score += 1
if d: score += 1

if(len(password)<8):
    print("Password is too small")
elif(score==2):
    print("🙂 Weak password,try somthing strong")
elif(score==3):
    print("🤏 Moderate password,try somthing strong")
elif(score==4):
    print("💪 Strong password")




