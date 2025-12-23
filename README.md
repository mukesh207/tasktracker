# Task Tracker CLI

A simple command-line task management tool to help you organize and track your daily tasks.

## Features

- ✅ Add new tasks
- ✏️ Update task descriptions
- 🔄 Change task status (not done, in progress, done)
- 🗑️ Delete tasks
- 📋 List tasks by status

## Installation

No external dependencies required. Just make sure you have Python 3.6+ installed.

```bash
python3 --version
```

## Usage

Run the CLI with:

```bash
python3 taskTrackeCli.py <command> [arguments]
```

## Available Commands

### 1. Add a Task
```bash
python3 taskTrackeCli.py add "Your task description"
```
Creates a new task with status "not done".

**Example:**
```bash
python3 taskTrackeCli.py add "Buy groceries"
```

### 2. List All Tasks
```bash
python3 taskTrackeCli.py listAll
```
Displays all tasks with their ID, description, and status.

### 3. Update Task Description
```bash
python3 taskTrackeCli.py update <taskId> "New description"
```
Modifies the description of an existing task.

**Example:**
```bash
python3 taskTrackeCli.py update 1 "Buy groceries and cook dinner"
```

### 4. Update Task Status
```bash
python3 taskTrackeCli.py updateStatus <taskId> <status>
```
Changes the status of a task. Valid statuses: `done`, `not done`, `in progress`

**Example:**
```bash
python3 taskTrackeCli.py updateStatus 1 "in progress"
python3 taskTrackeCli.py updateStatus 1 "done"
```

### 5. Delete a Task
```bash
python3 taskTrackeCli.py delete <taskId>
```
Removes a task permanently.

**Example:**
```bash
python3 taskTrackeCli.py delete 1
```

### 6. List Completed Tasks
```bash
python3 taskTrackeCli.py listDone
```
Shows only tasks with status "done".

### 7. List Pending Tasks
```bash
python3 taskTrackeCli.py listTaskNotDone
```
Shows only tasks with status "not done".

### 8. List In-Progress Tasks
```bash
python3 taskTrackeCli.py listTaskInProgress
```
Shows only tasks with status "in progress".

### 9. Show Help
```bash
python3 taskTrackeCli.py help
```
Displays all available commands and usage information.

## Data Storage

Tasks are stored in `tasks.json` file in the same directory. Each task contains:
- `id`: Unique identifier (integer)
- `description`: Task description (string)
- `status`: Task status - "done", "not done", or "in progress"

## Example Workflow

```bash
# Add some tasks
python3 taskTrackeCli.py add "Buy milk"
python3 taskTrackeCli.py add "Write report"
python3 taskTrackeCli.py add "Call dentist"

# List all tasks
python3 taskTrackeCli.py listAll

# Mark a task as in progress
python3 taskTrackeCli.py updateStatus 2 "in progress"

# View in-progress tasks
python3 taskTrackeCli.py listTaskInProgress

# Mark task as done
python3 taskTrackeCli.py updateStatus 2 "done"

# View completed tasks
python3 taskTrackeCli.py listDone

# Delete a task
python3 taskTrackeCli.py delete 3
```

## Notes

- Task IDs are automatically assigned and increment starting from 1
- When updating a task, its status is preserved if you're only changing the description
- When updating status, the description is preserved
