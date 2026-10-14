# System Design

## 1. Application Type
Python console application that runs in the VS Code terminal.

## 2. Data Structure
A Python list will store all tasks. Each task will be represented by a dictionary containing:
- `title`: the task description.
- `completed`: a Boolean value indicating whether the task is complete.

Task numbers will be generated from the current list position, starting at 1. A separate ID field is not required.

## 3. Main Functions

### add_task(tasks, title)
- Removes leading and trailing whitespace from the title.
- Rejects empty or whitespace-only titles.
- Adds a valid task with its completion status set to `False`.
- Reports successful addition or an appropriate validation error.

### view_tasks(tasks)
- Displays each task's number, title, and completion status.
- Displays a message when the task list is empty.

### complete_task(tasks, task_number)
- Checks whether the task number is within the valid list range.
- Marks the selected task as completed.
- Reports invalid task numbers.
- Reports when a task is already completed.

### delete_task(tasks, task_number)
- Checks whether the task number is within the valid list range.
- Deletes the selected task when the number is valid.
- Reports invalid task numbers without crashing.

### main()
- Displays a numbered menu.
- Accepts the user's menu choice.
- Calls the appropriate task function.
- Handles invalid menu choices and nonnumeric task numbers.
- Continues displaying the menu after recoverable input errors.
- Exits normally when the user selects Exit.

## 4. Program Flow
1. Start the application.
2. Initialize an empty task list.
3. Display the menu.
4. Read the user's choice.
5. Perform the selected operation.
6. Display the result or an error message.
7. Repeat the menu until the user selects Exit.

## 5. Error Handling
- Empty task titles are rejected.
- Invalid menu choices produce an error message.
- Nonnumeric task numbers are handled without terminating the application.
- Task numbers outside the valid list range are rejected.
- Recoverable errors return the user to the menu.

## 6. Testing Strategy
The application will be tested using pytest.

The test cases will cover:
- Adding a task with a valid title.
- Rejecting empty and whitespace-only titles.
- Viewing tasks and handling an empty task list.
- Completing a valid task.
- Handling an invalid task number.
- Reporting repeated completion.
- Deleting a valid task.
- Handling deletion with an invalid task number.
- Handling invalid menu choices.
- Handling nonnumeric task-number input.
- Exiting the application normally.

## 7. Tools
- Python
- Visual Studio Code
- GitHub Copilot
- pytest

## 8. Design Limitations
- Tasks are stored in memory and disappear when the application exits.
- Task numbers are based on the current list position and may change after deletion.
- The application does not use a database, login system, or graphical interface.