import json
import os

TODO_FILE = 'todo_list.json'
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({'task': task, 'status': 'pending'})
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['task']} - {task['status']}")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_no < len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_no]['task'] = new_task
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks.pop(task_no)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]['status'] = 'completed'
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
