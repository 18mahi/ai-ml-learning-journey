# TO-DO Manager

print("Welcome to the TO-DO Manager!")
print("You can add, view, and remove tasks from your to-do list.")

#Task-1 :Add task
tasks = []
task = input("Enter task to add: ")
try:
    if task == "":
        raise ValueError("Task cannot be empty.")
except ValueError as e:
    print(e)
else:
    tasks.append(f"task: {task}")
    print("Task added successfully!")

#Task-2 :View tasks
if not tasks:
    print("No tasks in the to-do list.")
else:
    print("Tasks to do: ")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

#Task-3 :Remove task
try:
    task_num = int(input("Enter task number to remove: "))
    if task_num < 1 or task_num > len(tasks):
        raise IndexError("Invalid task number.")
except ValueError:
    print("Please enter a valid number.")
except IndexError as e:
    print(e)
else:
    removed_task = tasks.pop(task_num - 1)
    print(f"Task '{removed_task}' removed successfully!")

#Task-4 :Mark Task as Completed by adding status pending or completed
try:
    task_num = int(input("Enter task number to mark as completed: "))
    if task_num < 1 or task_num > len(tasks):
        raise IndexError("Invalid task number.")
except ValueError:
    print("Please enter a valid number.")
except IndexError as e:
    print(e)
else:
    status= input("Enter status (pending/completed): ").lower()
    if status not in ["pending", "completed"]:
        print("Invalid status. Please enter 'pending' or 'completed'.")
    else:
        tasks[task_num - 1] += f" - {status.capitalize()}"
        print(f"Task '{tasks[task_num - 1]}' marked as {status}!")
