def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username == "admin" and password == "pranali123":
        print("Login Successfully ")
        return True
    else:
        print("Invalid Credentials")
        return False
    
def file_manager():
    while True:
        print("\nFILE MANAGER : ")
        print("1.Create A New File : ")
        print("2.Read File : ")
        print("3.Delete A File : ")
        print("4.Go Back To Menu : ")
        choice=input("Enter your choice : ")
        
        if choice == "1":
            filename = input("Enter the name of the new file : ")
            try:
                with open(filename,'w') as file:
                    file.write("this is a new file.")
                print(f"file '{filename}' created.")
            except:
                print("Error creating the file.")
        
        elif choice == "2":
            try:
                with open("myfile.txt",'r') as file:
                    content = file.read()
                print("\nContent from myfile.txt :")
                print(content)
            except FileNotFoundError:
                print("file 'myfile.txt' not found.")
                
        elif choice == '3':
            filename = input("enter the name of the file to delete : ")
            try:
                with open(filename, 'w') as file:
                    file.close()  
                print(f"File '{filename}' deleted (overwritten).")
            except FileNotFoundError:
                print(f"File '{filename}' not found!")
                
        elif choice == '4':
            break
        else:
            print("INVALID OPTION. PLEASE TRY AGAIN.")
            
def calculator():
    while True:
        print("\nCalculator : ")
        print("1. Add")
        print("2. Substract ")
        print("3. Multiply")
        print("4. Divide")
        print("5. Go Back To Main Menu ")

        choice = input("Enter Your Choice: ")
        if choice == '5':
            break
        
        try:
            num1=float(input("Enter First Number: "))        
            num2=float(input("Enter Second Number: "))
            
            if choice == '1':
                print(f"Result : {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1-num2}")
            elif choice == '3':
                    print(f"Result: {num1*num2}")
            elif choice == '4':
                if num2 !=0:
                    print(f"Result: {num1/num2}")
                else:
                    print("Error: Division By Zero.")
            else:
                print("Invalid Choice.")
        except ValueError:
            print("Invalid Input.Please Enter Numeric Values.")
            
def main_menu():
    while True:
        print("\nWelcome To Mini OS!")
        print("1.login")
        print("2.file manager")
        print("3.calculator")
        print("4.exit")
        
        choice =  input("Enter your choice: ")
        
        if choice == '1':
            if login():
                continue
            else:
                continue
        elif choice == '2':
            file_manager()
        elif choice == '3':
            calculator()
        elif choice == '4':
            print("EXISTING THE SYSTEM. BYE!")
            break
        else:
            print("Invalid Choice. Please Try Again.")
            
if __name__ == "__main__":
    main_menu() 

        