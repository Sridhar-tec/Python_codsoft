todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark as Completed")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for idx, task in enumerate(todo_list, 1):
            status = " Done" if task["completed"] else " Not Done"
            print(f"{idx}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task name: ")
    task = {"title": title, "completed": False}
    todo_list.append(task)
    print("Task added successfully.")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: ")) - 1
        if 0 <= task_no < len(todo_list):
            new_title = input("Enter new task name: ")
            todo_list[task_no]["title"] = new_title
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(todo_list):
            del todo_list[task_no]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list[task_no]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_completed()
    elif choice == '6':
        print("Thank you for using To-Do List App!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
