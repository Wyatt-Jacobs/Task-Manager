# File handler
from models.task import Task

tasks = []
usernames = []
passwords = []

def save_tasks():
    """
    Saves all tasks in memory back to tasks.txt
    """
    with open("data/tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(
                f"{task.username}, {task.title}, {task.description}, "
                f"{task.assigned}, {task.due}, {task.completed}\n"
            )


def load_tasks():
    """
    Loads task from tasks.txt
    """
    tasks.clear()
    try:
        with open("data/tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\r\n")
                if not line:
                    continue
                (username, title, description,
                 assigned, due, completed) = line.split(", ")
                tasks.append(Task(username, title, description, assigned,
                                  due, completed))
    except FileNotFoundError:
        print("File not found")


load_tasks()


def load_users():
    """
    Loads users from user.txt
    """
    usernames.clear()
    passwords.clear()
    try:
        with open("data/user.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\r\n")
                if not line:
                    continue
                try:
                    username, password = line.split(", ", 1)
                except ValueError:
                    print("Skipping invalid user record in user.txt.")
                    continue
                usernames.append(username)
                passwords.append(password)
    except FileNotFoundError:
        print("File not found")