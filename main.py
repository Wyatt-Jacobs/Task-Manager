from services.user_service import login, reg_user

from services.task_service import (
    add_task,
    view_all,
    view_mine,
    view_completed,
    delete_task
)

from services.report_service import (
    generate_reports,
    display_statistics
)

from services.file_handler import (
    load_tasks,
    load_users
)

load_tasks()
load_users()

current_user = login()

if current_user == "admin":
    while True:
        menu = input('''Select one of the following options:
                    r - register a user
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    vc - view completed tasks
                    del - delete tasks
                    ds - display statistics
                    gr - generate reports
                    e - exit
                    : ''').strip().lower()

        if menu == 'r':
            reg_user()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine(current_user)

        elif menu == 'vc':
            view_completed()

        elif menu == 'del':
            delete_task()

        elif menu == 'ds':
            display_statistics()

        elif menu == 'gr':
            generate_reports()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")

else:
    while True:
        menu = input('''Select one of the following options:
                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit
                    : ''').strip().lower()

        if menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_mine(current_user)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")