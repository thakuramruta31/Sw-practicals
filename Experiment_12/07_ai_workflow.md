# AI-Assisted Software Development Workflow

## Project Title
Student Task Manager

## AI Tool Used
GitHub Copilot

## 1. Planning
GitHub Copilot was asked to review the project plan and suggest suitable features, scope, risks, and a development sequence.

## 2. Requirements Analysis
Copilot reviewed the software requirements and suggested clearer validation rules, error handling, and testable behavior.

## 3. Design
Copilot reviewed the application design, task data structure, function responsibilities, and testing strategy.

## 4. Development
Copilot assisted with reviewing the Python implementation and identifying missing behavior, including handling repeated task completion.

## 5. Testing
Pytest was used to test task creation, empty titles, viewing an empty list, task completion, repeated completion, invalid task numbers, and task deletion.

## 6. Debugging
The code review identified an issue with repeated completion. The implementation was updated to return a separate result for an already completed task.

## 7. Documentation
The planning, requirements, design, debugging, workflow, and README files document the development process and project limitations.

## Evaluation of AI Assistance
Copilot suggestions were reviewed against the project requirements. The suggested changes were incorporated where appropriate.

## Final Outcome
The Student Task Manager was implemented as a Python console application. The latest recorded pytest result was 8 passed in 0.28 seconds.

## Limitations
Tasks are stored in memory and are lost when the application exits. The application does not use a database, login system, or graphical interface.