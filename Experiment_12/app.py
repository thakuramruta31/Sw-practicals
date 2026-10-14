
def add_task(tasks, title):
    """Add a task after validating its title."""
    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return task


def view_tasks(tasks):
    """Display all tasks or an empty-list message."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} - {status}")


def complete_task(tasks, task_number):
    """Complete a task or report an invalid/repeated request."""
    if task_number < 1 or task_number > len(tasks):
        return False

    task = tasks[task_number - 1]

    if task["completed"]:
        return "already_completed"

    task["completed"] = True
    return True


def delete_task(tasks, task_number):
    """Delete a task using its current list position."""
    if task_number < 1 or task_number > len(tasks):
        return False

    tasks.pop(task_number - 1)
    return True


def main():
    """Display the menu and process user choices."""
    tasks = []

    while True:
        print("\n--- Student Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")

            try:
                add_task(tasks, title)
                print("Task added successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("No tasks available to complete.")
                continue

            try:
                number = int(input("Enter task number to complete: "))
                result = complete_task(tasks, number)

                if result == "already_completed":
                    print("Task is already completed.")
                elif result is True:
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid numeric task number.")

        elif choice == "4":
            if not tasks:
                print("No tasks available to delete.")
                continue

            try:
                number = int(input("Enter task number to delete: "))

                if delete_task(tasks, number):
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid numeric task number.")

        elif choice == "5":
            print("Exiting Student Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
