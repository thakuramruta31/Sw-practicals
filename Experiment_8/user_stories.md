# Online Library Management System: User Stories

Stories below are derived only from the supplied SRS. A behavior marked **Needs confirmation** is not treated as a system requirement or a pass/fail expectation until the product owner clarifies it.

## User Stories

### US-01: Log in with registered credentials

- **SRS requirement:** FR1
- **User story:** As a registered user, I want to log in using my email address and password, so that I can access the system as an authenticated user.
- **Acceptance criteria:**
	- **Given** I am a registered user and provide the correct email address and password, **when** I submit my login credentials, **then** the system logs me in and displays a clear success message (NFR1).
	- **Given** I provide an incorrect email address or password, **when** I submit my login credentials, **then** the system does not log me in and displays an error message (FR1) that is clear (NFR1).
- **Test scenarios:**

| Type | Scenario | Expected result |
|---|---|---|
| Positive | Submit the correct email address and password for a registered user. | Login succeeds and a clear success message is displayed. |
| Negative | Submit credentials that are incorrect. | Login does not succeed and a clear error message is displayed. |

### US-02: Search for books

- **SRS requirement:** FR2
- **User story:** As a user, I want to search for books by title or author and see matching books with their availability status, so that I can find books and check whether they are available.
- **Acceptance criteria:**
	- **Given** books match a title or author search, **when** I search by title or author, **then** the system displays the matching books and each book's availability status.
	- **Given** a search operation succeeds, **when** the system displays its result, **then** it displays a clear success message (NFR1).
	- **Given** a search operation fails, **when** the system reports the failure, **then** it displays a clear failure message (NFR1).
- **Test scenarios:**

| Type | Scenario | Expected result |
|---|---|---|
| Positive | Search by a title known to match one or more books. | Matching books are displayed with their availability status. |
| Positive | Search by an author known to match one or more books. | Matching books are displayed with their availability status. |
| Negative / clarification | Search using a title or author with no matches. | The SRS does not specify whether this is a successful empty result or a failure, nor the message to display. Confirm expected behavior before making this a pass/fail test. |

### US-03: Borrow an available book

- **SRS requirement:** FR3
- **User story:** As a logged-in user, I want to borrow an available book, so that I can borrow books offered by the library.
- **Acceptance criteria:**
	- **Given** I am logged in and the selected book is available, **when** I borrow it, **then** the borrowing succeeds, the book's availability is updated, and the system displays a clear success message (NFR1).
	- **Given** I am logged in and the selected book is unavailable, **when** I attempt to borrow it, **then** the system does not allow the borrowing and displays a clear failure message (NFR1).
- **Test scenarios:**

| Type | Scenario | Expected result |
|---|---|---|
| Positive | A logged-in user borrows an available book. | Borrowing succeeds, availability is updated, and a clear success message is displayed. |
| Negative | A logged-in user attempts to borrow an unavailable book. | Borrowing is not allowed and a clear failure message is displayed. |
| Negative / clarification | A user who is not logged in attempts to borrow an available book. | FR3 limits borrowing to logged-in users, but does not specify the system response. Confirm the expected response/message. |

### US-04: Return a borrowed book

- **SRS requirement:** FR4
- **User story:** As a user, I want to return a book I have borrowed, so that the book's availability can be updated after its return.
- **Acceptance criteria:**
	- **Given** I have borrowed a book, **when** I return it successfully, **then** the system updates the book's availability and displays a clear success message (NFR1).
	- **Given** a return operation fails, **when** the system reports the failure, **then** it displays a clear failure message (NFR1).
- **Test scenarios:**

| Type | Scenario | Expected result |
|---|---|---|
| Positive | A user returns a book they have borrowed and the return succeeds. | Availability is updated and a clear success message is displayed. |
| Negative / clarification | A user attempts to return a book they have not borrowed. | The SRS does not specify whether this attempt is possible or how it is handled. Confirm the expected behavior before defining a pass/fail result. |

### US-05: View borrowing history

- **SRS requirement:** FR5
- **User story:** As a user, I want to view a list of books I have borrowed, including each book's title and borrowing status, so that I can review my borrowing history.
- **Acceptance criteria:**
	- **Given** I have borrowed books, **when** I view my borrowing history, **then** the system displays a list containing the book title and borrowing status for each listed book.
	- **Given** viewing the history succeeds, **when** the system displays the history, **then** it displays a clear success message (NFR1).
	- **Given** viewing the history fails, **when** the system reports the failure, **then** it displays a clear failure message (NFR1).
- **Test scenarios:**

| Type | Scenario | Expected result |
|---|---|---|
| Positive | A user with borrowing history views it. | The list includes each book's title and borrowing status. |
| Negative / clarification | A user with no borrowing history views it. | The SRS does not specify the empty-history presentation or whether a message is required. Confirm expected behavior. |
| Negative / clarification | The history operation fails. | NFR1 requires a clear failure message, but the cause and recovery behavior are unspecified. |

## Traceability

| SRS requirement | Requirement summary | Traceable user story/stories | Coverage |
|---|---|---|---|
| FR1 | Login using registered email and password; show an error for incorrect credentials. | US-01 | Covered |
| FR2 | Search by title or author; display matches and availability. | US-02 | Covered |
| FR3 | Logged-in users can borrow available books; update availability; disallow unavailable books. | US-03 | Covered |
| FR4 | Return borrowed books; update availability after successful return. | US-04 | Covered |
| FR5 | View borrowed-book list with title and borrowing status. | US-05 | Covered |
| NFR1 | Display clear messages when an operation succeeds or fails. | US-01, US-02, US-03, US-04, US-05 | Applied across all stories; exact message content is unspecified |

## Missing Information, Unclear Requirements, and Assumptions

| Area | Missing or unclear detail | Treatment in these stories / confirmation needed |
|---|---|---|
| FR1 | What counts as a registered user, and what happens for an unregistered email, missing fields, or account lockout? | Only correct and incorrect credentials are covered. Confirm validation and account-security behavior. |
| FR2 | Search matching rules (partial/exact, case sensitivity), combined title-and-author search, sorting, and pagination are unspecified. | No matching algorithm or result ordering is assumed. Confirm expected rules. |
| FR2 | No-match search behavior is unspecified. | Whether it is a successful empty result or a failure, and its message, needs confirmation. |
| FR3 | Borrowing limits, duplicate borrowing, concurrency, and any due date or loan duration are unspecified. | No limits, due dates, or other borrowing rules are added. Confirm which rules apply. |
| FR3 | The user-visible response for an unauthenticated borrow attempt is unspecified. | The test is flagged for clarification, not assigned an invented expected outcome. |
| FR4 | How a book is associated with the user, whether a user must be logged in to return it, and what happens on an invalid or repeated return are unspecified. | Only successful return of a borrowed book is defined; confirm identity and failure rules. |
| FR5 | “Borrowing status” values, history ordering, and whether returned books remain in history are unspecified. | Status values and ordering are not invented. Confirm expected contents and representation. |
| NFR1 | “Clear” is subjective; message wording, location, accessibility, and localization expectations are not defined. | A clear success/failure message is required, but its content and presentation need measurable criteria. |
| Cross-cutting | Authentication or authorization requirements for search, return, and history are not fully stated. | The user type is kept as “user” where the SRS does not define a login condition. Confirm access rules. |

**Assumptions:** “Registered user” means a user whose submitted email and password are accepted by the system; “available” and “unavailable” are states the system can determine; “successful” and “failed” refer to the outcome reported by the system. These terms are used as supplied and are not given additional rules here.

## Completeness Evaluation

| Dimension | Evaluation | Basis |
|---|---|---|
| Requirement coverage | Complete against the supplied list | Each FR1–FR5 has at least one story, and NFR1 is represented across all five. |
| Clarity | Partially complete | The core user goals are clear; search semantics, statuses, access rules, and message quality need definition. |
| Testability | Partially complete | Explicit behaviors have positive/negative scenarios. Several boundary cases are marked for clarification because the SRS gives no expected outcome. |
| Traceability | Complete | Each story names its source FR; the traceability table maps all functional and non-functional requirements. |

## Improvements Needed

- Define measurable message-quality criteria for NFR1, including which operations need messages and what makes a message clear.
- Specify the search matching rules and the expected result when there are no matches.
- Define authentication and authorization conditions for searching, returning books, and viewing history.
- Specify borrowing constraints and invalid/repeated borrowing behavior, including whether due dates or borrowing limits exist.
- Define valid return conditions and the behavior for returning a book that is not currently borrowed by the user.
- Define borrowing-status values and whether returned books remain in borrowing history.
- Convert the clarification items above into explicit SRS requirements before treating their tests as acceptance gates.
