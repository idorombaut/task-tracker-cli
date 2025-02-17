# Task Tracker CLI

## Overview
A simple command-line task management tool to manage your tasks and their status using a local JSON file for storage.

## Features
- **Add tasks**: Create new tasks with descriptions.
- **Update tasks**: Edit the description of an existing task.
- **Delete tasks**: Remove tasks by ID.
- **Change task status**: Mark tasks as "in-progress" or "done".
- **List tasks**: View tasks filtered by status or all tasks.

## Usage
The tool works by executing commands in the terminal. The commands are as follows:

1. Add a Task
   ```
   python task_tracker.py add "Your task description"
   ```
2. Update a Task
   ```
   python task_tracker.py update <task_id> "New description"
   ```
3. Delete a Task
   ```
   python task_tracker.py delete <task_id>
   ```
4. Mark a Task as In-Progress
   ```
   python task_tracker.py mark-in-progress <task_id>
   ```
5. Mark a Task as Done
   ```
   python task_tracker.py mark-done <task_id>
   ```
6. List Tasks  
   To list all tasks:
   ```
   python task_tracker.py list
   ```
   To list tasks by status (e.g., only "todo", "in-progress", or "done"):
   ```
   python task_tracker.py list <status>
   ```
