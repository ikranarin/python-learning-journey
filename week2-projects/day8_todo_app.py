import json

# -----------------------------
# Load tasks from file
# -----------------------------

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []


# -----------------------------
# Main program
# -----------------------------

choice = ""

while choice != "5":

    print("\n--- TO DO LIST ---")
    print("1 - View Tasks")
    print("2 - Add Task")
    print("3 - Mark Task as Done")
    print("4 - Remove Task")
    print("5 - Exit")

    choice = input("Choose an option: ")

    # -----------------------------
    # View tasks
    # -----------------------------

    if choice == "1":

        if len(tasks) == 0:
            print("No tasks yet")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):

                task = tasks[i]

                if task["done"]:
                    status = "✔"
                else:
                    status = "✘"

                print(i + 1, "-", task["title"], "-", status)

    # -----------------------------
    # Add task
    # -----------------------------

    elif choice == "2":

        title = input("Enter new task: ")

        task = {
            "title": title,
            "done": False
        }

        tasks.append(task)

        print("Task added")

    # -----------------------------
    # Mark task done
    # -----------------------------

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available")

        else:

            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["title"])

            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):

                tasks[number - 1]["done"] = True
                print("Task marked as done")

            else:
                print("Invalid number")

    # -----------------------------
    # Remove task
    # -----------------------------

    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks to remove")

        else:

            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["title"])

            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):

                removed = tasks.pop(number - 1)
                print("Removed:", removed["title"])

            else:
                print("Invalid number")

    elif choice == "5":

        print("Saving tasks...")

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        print("Tasks saved. Goodbye!")

    else:
        print("Invalid option")