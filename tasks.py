"""
Task Manager - Command-line tool to manage homework/study tasks.
University of Mohamed Kheider - Biskra
"""

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting with empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to tasks.json file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def add_task(title):
    """Add a new task with the given title."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: '{title}'")


def list_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "[Done]" if task["done"] else "[    ]"
        print(f"  {task['id']}. {status} {task['title']}")
    print()


def mark_done(task_number):
    """Mark a task as done by its number."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    try:
        task_number = int(task_number)
    except ValueError:
        print("Error: Please enter a valid task number.")
        return

    for task in tasks:
        if task["id"] == task_number:
            if task["done"]:
                print(f"Task {task_number} is already marked as done.")
            else:
                task["done"] = True
                save_tasks(tasks)
                print(f"Task {task_number} marked as done!")
            return

    print(f"Error: Task number {task_number} not found.")


def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    try:
        task_number = int(task_number)
    except ValueError:
        print("Error: Please enter a valid task number.")
        return

    new_tasks = [t for t in tasks if t["id"] != task_number]
    if len(new_tasks) == len(tasks):
        print(f"Error: Task number {task_number} not found.")
        return

    # Re-assign IDs after deletion
    for i, task in enumerate(new_tasks):
        task["id"] = i + 1

    save_tasks(new_tasks)
    print(f"Task {task_number} deleted.")


def show_menu():
    """Display the main menu."""
    print("=" * 35)
    print("     Task Manager - Study Tasks")
    print("=" * 35)
    print("  1. Add new task")
    print("  2. View all tasks")
    print("  3. Mark task as done")
    print("  4. Delete a task")
    print("  5. Exit")
    print("=" * 35)


def main():
    """Main loop for the task manager application."""
    print("Welcome to Task Manager!")
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                add_task(title)
            else:
                print("Error: Task title cannot be empty.")

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            list_tasks()
            number = input("Enter task number to mark as done: ").strip()
            mark_done(number)

        elif choice == "4":
            list_tasks()
            number = input("Enter task number to delete: ").strip()
            delete_task(number)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
