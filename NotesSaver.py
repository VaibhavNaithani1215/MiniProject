print("_______Notes Saver (CLI Notepad)_______\n")

while True:
    print("Choose what you want to do \n")
    print("To add notes, Print 1 ")
    print("To view all notes, Print 2 ")
    print("To exit, Print 0 \n")
    choice=int(input("Enter your choice :"))

    if choice==0:
        print("EXIT")
        break

    elif choice==1:
        with open("MY NOTES.txt","a") as file:
            content=input("Write your note : ")
            file.write(content +"\n")
        print("Succesfully written")    
            
   
    elif choice==2:
        with open("MY NOTES.txt","r") as file:
            content=file.read()
            print(f"----Your notes---- \n{content}")

    else:
        print("Invalid input")

 
            

    