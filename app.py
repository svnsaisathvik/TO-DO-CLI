import sys
import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_task(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"Added: {task}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks yet.")
        return
    for i, t in enumerate(todos, 1):
        status = "DONE" if t["done"] else "PENDING"
        print(f"{i}. [{status}] {t['task']}")

def mark_done(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)
        print(f"Marked as done: {todos[index]['task']}")
    else:
        print("Invalid task number.")

def delete_task(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python app.py add \"task name\"")
        print("  python app.py list")
        print("  python app.py done <task_number>")
        print("  python app.py delete <task_number>")
        return

    command = sys.argv[1]

    if command == "add":
        task = " ".join(sys.argv[2:])
        add_task(task)

    elif command == "list":
        list_tasks()

    elif command == "done":
        index = int(sys.argv[2]) - 1
        mark_done(index)

    elif command == "delete":
        index = int(sys.argv[2]) - 1
        delete_task(index)

    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
