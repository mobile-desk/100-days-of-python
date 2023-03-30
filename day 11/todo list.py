# to do list

todo = []

def add(task):
    todo.append(task)
    print("New task added")
    main() 

def view():

    if len(todo) == 0:
        print("You have not added any tasks yet!!")
        main()
    else:
        for i in todo:
            print(f"{todo.index(i)+1}. {i}")
        main() 

def delete(t):
    todo.pop(t-1)
    main()

def main():
    print("""
    Welcome to our To-Do app
    What would you like to do.
    ***Please input the correct command***
    *add - add task
    *view - view all tasks
    *delete - delete a specific task
    *exit - close program
    """)

    usercommand = input("Enter command here: ").lower()

    if usercommand == "add":
        t = input("Enter new task here: ")
        add(t)
    elif usercommand == "exit":
        exit()
    elif usercommand == "delete":
        if len(todo) == 0:
            print("You have not added any tasks yet!!")
            main()
        else:  
            for i in todo:
                print(f"{todo.index(i)+1}. {i}")
            t = int(input("Please input the number of the task you want to delete: "))
            delete(t)
    elif usercommand == "view":
        view()
    else:
        print("Invalid command")
        main()

if __name__ == "__main__":
    main()