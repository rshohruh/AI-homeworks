import json
import csv

class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title, description, due_date=None, status="Pending"):
        task = {
            "Task ID": task_id,
            "Title": title,
            "Description": description,
            "Due Date": due_date,
            "Status": status,
        }
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task["Task ID"] == task_id:
                for key, value in kwargs.items():
                    if key in task:
                        task[key] = value
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["Task ID"] != task_id]

    def save_to_file(self, filename, format="json"):
        if format == "json":
            with open(filename, "w") as file:
                json.dump(self.tasks, file, indent=4)
        elif format == "csv":
            with open(filename, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.tasks[0].keys())
                writer.writeheader()
                writer.writerows(self.tasks)
        else:
            raise ValueError("Unsupported file format")

    def load_from_file(self, filename, format="json"):
        try:
            if format == "json":
                with open(filename, "r") as file:
                    self.tasks = json.load(file)
            elif format == "csv":
                with open(filename, "r") as file:
                    reader = csv.DictReader(file)
                    self.tasks = list(reader)
            else:
                raise ValueError("Unsupported file format")
        except FileNotFoundError:
            self.tasks = []
