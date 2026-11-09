# Task Class
class Task:
    def __init__(self, username, title, description, assigned, due,
                 completed):
        self.username = username
        self.title = title
        self.description = description
        self.assigned = assigned
        self.due = due
        self.completed = completed

    def vm_to_string(self, ref_num):
        output = "\n"
        output += "_" * 59 + "\n"
        output += f"{'Task:':<20}{self.title}\n"
        output += f"{'Reference Number:':<20}{ref_num}\n"
        output += f"{'Assigned to:':<20}{self.username}\n"
        output += f"{'Date assigned:':<20}{self.assigned}\n"
        output += f"{'Due date:':<20}{self.due}\n"
        output += f"{'Task completed?':<20}{self.completed}\n"
        output += f"{'Task description:':<20}{self.description}\n"
        output += "_" * 59
        return output

    def __str__(self):
        output = "\n"
        output += "_" * 59 + "\n"
        output += f"{'Task:':<20}{self.title}\n"
        output += f"{'Assigned to:':<20}{self.username}\n"
        output += f"{'Date assigned:':<20}{self.assigned}\n"
        output += f"{'Due date:':<20}{self.due}\n"
        output += f"{'Task completed?':<20}{self.completed}\n"
        output += f"{'Task description:':<20}{self.description}\n"
        output += "_" * 59
        return output