# Day 8 - To Do List App

tasks = []

choice = ""

while choice != "4":

    print("\n--- TO DO LIST ---")
    print("1 - View Tasks")
    print("2 - Add Task")
    print("3 - Remove Task")
    print("4 - Exit")

    choice = input("Choose an option: ")

    # View tasks
    if choice == "1":

        if len(tasks) == 0:
            print("No tasks yet")

        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    # Add task
    elif choice == "2":

        task = input("Enter new task: ")
        tasks.append(task)

        print("Task added")

    # Remove task
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove")

        else:

            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):

                removed = tasks.pop(task_number - 1)
                print("Removed task:", removed)

            else:
                print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid option")