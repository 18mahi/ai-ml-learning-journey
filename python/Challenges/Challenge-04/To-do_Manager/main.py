from task_manager import *
def menu():
    def menu():
        print("\nTO-DO MENU")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Tasks")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Search Task")
        print("7. Show Statistics")
        print("8. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index=int(input("Enter task number to update: "))
        update_task(index-1)
        task_num = int(input("Enter task number to delete: "))
        delete_task(task_num - 1)
    elif choice == '4':
        view_tasks()
        task_num = int(input("Enter task number to delete: "))
        delete_task(task_num - 1)
    elif choice == '5':
        mark_completed()
    elif choice == '6':
        search_task()
    elif choice == '7':
        show_statistics()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
