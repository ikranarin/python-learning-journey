import json
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, title):
        self.tasks = [t for t in self.tasks if t.title != title]

    def list_tasks(self):
        for task in self.tasks:
            print(task.title, "-", "Done" if task.completed else "Pending")

    def save_to_file(self, filename="tasks.json"):
        data = [task.__dict__ for task in self.tasks]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    task = Task(**item)
                    self.tasks.append(task)
        except:
            pass