# Login and registering users
from services.file_handler import (usernames, passwords, load_users)

def login():
    """
    Checks if password matches username. If password is incorrect throws
    incorrect password print statement
    """
    load_users()
    while True:
        user = input("Username: ")
        password = input("Password: ")
        credentials = dict(zip(usernames, passwords))
        if credentials.get(user) == password:
            print(f"Hi {user}, welcome back")
            return user
        elif user in usernames:
            print("Incorrect password")
        else:
            print("Username not found")
            
def reg_user():
    """
    Registers a new user
    """
    while True:
        new_username = input("Enter new username: ")
        if new_username in usernames:
            print("Username already exists")
            continue

        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")
        if new_password != confirm_password:
            print("Passwords do not match")
            continue

        try:
            with open("user.txt", "a+", encoding="utf-8") as f:
                f.seek(0, 2)
                if f.tell():
                    f.seek(f.tell() - 1)
                    if f.read(1) not in ("\n", "\r"):
                        f.write("\n")
                f.write(f"{new_username}, {new_password}\n")
        except OSError as error:
            print(f"Unable to save the new user: {error}")
            return

        usernames.append(new_username)
        passwords.append(new_password)
        print(f"{new_username} added")
        return
