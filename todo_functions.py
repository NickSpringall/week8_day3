import csv

def add_todo(file_name):
    print("Add todo")
    todo_title = input("Enter your TODO title: ")
    with open(file_name, "a")as todo_file:
        writer = csv.writer(todo_file)
        writer.writerow([todo_title, "false"])

def remove_todo(file_name):
    print("Remove todo")
    view_todo(file_name)
    todo_title = input("Enter the todo title that you want to remove: ")
    todo_lists = []
    # we will read and save all the data in a list escept the one that we want to remove
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        for row in reader:
            if(todo_title != row[0]):
                todo_lists.append(row)
    print(todo_lists)
    # print(todo_lists)
    # we will write that down in the file again
    with open(file_name, "w") as todo_file:
        writer = csv.writer(todo_file)
        writer.writerows(todo_lists)


    

def mark_todo(file_name):
    print("Make todo")
    view_todo(file_name)
    todo_title = input("Enter the todo title that you want to make as complete: ")
    todo_lists = []
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        for row in reader: 
            if (todo_title == row[0]):
                todo_lists.append([todo_title, "True"])
            else:
                todo_lists.append(row)
        print(todo_lists)
        with open (file_name, "w") as todo_file:
            writer = csv.writer(todo_file)
            writer.writerows(todo_lists)


def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as f: #convention is to use f as variable for with 
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if(row[1] == "True"):
                print(f"todo {row[0]} is completed")
            else:
                print(f"todo {row[0]} is not completed")