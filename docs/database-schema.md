# Database Schema

## 1. Database Overview

The Library Management System uses a relational MySQL database named:

```text
librarydb
```

The database stores all persistent information required by the application.

The main database entities are:

```text
Books
Members
Borrowing
```

The database is designed around the relationship between books, members, and borrowing transactions.

---

# 2. Database Architecture

The database architecture is:

```text
                     librarydb
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       BOOKS          MEMBERS       BORROWING
          │              │              │
          │              │              │
          └──────────────┼──────────────┘
                         │
                         ▼
                  Library Operations
```

The `borrowing` table connects the `books` and `members` tables.

---

# 3. Entity Relationship Diagram

```text
┌─────────────────────────┐
│         BOOKS           │
├─────────────────────────┤
│ PK  book_id             │
│     title               │
│     author              │
│     genre               │
│     published_year      │
│     is_available        │
└────────────┬────────────┘
             │
             │ 1
             │
             │ N
┌────────────▼────────────┐
│       BORROWING         │
├─────────────────────────┤
│ PK  loan_id             │
│ FK  book_id             │
│ FK  member_id           │
│     borrow_date         │
│     return_date         │
│     librarian_id        │
└────────────┬────────────┘
             │
             │ N
             │
             │ 1
┌────────────▼────────────┐
│        MEMBERS          │
├─────────────────────────┤
│ PK  member_id           │
│     name                │
│     email               │
│     phone_number        │
│     join_date           │
└─────────────────────────┘
```

---

# 4. Tables

The database contains three main tables:

| Table       | Purpose                              |
| ----------- | ------------------------------------ |
| `books`     | Stores library book information      |
| `members`   | Stores registered member information |
| `borrowing` | Stores book borrowing transactions   |

---

# 5. Books Table

The `books` table stores information about every book in the library.

## Structure

```text
books
├── book_id
├── title
├── author
├── genre
├── published_year
└── is_available
```

## SQL Definition

```sql
CREATE TABLE books (
    book_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100) DEFAULT NULL,
    published_year INT DEFAULT NULL,
    is_available TINYINT(1) DEFAULT 1,
    PRIMARY KEY (book_id)
);
```

---

# 6. Books Columns

| Column           | Type         | Null | Key | Description                 |
| ---------------- | ------------ | ---- | --- | --------------------------- |
| `book_id`        | INT          | NO   | PK  | Unique book identifier      |
| `title`          | VARCHAR(255) | NO   |     | Book title                  |
| `author`         | VARCHAR(255) | NO   |     | Book author                 |
| `genre`          | VARCHAR(100) | YES  |     | Book category               |
| `published_year` | INT          | YES  |     | Publication year            |
| `is_available`   | TINYINT(1)   | YES  |     | Current availability status |

---

# 7. `book_id`

`book_id` is the primary key of the `books` table.

It uniquely identifies each book.

Example:

```text
book_id = 1
```

Because the column uses:

```sql
AUTO_INCREMENT
```

MySQL automatically generates a new identifier when a book is inserted.

---

# 8. `title`

Stores the title of the book.

Example:

```text
The Great Gatsby
```

The field is required:

```sql
title VARCHAR(255) NOT NULL
```

---

# 9. `author`

Stores the author of the book.

Example:

```text
George Orwell
```

The field is required.

---

# 10. `genre`

Stores the category or genre of the book.

Examples:

```text
Fiction
Dystopian
Classic
Fantasy Adventure
Programming
```

The field is optional.

---

# 11. `published_year`

Stores the publication year.

Example:

```text
1925
```

The project uses an `INT` field so that publication years can be stored as numeric values.

---

# 12. `is_available`

Stores the current availability state of a book.

The application uses:

```text
1 = Available
0 = Borrowed
```

Example:

```text
is_available = 1
```

means the book can be borrowed.

```text
is_available = 0
```

means the book is currently borrowed.

---

# 13. Members Table

The `members` table stores information about library members.

## Structure

```text
members
├── member_id
├── name
├── email
├── phone_number
└── join_date
```

## SQL Definition

```sql
CREATE TABLE members (
    member_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) DEFAULT NULL,
    phone_number VARCHAR(15) DEFAULT NULL,
    join_date DATE DEFAULT NULL,
    PRIMARY KEY (member_id)
);
```

---

# 14. Members Columns

| Column         | Type         | Null | Key | Description              |
| -------------- | ------------ | ---- | --- | ------------------------ |
| `member_id`    | INT          | NO   | PK  | Unique member identifier |
| `name`         | VARCHAR(255) | NO   |     | Member name              |
| `email`        | VARCHAR(255) | YES  |     | Member email             |
| `phone_number` | VARCHAR(15)  | YES  |     | Member phone number      |
| `join_date`    | DATE         | YES  |     | Date the member joined   |

---

# 15. `member_id`

`member_id` is the primary key of the `members` table.

It uniquely identifies each member.

Example:

```text
member_id = 1
```

The value is automatically generated by MySQL.

---

# 16. `name`

Stores the member's name.

Example:

```text
John Smith
```

The field is required.

---

# 17. `email`

Stores the member's email address.

Example:

```text
johnsmith@example.com
```

The field is optional in the current database design.

---

# 18. `phone_number`

Stores the member's phone number.

Example:

```text
0612345680
```

The field uses `VARCHAR` instead of an integer because phone numbers are identifiers rather than numbers used for mathematical calculations.

This also allows leading zeros to be preserved.

---

# 19. `join_date`

Stores the date on which the member joined the library.

Example:

```text
2026-09-26
```

The field uses the MySQL `DATE` data type.

---

# 20. Borrowing Table

The `borrowing` table stores transactions between books and members.

## Structure

```text
borrowing
├── loan_id
├── book_id
├── member_id
├── borrow_date
├── return_date
└── librarian_id
```

## SQL Definition

```sql
CREATE TABLE borrowing (
    loan_id INT NOT NULL AUTO_INCREMENT,
    book_id INT DEFAULT NULL,
    member_id INT DEFAULT NULL,
    borrow_date DATE DEFAULT NULL,
    return_date DATE DEFAULT NULL,
    librarian_id INT DEFAULT NULL,
    PRIMARY KEY (loan_id),
    CONSTRAINT fk_borrowing_book
        FOREIGN KEY (book_id)
        REFERENCES books(book_id),
    CONSTRAINT fk_borrowing_member
        FOREIGN KEY (member_id)
        REFERENCES members(member_id)
);
```

---

# 21. Borrowing Columns

| Column         | Type | Null | Key | Description                  |
| -------------- | ---- | ---- | --- | ---------------------------- |
| `loan_id`      | INT  | NO   | PK  | Unique borrowing identifier  |
| `book_id`      | INT  | YES  | FK  | References the borrowed book |
| `member_id`    | INT  | YES  | FK  | References the member        |
| `borrow_date`  | DATE | YES  |     | Date the book was borrowed   |
| `return_date`  | DATE | YES  |     | Date the book was returned   |
| `librarian_id` | INT  | YES  |     | Identifier for a librarian   |

---

# 22. `loan_id`

`loan_id` is the primary key of the `borrowing` table.

It uniquely identifies every borrowing transaction.

Example:

```text
loan_id = 3
```

---

# 23. `book_id` Foreign Key

The `book_id` column in `borrowing` references:

```text
books.book_id
```

Relationship:

```text
borrowing.book_id
        │
        ▼
books.book_id
```

This identifies which book was borrowed.

---

# 24. `member_id` Foreign Key

The `member_id` column in `borrowing` references:

```text
members.member_id
```

Relationship:

```text
borrowing.member_id
        │
        ▼
members.member_id
```

This identifies which member borrowed the book.

---

# 25. `borrow_date`

Stores the date when the borrowing transaction was created.

Example:

```text
2026-09-26
```

The application uses the current database date when a book is borrowed.

---

# 26. `return_date`

Stores the date when a book is returned.

For an active loan:

```text
return_date = NULL
```

For a returned loan:

```text
return_date = 2026-09-26
```

Therefore:

```text
NULL       → Active loan
Date value → Returned loan
```

---

# 27. `librarian_id`

The `librarian_id` column is reserved for identifying the librarian responsible for a transaction.

The current application does not yet implement a separate librarian/user table.

This field provides a foundation for future authentication and role-management features.

---

# 28. Primary Keys

The database contains three primary keys.

```text
books.book_id
members.member_id
borrowing.loan_id
```

Primary keys provide unique identification for records.

```text
BOOKS
PK → book_id

MEMBERS
PK → member_id

BORROWING
PK → loan_id
```

---

# 29. Foreign Keys

The borrowing table contains two foreign keys.

```text
borrowing.book_id
        ↓
books.book_id
```

and:

```text
borrowing.member_id
        ↓
members.member_id
```

These relationships connect transactions to real books and members.

---

# 30. Relationship Between Books and Borrowing

One book can have multiple borrowing records over time.

For example:

```text
The Hobbit
    │
    ├── Loan 1
    ├── Loan 5
    ├── Loan 12
    └── Loan 20
```

Therefore:

```text
One Book
   │
   └── Many Borrowing Records
```

This is a:

```text
1 : N
```

relationship.

---

# 31. Relationship Between Members and Borrowing

One member can borrow multiple books over time.

Example:

```text
John Smith
    │
    ├── Loan 3
    ├── Loan 8
    ├── Loan 14
    └── Loan 21
```

Therefore:

```text
One Member
   │
   └── Many Borrowing Records
```

This is also a:

```text
1 : N
```

relationship.

---

# 32. Overall Relationship

The database can therefore be represented as:

```text
BOOKS
  │
  │ 1
  │
  │ N
  ▼
BORROWING
  ▲
  │ N
  │
  │ 1
MEMBERS
```

The `borrowing` table acts as the transaction table connecting books and members.

---

# 33. Borrowing Lifecycle

A borrowing transaction follows this lifecycle:

```text
Book Available
      │
      ▼
Member selects book
      │
      ▼
Borrowing record created
      │
      ▼
return_date = NULL
      │
      ▼
Book becomes unavailable
      │
      ▼
Book is returned
      │
      ▼
return_date is populated
      │
      ▼
Book becomes available
```

---

# 34. Example Active Loan

Example database state:

```text
borrowing
----------------------------------------
loan_id       1
book_id       1
member_id     1
borrow_date   2026-09-20
return_date   NULL
```

This means:

```text
Book #1
was borrowed by
Member #1
on 2026-09-20
and has not yet been returned.
```

The corresponding book should have:

```text
is_available = 0
```

---

# 35. Example Returned Loan

Example:

```text
borrowing
----------------------------------------
loan_id       2
book_id       2
member_id     2
borrow_date   2026-08-10
return_date   2026-08-15
```

This means the book was borrowed on:

```text
2026-08-10
```

and returned on:

```text
2026-08-15
```

The book can therefore be available for another borrowing transaction.

---

# 36. Data Integrity

The database uses several mechanisms to maintain data integrity.

## Primary Keys

Prevent duplicate identifiers.

## Foreign Keys

Maintain relationships between tables.

## NOT NULL

Required fields cannot be empty.

## AUTO_INCREMENT

Automatically generates unique identifiers.

## InnoDB

Provides transaction support and foreign-key functionality.

---

# 37. Character Set

The tables use:

```text
utf8mb4
```

This provides support for a broad range of characters and international text.

Example database configuration:

```sql
DEFAULT CHARSET=utf8mb4;
```

---

# 38. Storage Engine

The tables use:

```text
InnoDB
```

Example:

```sql
ENGINE=InnoDB
```

InnoDB supports:

* Transactions
* Foreign keys
* Reliable data storage
* Transaction rollback

These capabilities are useful for operations such as borrowing and returning books.

---

# 39. Database Scripts

The database setup is divided into separate SQL files.

```text
sql/
│
├── 01_create_database.sql
├── 02_create_tables.sql
├── 03_insert_data.sql
├── 04_queries.sql
└── 05_advanced_queries.sql
```

---

# 40. Script 01 — Create Database

File:

```text
sql/01_create_database.sql
```

Purpose:

```text
Create librarydb
Select librarydb
```

---

# 41. Script 02 — Create Tables

File:

```text
sql/02_create_tables.sql
```

Purpose:

```text
Create books
Create members
Create borrowing
Create relationships
```

---

# 42. Script 03 — Insert Data

File:

```text
sql/03_insert_data.sql
```

Purpose:

```text
Insert sample books
Insert sample members
Insert sample borrowing records
```

---

# 43. Script 04 — Basic Queries

File:

```text
sql/04_queries.sql
```

Contains queries for:

* Viewing books
* Viewing members
* Viewing borrowing records
* Available books
* Borrowed books
* Books by genre
* Books by publication year
* Counts
* Active loans
* Returned books
* Borrowing history

---

# 44. Script 05 — Advanced Queries

File:

```text
sql/05_advanced_queries.sql
```

Contains more advanced reporting queries, including:

* Complete borrowing reports
* Current loans
* Member borrowing history
* Books never borrowed
* Most borrowed books
* Books by year range
* Title searches
* Members by join year
* Aggregated borrowing statistics
* Availability status
* Dashboard statistics

---

# 45. Example SQL Queries

## View All Books

```sql
SELECT *
FROM books;
```

## View Available Books

```sql
SELECT *
FROM books
WHERE is_available = 1;
```

## View Borrowed Books

```sql
SELECT *
FROM books
WHERE is_available = 0;
```

## View All Members

```sql
SELECT *
FROM members;
```

## View Active Loans

```sql
SELECT *
FROM borrowing
WHERE return_date IS NULL;
```

---

# 46. Borrowing Report

A complete borrowing report can join all three tables:

```sql
SELECT
    b.title,
    m.name AS member_name,
    br.borrow_date,
    br.return_date
FROM borrowing br
JOIN books b
    ON br.book_id = b.book_id
JOIN members m
    ON br.member_id = m.member_id;
```

This produces a report containing:

```text
Book
Member
Borrow Date
Return Date
```

---

# 47. Current Database Flow

The application interacts with the database through the following process:

```text
User Action
    │
    ▼
Flask Route
    │
    ▼
Validation
    │
    ▼
SQL Query
    │
    ▼
MySQL
    │
    ▼
Result
    │
    ▼
Flask
    │
    ▼
Jinja2 Template
    │
    ▼
Browser
```

---

# 48. Database and Backend Relationship

The backend uses the database connection defined in:

```text
database.py
```

The connection is used by Flask routes to execute SQL operations.

Conceptually:

```text
app.py
   │
   ▼
get_db_connection()
   │
   ▼
MySQL Connector
   │
   ▼
librarydb
```

---

# 49. Database and Frontend Relationship

The frontend never directly connects to MySQL.

Instead:

```text
Frontend
    │
    ▼
Flask
    │
    ▼
Database
```

When data is retrieved:

```text
Database
    │
    ▼
Flask
    │
    ▼
Jinja2
    │
    ▼
HTML
    │
    ▼
Browser
```

This separation keeps database credentials and SQL operations on the server side.

---

# 50. Database Design Summary

The database can be summarized as:

```text
┌─────────────────┐
│      BOOKS      │
│                 │
│ PK book_id      │
│ title           │
│ author          │
│ genre           │
│ published_year  │
│ is_available    │
└────────┬────────┘
         │
         │
         ▼
┌─────────────────┐
│    BORROWING    │
│                 │
│ PK loan_id      │
│ FK book_id      │
│ FK member_id    │
│ borrow_date     │
│ return_date     │
│ librarian_id    │
└────────┬────────┘
         │
         │
         ▼
┌─────────────────┐
│     MEMBERS     │
│                 │
│ PK member_id    │
│ name            │
│ email           │
│ phone_number    │
│ join_date       │
└─────────────────┘
```

---

# 51. Future Database Improvements

The current database provides the foundation for the application.

Future versions could introduce additional tables.

## Users

```text
users
├── user_id
├── username
├── email
├── password_hash
└── role
```

## Authors

A separate authors table could normalize author information.

```text
authors
├── author_id
└── name
```

Books could then reference authors using a foreign key.

## Categories

A separate categories table could replace the current text-based genre field.

```text
categories
├── category_id
└── name
```

## Reservations

A reservation system could be added:

```text
reservations
├── reservation_id
├── book_id
├── member_id
├── reservation_date
└── status
```

## Fines

A future version could track overdue fines:

```text
fines
├── fine_id
├── loan_id
├── amount
├── issued_date
└── status
```

---

# 52. Future Database Architecture

A larger production system could eventually use:

```text
                        LIBRARY DATABASE
                              │
       ┌──────────┬───────────┼───────────┬───────────┐
       │          │           │           │           │
       ▼          ▼           ▼           ▼           ▼
     Users      Books       Authors     Members    Categories
       │          │                       │
       │          └──────────┬────────────┘
       │                     │
       ▼                     ▼
    Roles              Borrowing
                             │
                   ┌─────────┼─────────┐
                   ▼         ▼         ▼
              Reservations  Fines   Returns
```

This would allow the application to support more advanced library operations.

---

# 53. Conclusion

The MySQL database provides the foundation of the Library Management System.

Its main responsibilities are:

```text
Store Data
    ↓
Maintain Relationships
    ↓
Protect Data Integrity
    ↓
Support Transactions
    ↓
Provide Data to Flask
    ↓
Support Reports and Statistics
```

The three core tables:

```text
books
members
borrowing
```

provide the relational structure required for the current application.

The database is separated from the frontend and backend, allowing the system to evolve toward a larger production architecture without changing the fundamental data model.
