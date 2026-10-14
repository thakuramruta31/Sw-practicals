# Project Planning

## Project Title
Student Task Manager

## Problem Statement
Students need a simple application to organize and track their daily tasks.

## Objective
To develop a Python console application that allows students to add, view, complete, and delete tasks.

## Main Features
- Add a task with a required title.
- View all tasks with their task numbers and completion status.
- Mark a task as completed.
- Delete a task.
- Handle invalid menu choices and task numbers without crashing.
- Display a message if a task is already completed.

## Scope
The application will run in the VS Code terminal. Tasks will be stored in memory while the application is running.

Each task will contain:
- Task title
- Completion status

Task numbers will be generated from the current list position, starting at 1. Task numbers may change after a task is deleted.

The application will not include a database, user accounts, deadlines, priorities, or a graphical interface.

## Tools
- Python
- Visual Studio Code
- GitHub Copilot
- pytest

## Risks and Limitations
- Tasks will be lost when the application exits.
- Invalid input may cause errors if it is not handled properly.
- Separate functions make the code easier to test and maintain.
- Adding unnecessary features may increase project complexity.

## Development Plan
1. Define the task fields and expected behavior.
2. Implement and test the add-task and view-task functions.
3. Implement complete-task and delete-task functions.
4. Create a terminal menu to connect all functions.
5. Handle invalid input and repeated completion.
6. Test the application using pytest.
7. Document the project and its limitations in the README.

## AI Assistance
GitHub Copilot will assist with planning, requirements analysis, design, development, testing, debugging, and documentation. Its suggestions will be reviewed before being accepted.