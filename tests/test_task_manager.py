import unittest
from models.task import Task


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for Task Manager use cases.
    """

    def setUp(self):
        """
        Create a sample task before each test.
        """
        self.task = Task(
            "admin",
            "Submit Assignment",
            "Complete Software Design project",
            "09 Nov 2026",
            "15 Nov 2026",
            "No"
        )

    # ---------------------------------------------------
    # Use Case 1: Create a Task
    # ---------------------------------------------------
    def test_create_task(self):
        self.assertEqual(self.task.username, "admin")
        self.assertEqual(
            self.task.title,
            "Submit Assignment"
        )
        self.assertEqual(
            self.task.description,
            "Complete Software Design project"
        )
        self.assertEqual(
            self.task.completed,
            "No"
        )

    # ---------------------------------------------------
    # Use Case 2: View Task Information
    # ---------------------------------------------------
    def test_view_task_information(self):
        task_string = str(self.task)

        self.assertIn("admin", task_string)
        self.assertIn("Submit Assignment", task_string)
        self.assertIn(
            "Complete Software Design project",
            task_string
        )

    # ---------------------------------------------------
    # Use Case 3: Mark Task Complete
    # ---------------------------------------------------
    def test_mark_task_complete(self):
        self.task.completed = "Yes"

        self.assertEqual(
            self.task.completed,
            "Yes"
        )

    # ---------------------------------------------------
    # Use Case 4: Edit Task
    # ---------------------------------------------------
    def test_edit_task_due_date(self):
        self.task.due = "20 Nov 2026"

        self.assertEqual(
            self.task.due,
            "20 Nov 2026"
        )


if __name__ == "__main__":
    unittest.main()