import os
import json
from app import add_task, load_todos, save_todos, delete_task, mark_done

TODO_FILE = "todos.json"

def setup_function():
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)

def test_add_task():
    add_task("Buy milk")
    todos = load_todos()
    assert len(todos) == 1
    assert todos[0]["task"] == "Buy milk"

def test_mark_done():
    add_task("Study")
    mark_done(0)
    todos = load_todos()
    assert todos[0]["done"] is True

def test_delete_task():
    add_task("Task 1")
    add_task("Task 2")
    delete_task(0)
    todos = load_todos()
    assert len(todos) == 1
    assert todos[0]["task"] == "Task 2"
