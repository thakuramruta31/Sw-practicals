# Software Requirements

## 1. Functional Requirements

**FR1: Add Task**  
The application shall allow the user to add a task by entering a title. It shall remove leading and trailing whitespace from the title before saving it.

**FR2: View Tasks**  
The application shall display each task's number, title, and completion status. If no tasks exist, it shall display a message indicating that the task list is empty.

**FR3: Complete Task**  
The application shall allow the user to mark a task as completed by entering its task number. If the task number is invalid, the application shall display an error message.

**FR4: Delete Task**  
The application shall allow the user to delete a task by entering its task number. If the task number is invalid, the application shall display an error message.

**FR5: Exit Application**  
The application shall exit normally when the user selects the exit option from the menu.

**FR6: Validate Task Titles**  
The application shall reject titles that are empty or contain only whitespace and display an appropriate error message.

**FR7: Handle Invalid Input**  
The application shall handle nonnumeric task numbers and invalid menu choices without crashing. It shall display an appropriate error message and allow the user to continue.

**FR8: Handle Repeated Completion**  
If the user marks an already completed task as completed, the application shall continue running and display an appropriate message.

## 2. Non-Functional Requirements

**NFR1: Usability**  
The application shall display a numbered menu and prompts that explain the input expected from the user.

**NFR2: Maintainability**  
The code shall use separate functions for task operations and menu handling wherever practical.

**NFR3: Feedback**  
The application shall display a message indicating the outcome of each operation, including success or an error.

**NFR4: Reliability**  
Invalid input shall not cause the application to terminate unexpectedly.

## 3. Constraints

- The application shall be developed using Python.
- It shall run in the VS Code terminal.
- Tasks shall be stored in memory using a Python list.
- No database, login system, or graphical interface is required.
- Tasks shall not be preserved after the application exits.

## 4. Testing Criteria

- Verify that a task with a valid title can be added.
- Verify that empty and whitespace-only titles are rejected.
- Verify that tasks can be displayed with their completion status.
- Verify the message shown when the task list is empty.
- Verify that valid tasks can be completed and deleted.
- Verify that invalid task numbers and menu choices are handled.
- Verify that completing an already completed task does not crash the application.
- Verify that the application exits when the exit option is selected.