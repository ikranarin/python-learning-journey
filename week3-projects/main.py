from task import Task
from day15_task_manager import TaskManager

def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            priority = input("Priority: ")
            deadline = input("Deadline: ")
            manager.add_task(Task(title, desc, priority, deadline))

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            title = input("Task title to complete: ")
            for t in manager.tasks:
                if t.title == title:
                    t.mark_complete()

        elif choice == "4":
            title = input("Task title to delete: ")
            manager.delete_task(title)

        elif choice == "5":
            manager.save_to_file()
            break

if __name__ == "__main__":
    main()