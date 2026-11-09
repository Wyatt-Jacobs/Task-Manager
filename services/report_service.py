# Generating and displaying statistics
from datetime import date, datetime
from services.file_handler import tasks, usernames

def generate_reports():
    """
    Generates reports for tasks and users
    creates task_overview.txt and user_overview.txt
    """
    # Task Overview
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.completed == "Yes")
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(
        1 for task in tasks
        if task.completed == "No"
        and date.today() > datetime.strptime(task.due, "%d %b %Y").date()
    )
    percent_incomplete = (
        (incomplete_tasks / total_tasks * 100) if total_tasks > 0 else 0
    )
    percent_overdue = (
        (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0
    )
    task_overview = "TASK OVERVIEW\n"
    task_overview += f"Total tasks: {total_tasks}\n"
    task_overview += f"Completed tasks: {completed_tasks}\n"
    task_overview += f"Incomplete tasks: {incomplete_tasks}\n"
    task_overview += f"Overdue tasks: {overdue_tasks}\n"
    task_overview += (
        f"Percentage of incomplete tasks: {percent_incomplete:.2f}%\n"
    )
    task_overview += (
        f"Percentage of overdue tasks: {percent_overdue:.2f}%\n"
    )

    # User Overview
    total_users = len(usernames)
    user_overview = "USER OVERVIEW\n"
    user_overview += f"Total registered users: {total_users}\n"
    user_overview += f"Total tasks: {total_tasks}\n"
    for user in usernames:
        user_tasks = [task for task in tasks if task.username == user]
        assigned_count = len(user_tasks)
        completed_count = sum(
            1 for task in user_tasks if task.completed == "Yes"
        )
        incomplete_count = assigned_count - completed_count
        overdue_count = sum(
            1 for task in user_tasks
            if task.completed == "No"
            and date.today() > datetime.strptime(task.due, "%d %b %Y").date()
        )

        percent_of_all_tasks = (
            assigned_count / total_tasks * 100 if total_tasks else 0
        )
        percent_completed = (
            completed_count / assigned_count * 100 if assigned_count else 0
        )
        percent_incomplete = (
            incomplete_count / assigned_count * 100 if assigned_count else 0
        )
        percent_overdue = (
            overdue_count / assigned_count * 100 if assigned_count else 0
        )

        user_overview += f"\n{user}\n"
        user_overview += f"Tasks assigned: {assigned_count}\n"
        user_overview += (
            f"Percentage of all tasks assigned: "
            f"{percent_of_all_tasks:.2f}%\n"
        )
        user_overview += (
            f"Percentage of assigned tasks completed: "
            f"{percent_completed:.2f}%\n"
        )
        user_overview += (
            f"Percentage of assigned tasks incomplete: "
            f"{percent_incomplete:.2f}%\n"
        )
        user_overview += (
            f"Percentage of assigned tasks overdue and incomplete: "
            f"{percent_overdue:.2f}%\n"
        )

    try:
        with open("data/task_overview.txt", "w", encoding="utf-8") as f:
            f.write(task_overview)
        with open("data/user_overview.txt", "w", encoding="utf-8") as f:
            f.write(user_overview)
        print("Reports generated successfully.")
    except FileNotFoundError:
        print("File not found")
    return task_overview, user_overview


def display_statistics():
    """
    Generates and displays the task and user reports.
    """
    task_overview, user_overview = generate_reports()
    print(f"\n{'=' * 60}\nTASK OVERVIEW\n{'=' * 60}")
    print(task_overview.rstrip())
    print(f"\n{'=' * 60}\nUSER OVERVIEW\n{'=' * 60}")
    print(user_overview.rstrip())
    print("\n")