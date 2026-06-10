# Task Tracker CLI

This project allows users to manage tasks directly from the terminal using positional arguments and stores all data in a JSON file.

Project idea from roadmap.sh:

https://roadmap.sh/projects/task-tracker

## Features

- Add a task
- Update a task
- Delete a task
- Mark a task as in progress
- Mark a task as done
- List all tasks
- List tasks by status:
  - todo
  - in-progress
  - done
- Store task data in a JSON file
- Automatic task ID generation

## Project Structure

```text
task-tracker/
│
├── main.py
├── tasks.py
├── source.py
├── README.md
└── tasks.json
```

## Usage

### Add a Task

```bash
python main.py add "Buy groceries"
```

Output:

```text
Task added successfully (ID: 1)
```

### Update a Task

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task

```bash
python main.py delete 1
```

### Mark Task as In Progress

```bash
python main.py mark-in-progress 1
```

### Mark Task as Done

```bash
python main.py mark-done 1
```

### List All Tasks

```bash
python main.py list
```

Example output:

```text
ID    Description          Date          Status
1     Buy groceries        2026-06-09    todo
2     Learn Python         2026-06-09    done
```

### List Tasks by Status

List completed tasks:

```bash
python main.py list done
```

List pending tasks:

```bash
python main.py list todo
```

List tasks in progress:

```bash
python main.py list in-progress
```

## Data Storage

Tasks are stored in a local JSON file.

Example:

```json
[
  {
    "id_task": 1,
    "task": "Learn Python",
    "status": "todo",
    "date": "2026-06-09"
  }
]
```

## What I Learned

- Working with JSON files
- File handling in Python
- Command-line interfaces (CLI)
- Using argparse
- CRUD operations
- Error handling
- Organizing code into multiple modules
