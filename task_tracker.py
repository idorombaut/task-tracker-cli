import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Load tasks and counter from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return [], 0
    try:
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)
            return data.get("tasks", []), data.get("counter", 0)
    except json.JSONDecodeError:
        return [], 0
    
# Generate tasks and counter to JSON file
def save_tasks(tasks, counter):
    with open(TASKS_FILE, "w") as file:
        json.dump({"tasks": tasks, "counter": counter}, file, indent=4)

# Generate a new task ID
def generate_task_id(counter):
    return counter + 1

# Add a new task
def add_task(description):
    tasks, counter = load_tasks()
    new_task_id = generate_task_id(counter)
    new_task = {
        "id": new_task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    counter += 1
    save_tasks(tasks, counter)
    print(f"Task added successfully (ID: {new_task['id']})")

# Update an existing task
def update_task(task_id, new_description):
    tasks, counter = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks, counter)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

# Delete a task
def delete_task(task_id):
    tasks, counter = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"Task {task_id} not found")
    else:
        save_tasks(updated_tasks, counter)
        print(f"Task {task_id} deleted successfully")

# Mark a task as in-progress
def mark_in_progress(task_id):
    tasks, counter = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] != "done":
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().isoformat()
                save_tasks(tasks, counter)
                print(f"Task {task_id} marked as in-progress")
                return
            else:
                print(f"Task {task_id} is already completed (done)")
                return
    print(f"Task {task_id} not found")

# Mark a task as done
def mark_done(task_id):
    tasks, counter = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks, counter)
            print(f"Task {task_id} marked as done")
            return
    print(f"Task {task_id} not found")

# List tasks, optionally by status
def list_tasks(status=None):
    tasks, counter = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, \
                  Created: {task['createdAt']}, Last Updated: {task['updatedAt']}")
    else:
        print("No tasks found")

# Command-line argument handling
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli [add|update|delete|mark-in-progress|mark-done|list] ...")
        return
    
    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])

    elif command == "update" and len(sys.argv) == 4:
        try:
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)
        except ValueError:
            print("Invalid task ID")

    elif command == "delete" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Invalid task ID")
        
    elif command == "mark-in-progress" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_in_progress(task_id)
        except ValueError:
            print("Invalid task ID")
        
    elif command == "mark-done" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("Invalid task ID")
        
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3:
            status = sys.argv[2]
            if status in ["todo", "in-progress", "done"]:
                list_tasks(status)
            else:
                print("Invalid status. Use one of 'todo', 'in-progress', 'done'")
        else:
            print("Usage: task-cli list [status]")
        
    else:
        print("Invalid command or arguments")

if __name__ == "__main__":
    main()
