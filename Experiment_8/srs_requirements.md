# Software Requirements Specification (SRS)

## Project: Online Library Management System

### Functional Requirements

**FR1: User Login**

The system shall allow registered users to log in using their email address and password. If the credentials are incorrect, the system shall display an error message.

**FR2: Search Books**

The system shall allow users to search for books by title or author. The system shall display matching books with their availability status.

**FR3: Borrow Books**

Logged-in users shall be able to borrow available books. The system shall update the book's availability after successful borrowing. Unavailable books cannot be borrowed.

**FR4: Return Books**

Users shall be able to return borrowed books. After a successful return, the system shall update the book's availability.

**FR5: View Borrowing History**

Users shall be able to view a list of books they have borrowed, including the book title and borrowing status.

### Non-Functional Requirement

**NFR1: Usability**

The system shall display clear messages when an operation succeeds or fails.