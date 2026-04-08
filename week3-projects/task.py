class Task:
    def __init__(self, title, description, priority, deadline):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True