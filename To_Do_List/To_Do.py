close = False

print("Welcome to your to do List!")
print("Type 'Close' to close the program.")
with open("To_Do.txt", "a+") as file:
    while close != True:
        command = input("What would you like to do? \n1. Add \n2. Remove \n3. View \n4. CLose\n> ")
        print("\n") 

        #Add items to the To-DO List
        if command == "Add" or command == "1":
            to_do = input("What would you like to add to your To-Do List?\n")
            file.write(to_do + "\n")

        #Remove items from the To-Do List
        elif command == "Remove" or command == "2":
            remove = input("What would you like to remove from your To-Do List?\n (Case senstive)\n")
            
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip("\n") != remove:
                    file.write(line)

        #View the To-Do List
        elif command == "View" or command == "3":
            file.seek(0)
            content = file.read()
            print("Your To-Do List:\n" + content)

        #Close the program
        elif command == "Close" or command == "4":
            close = True
        print("\n")