from colored import fg, bg, attr 

from todo_functions import add_todo, remove_todo, mark_todo, view_todo

print(f"welcome to your TODO list {attr('reset')}")

    # CSV Structure
# CSV = comma seperated values - similar to table structure
# title,completed
# Todo 1,False
# Todo 2,True

file_name = "list.csv"

try:
    todo_file = open(file_name, "r") # If the file doesn't exist, it throws exception
    todo_file.close()
    print("in try block")

# If it exists, then all is fine
# If it does not exist, then we can create it

except FileNotFoundError as e:
    todo_file = open(file_name, "w")
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

def create_menu():
    print("1. Enter 1 to add a new item to your list")
    print("2. Enter 2 to remove item from you list")
    print("3. Enter 3 to mark an item as completed")
    print("4. Enter 4 to view your TODO list")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = create_menu()

    if(user_choice == "1"):
        add_todo(file_name)
    elif (user_choice == "2"):
        remove_todo(file_name)
    elif (user_choice == "3"):
        mark_todo(file_name)
    elif (user_choice == "4"):
        view_todo(file_name)
    elif (user_choice == "5"):
        continue
    else:
        print("Invalid Input")
    
    input("Press Enter to continue....")

print("Thank you for using TODO list")
