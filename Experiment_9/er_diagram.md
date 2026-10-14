# AI-Generated ER Diagram

```mermaid
erDiagram
    USER ||--o{ BORROWING : makes
    BOOK ||--o{ BORROWING : appears_in

    USER {
        int user_id PK
        string name
        string email
    }

    BOOK {
        int book_id PK
        string title
        string author
        string availability_status
    }

    BORROWING {
        int borrowing_id PK
        int user_id FK
        int book_id FK
        date borrowing_date
        date return_date
        string status
    }
```

## Explanation

- USER stores user details.
- BOOK stores book details and availability.
- BORROWING stores each borrowing transaction.
- PK means Primary Key.
- FK means Foreign Key.
- One user can have multiple borrowing records.
- One book can appear in multiple borrowing records over time.
- Each borrowing record belongs to one user and one book.