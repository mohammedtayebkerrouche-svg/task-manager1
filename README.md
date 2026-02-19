# Task Manager - Simple Task List

A command-line Task Manager built in Python for managing homework and study tasks.

**University of Mohamed Kheider – Biskra**  
Course: Programming | Level: PhD Students | Academic Year: 2025/2026

---

## Features

- Add new tasks
- View all tasks with their status (done / pending)
- Mark tasks as done
- Delete tasks
- Data persisted automatically in `tasks.json`

---

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only built-in modules)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/mohammedtayebkerrouche-svg/task-manager
cd task-manager
```

---

## Usage

Run the application:

```bash
python tasks.py
```

You will see a menu like this:

```
===================================
     Task Manager - Study Tasks
===================================
  1. Add new task
  2. View all tasks
  3. Mark task as done
  4. Delete a task
  5. Exit
===================================
Enter your choice (1-5):
```

### Menu Options

| Option | Description |
|--------|-------------|
| 1 | Enter a task title to add it to your list |
| 2 | Display all tasks with their ID and status |
| 3 | Enter a task ID to mark it as completed |
| 4 | Enter a task ID to remove it permanently |
| 5 | Exit the application |

---

## Example Session

```
Welcome to Task Manager!
===================================
     Task Manager - Study Tasks
===================================
  1. Add new task
  ...
Enter your choice (1-5): 1
Enter task title: Workshop 1 – Academic Writing Assisted by AI
Task added: 'Workshop 1 – Academic Writing Assisted by AI'

Enter your choice (1-5): 2

--- Your Tasks ---
  1. [Done] Workshop 1 – Academic Writing Assisted by AI
  2. [    ] Workshop 1 – Collaborative Management of Open Scientific Projects
  3. [    ] Workshop 2 – Strengthening Research Skills through AI-Assisted Literature Review
  4. [    ] Workshop 2 – Academic Writing Assisted by AI
```

---

## File Structure

```
task-manager/
│
├── tasks.py        # Main application file
├── tasks.json      # Task data storage (auto-created)
└── README.md       # This file
```

---

## Running Flake8 (Code Style Check)

```bash
pip install flake8
flake8 tasks.py
# No output = no errors
```

---

## Git Commit History

```
git init
git add tasks.py tasks.json README.md
git commit -m "Initial commit: Add project files"

git commit -m "feat: Add add_task and list_tasks functions"
git commit -m "feat: Add mark_done and delete_task with error handling"
git commit -m "refactor: Clean code and add docstrings for Flake8 compliance"
```

---

## Error Handling

The application handles the following errors gracefully:

- **Invalid task number** – shows a clear error message instead of crashing
- **Empty task title** – rejects blank task names
- **Corrupted JSON file** – warns the user and starts with an empty list
- **Missing tasks.json** – automatically creates the file on first use

---

## License

This project is created for academic purposes at the University of Mohamed Kheider – Biskra.
