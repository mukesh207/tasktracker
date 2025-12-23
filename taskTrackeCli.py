import sys
import os
import json
from datetime import datetime



taskFILE = "./tasks.json"


def load_tasks():    
    if not os.path.exists(taskFILE):
        return []
    with open(taskFILE, 'r') as file:
        content = file.read()
        if not content:
            return []
        return json.loads(content)
    
def save_tasks(tasks):
    with open(taskFILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_next_task_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1



def help():
    helpText = """
    Task Tracker CLI - Available Commands:
    1. add <taskDescription> - Add a new task
    2. delete <taskId> - Delete a task by ID
    3. updateStatus <taskId> <status> - Update the status of a task choices: done, not done, in progress
    4. update <taskId> <taskDescription> - Update the description of a task
    5. listAll - List all tasks
    6. listDone - List all completed tasks
    7. listTaskNotDone - List all pending tasks
    8. listTaskInProgress - List all tasks in progress
    9. help - Show this help message
    """
    print(helpText)

    


def add_task(taskDescription):
    
    tasks = load_tasks()
    task = {
        "id": get_next_task_id(tasks),
        "description": taskDescription,
        "status": "not done",
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added with ID: {task['id']}")

    print(f"Adding task with description: {taskDescription}")

def update_task(taskId, taskDescription):

    tasks = load_tasks()
    taskId = int(taskId)
    for task in tasks:
        if task['id'] == taskId:
            tasks.remove(task)
            tasks.append({
                "id": taskId,
                "description": taskDescription,
                "status": task['status'],
                "updated_at": datetime.now().isoformat()
            })
            save_tasks(tasks)
            print(f"Task updated with ID: {taskId}")
            return
    print(f"Task not found with ID: {taskId}")

def delete_task(taskId):
    tasks = load_tasks()
    taskId = int(taskId)
    for task in tasks:
        if task['id'] == taskId:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task deleted with ID: {taskId}")
            return
    print(f"Task not found with ID: {taskId}")


def update_task_status(taskId, status):
    tasks = load_tasks()
    taskId = int(taskId)
    for task in tasks:
        if task['id'] == taskId:
            tasks.remove(task)
            tasks.append({
                "id": taskId,
                "description": task['description'],
                "status": status,
                "updated_at": datetime.now().isoformat()
            })
            save_tasks(tasks)
            print(f"Task status updated with ID: {taskId}")
            return
    print(f"Task not found with ID: {taskId}")

def list_task_all():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

def list_task_done():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    done_tasks = [task for task in tasks if task['status'] == 'done']
    if not done_tasks:
        print("No completed tasks.")
        return

    for task in done_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}")

def list_task_not_done():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    not_done_tasks = [task for task in tasks if task['status'] == 'not done']
    if not not_done_tasks:
        print("No pending tasks.")
        return

    for task in not_done_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}")


def list_task_in_progress():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    in_progress_tasks = [task for task in tasks if task['status'] == 'in progress']
    if not in_progress_tasks:
        print("No tasks in progress.")
        return

    for task in in_progress_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}")


def main(*args):
    print("Welcome to Task Tracker CLI")

    command = args[0] if args else None
    print(f"Command received: {command}")

    commands = {
        'help': help,
        'add': add_task,
        'delete': delete_task,
        'updateStatus': update_task_status,
        'update': update_task,
        'listAll': list_task_all,
        'listDone': list_task_done,
        'listTaskNotDone': list_task_not_done,
        'listTaskInProgress': list_task_in_progress
    }

    if command in commands:
        func = commands[command]
        if len(args) > 1:
            func(*args[1:])
        else:
            func()

    elif command not in commands:
        print(f"Unknown command: {command}. Use 'help' for available commands.")
        return
    else:
        print("No command provided. Use 'help' for available commands.")
        return

    
    

if __name__ == "__main__":
    main(*sys.argv[1:]) 