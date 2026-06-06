from storage import load_tasks, save_tasks


#Task-1 :Add task
def add_task():
    tasks = load_tasks()

    task = input("Enter task to add: ").strip()

    # Duplicate check
    if any(t["task"].lower() == task.lower() for t in tasks ):
        print(
            "Task already exists "
            "in the to-do list."
        )
        return

    status = input("Enter status " "(pending/completed): ").lower().strip()

    try:

        # Empty task check
        if task == "":
            raise ValueError("Task cannot be empty.")

        # Status validation
        if status not in [
            "pending",
            "completed"
        ]:
            raise ValueError("Status must be "
                "'pending' or "
                "'completed'."
            )

    except ValueError as e:
        print(e)

    else:
        priority = input(
        "Enter priority "
        "(high/medium/low): "
    ).lower().strip()

    if priority not in [
        "high",
        "medium",
        "low"
    ]:
        print(
            "Invalid priority."
        )
        return
    due_date = input(
    "Enter due date "
    "(DD Month): "
    ).strip()

    tasks.append({
        "task": task,
        "status": status,
        "priority": priority,
        "due_date": due_date
    })

    save_tasks(tasks)

    print("Task added successfully!")

#Task-2 :View tasks
def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, start=1):

        print(
            f"{i}. "
            f"{task['task']} "
            f"[{task['status']}]"
            f"Priority: "
            f"{task['priority']}"
            f"Due Date: "
            f"{task['due_date']}"
        )
        
#task: update tasks
def update_task(index):

    tasks = load_tasks()

    if 0 <= index < len(tasks):

        new_task = input(
            "Enter new task name: "
        ).strip()

        new_status = input(
            "Enter new status "
            "(pending/completed): "
        ).strip().lower()
        
        new_priority = input(
        "Enter new priority "
        "(high/medium/low): "
        ).lower().strip()
        
        new_due_date = input(
        "Enter new due date: "
        ).strip()

        tasks[index]["task"] = new_task
        tasks[index]["status"] = new_status
        tasks[index]["priority"] = new_priority
        tasks[index]["due_date"] = new_due_date
        save_tasks(tasks)

        print(
            "Task updated successfully!"
        )

    else:
        print(
            "Invalid task number."
        )

#Task-4 :Remove task
def delete_task():

    tasks = load_tasks()

    try:
        task_num = int(
            input(
                "Enter task number to remove: "
            )
        )

        if (
            task_num < 1
            or task_num > len(tasks)
        ):
            raise IndexError(
                "Invalid task number."
            )

    except ValueError:
        print(
            "Please enter a valid number."
        )

    except IndexError as e:
        print(e)

    else:

        removed_task = tasks.pop(
            task_num - 1
        )

        save_tasks(tasks)

        print(
            f"Task "
            f"'{removed_task['task']}' "
            f"removed successfully!"
        )
        
#Task-5 :Mark Task as Completed by adding status pending or completed
def mark_completed():

    tasks = load_tasks()

    try:

        task_num = int(
            input(
                "Enter task number: "
            )
        )

        if (
            task_num < 1
            or task_num > len(tasks)
        ):
            raise IndexError(
                "Invalid task number."
            )

    except ValueError:
        print(
            "Please enter a valid number."
        )

    except IndexError as e:
        print(e)

    else:

        status = input(
            "Enter status "
            "(pending/completed): "
        ).lower().strip()

        if status not in [
            "pending",
            "completed"
        ]:
            print(
                "Invalid status."
            )

        else:

            tasks[
                task_num - 1
            ]["status"] = status

            save_tasks(tasks)

            print(
                f"{task_num}. "
                f"'{tasks[task_num - 1]['task']}' "
                f"marked as "
                f"{status}!"
            )
#task-6 :search task

def search_task():

    tasks = load_tasks()

    keyword = input(
        "Enter task to search: "
    ).lower().strip()

    found = False

    print("\nSearch Results:")

    for i, task in enumerate(
        tasks,
        start=1
    ):

        if keyword in (
            task["task"]
            .lower()
        ):

            print(
                f"{i}. "
                f"{task['task']} "
                f"[{task['status']}]"
            )

            found = True

    if not found:
        print(
            "No matching task found."
        )
        
def show_statistics():

    tasks = load_tasks()

    total_tasks = len(tasks)

    completed_tasks = sum(
        1
        for task in tasks
        if task["status"] == "completed"
    )

    pending_tasks = sum(
        1
        for task in tasks
        if task["status"] == "pending"
    )

    print("\n===== TASK STATISTICS =====")

    print(
        f"Total Tasks: "
        f"{total_tasks}"
    )

    print(
        f"Completed Tasks: "
        f"{completed_tasks}"
    )

    print(
        f"Pending Tasks: "
        f"{pending_tasks}"
    )
