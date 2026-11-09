# task services
from datetime import date, datetime
from models.task import Task
from services.file_handler import (
    tasks,
    usernames,
    save_tasks
)

def view_completed():
    """
    Displays completed tasks, or a message when there are none.
    """
    completed_tasks = [task for task in tasks if task.completed == "Yes"]
    if not completed_tasks:
        print("No completed tasks found.")
        return

    print("Completed tasks:")
    for task in completed_tasks:
        print(task)

def view_mine(current_user):
    """
    Display tasks assigned to current_user with a numbered list and allow
    the user to choose a task to complete or edit.
    """
    user_tasks = [task for task in tasks if task.username == current_user]

    if not user_tasks:
        print("No tasks assigned")
        return

    while True:
        print("\nTasks assigned to you:")
        for index, task in enumerate(user_tasks, start=1):
            print(task.vm_to_string(index))

        selection = input(
            "Enter task number to select it or -1 to return to the menu: "
        )

        if selection == "-1":
            return

        try:
            task_number = int(selection)
        except ValueError:
            print("Please enter a valid task number or -1.")
            continue

        if task_number < 1 or task_number > len(user_tasks):
            print("Task number out of range.")
            continue

        selected_task = user_tasks[task_number - 1]

        while True:
            action = input(
                "Choose an action: 1 - mark complete, 2 - edit task, "
                "-1 - return: "
            ).strip()

            if action == "-1":
                break

            if action == "1":
                selected_task.completed = "Yes"
                save_tasks()
                print(f"Task '{selected_task.title}' marked as complete.")
                return

            if action == "2":
                if selected_task.completed == "Yes":
                    print("This task has already been completed and "
                          "cannot be edited.")
                    break

                print("Leave a field blank to keep the current value.")
                new_username = input(
                    f"New username ({selected_task.username}): "
                ).strip()
                new_due = input(
                    f"New due date ({selected_task.due}): "
                ).strip()

                if new_username:
                    selected_task.username = new_username
                if new_due:
                    selected_task.due = new_due

                save_tasks()
                print(f"Task '{selected_task.title}' updated.")
                return

            print("Invalid option. Please choose 1, 2, or -1.")

def view_all():
    """
    Prints all tasks
    """
    for task in tasks:
        print(task)
        
def delete_task():
    """
    Deletes a task from tasks.txt
    """
    view_all()
    task_to_delete = input("Enter the title of the task to delete: ")
    for task in tasks:
        if task.title == task_to_delete:
            tasks.remove(task)
            print(f"{task.title} has been deleted")
            save_tasks()
            break
    else:
        print("Task not found")
        
def add_task():
    """
    Append tasks.txt with new task
    """
    username = input("User task is assigned to: ")
    if username not in usernames:
        print("User does not exist")
        return
    title = input("Task title: ")
    description = input("Task description: ")
    current = date.today().strftime("%d %b %Y")
    due = input("Due date [dd mmm yyyy]: ")
    try:
        datetime.strptime(due, "%d %b %Y")  # validate date
    except ValueError:
        print("Invalid date format. Please use 'dd mmm yyyy'.")
        return
    completed = "No"
    new_task = Task(username, title, description, current, due, completed)
    tasks.append(new_task)
    save_tasks()
    print(f"{new_task.title} task added")