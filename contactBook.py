print("\n------CONTACT BOOK------\n ")

def add_contact():
        
        name=input("\nEnter Contact Name : ").strip().lower().capitalize()
        phone=(input("Enter phone number : "))

        if not phone.isdigit():
             print("invalid Phone Number ! ")
             return

        

        with open("contacts.txt","a") as file:
            file.write(name + "," + phone +"\n") 
           
            
def view_contacts():
    try :
          with open("contacts.txt","r") as file:
               show=file.read()
               print(f"\n{show}")
               
    except FileNotFoundError:
         print("\nfile does not exist")

    
def search_contact():
    search=input("\nEnter the name you want to search : ").strip().lower().capitalize()
    found=False
             
    with open("contacts.txt","r") as file:
         for line in file:
              if search in line:
                   print(line)
                   found=True

    if not found:
        print("\nContact not found\n")

    

while True:
    print("\nTO ADD CONTACTS , Enter 1 : ")
    print("TO VIEW ALL CONTACTS  , Enter 2 : ")
    print("TO SEARCH BY NAME   , Enter 3 : ")
    print("TO EXIT  , Enter 0 : ")
    choice=int(input("Enter your choice : "))


    if choice ==0:
        print("EXIT")
        break
    elif choice==1:
        add_contact()
        
    elif choice==2:
        view_contacts()
         
    elif choice==3:
        search_contact(
        )

    else:
         ("Error ! ,Please check again .")


