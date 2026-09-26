# Development Process

## 1. Project Introduction

The Library Management System was developed as a full-stack web application for managing the main operations of a library.

The system combines:

* MySQL for data storage
* SQL for database operations and reporting
* Python for application logic
* Flask for the web backend
* Jinja2 for server-side HTML rendering
* HTML and CSS for the frontend
* Git and GitHub for version control and project documentation

The development process was organized into multiple stages, starting with database design and continuing through backend development, frontend development, testing, and documentation.

---

# 2. Development Architecture

The application follows a layered architecture:

```text
                    LIBRARY MANAGEMENT SYSTEM
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
          FRONTEND         BACKEND         DATABASE
              │               │               │
          HTML/CSS          Flask           MySQL
          Jinja2            Python          SQL
              │               │               │
              └───────────────┼───────────────┘
                              │
                              ▼
                         APPLICATION
```

The frontend communicates with the Flask backend, while the backend communicates with MySQL.

---

# 3. Phase 1 — Requirements and System Planning

The first stage was to identify the main operations required by the library.

The system needed to support:

* Book management
* Member management
* Borrowing
* Returning books
* Availability tracking
* Search
* Dashboard statistics
* Borrowing history

The main entities were identified as:

```text
Books
Members
Borrowing
```

The borrowing table was designed as the connection between books and members.

---

# 4. Phase 2 — Database Design

The MySQL database was designed before implementing the web interface.

The database is called:

```text
librarydb
```

The main tables are:

```text
books
members
borrowing
```

The relationships are:

```text
BOOKS
  │
  │ book_id
  ▼
BORROWING
  ▲
  │ member_id
  │
MEMBERS
```

This relational structure allows borrowing transactions to connect a specific book with a specific member.

---

# 5. Phase 3 — Database Creation

The first SQL script creates the database:

```text
sql/01_create_database.sql
```

The script contains the database creation logic and selects the database for subsequent operations.

---

# 6. Phase 4 — Table Creation

The second SQL script creates the application tables:

```text
sql/02_create_tables.sql
```

The following tables are created:

```text
books
members
borrowing
```

Primary keys and foreign keys are also defined.

The database uses InnoDB to support relational constraints and transactions.

---

# 7. Phase 5 — Sample Data

The third SQL script inserts initial test data:

```text
sql/03_insert_data.sql
```

The data includes:

* Books
* Members
* Borrowing records

Sample data makes it possible to test the application immediately after creating the database.

---

# 8. Phase 6 — SQL Queries

The project contains dedicated SQL query files.

Basic queries are stored in:

```text
sql/04_queries.sql
```

Advanced queries are stored in:

```text
sql/05_advanced_queries.sql
```

The queries cover:

* Filtering
* Searching
* Sorting
* Aggregation
* Joins
* Borrowing reports
* Availability
* Member history
* Dashboard statistics

---

# 9. Phase 7 — Python Environment

The backend was developed using Python.

A virtual environment was created to isolate project dependencies:

```text
venv/
```

The environment contains the project's Python packages without affecting the global Python installation.

The main dependencies are:

```text
Flask
mysql-connector-python
python-dotenv
```

They are stored in:

```text
requirements.txt
```

---

# 10. Phase 8 — Database Connection

The database connection was separated from the main application.

The connection logic is stored in:

```text
database.py
```

The application uses:

```text
mysql-connector-python
```

Environment variables are loaded using:

```text
python-dotenv
```

The connection flow is:

```text
Flask
  ↓
database.py
  ↓
MySQL Connector
  ↓
MySQL
  ↓
librarydb
```

This approach keeps database connection configuration centralized.

---

# 11. Phase 9 — Connection Testing

Before building the web application, the database connection was tested independently.

The test file is:

```text
test_connection.py
```

The test verifies that Python can:

1. Connect to MySQL.
2. Select the correct database.
3. Execute a SQL query.
4. Retrieve the database name.
5. Close the connection.

Expected result:

```text
SUCCESS: Connected to MySQL database!
Connected database: librarydb
```

---

# 12. Phase 10 — Flask Backend

After verifying the database connection, the Flask backend was created.

The main application file is:

```text
app.py
```

The backend is responsible for:

* Routing
* Database operations
* Business logic
* Validation
* Search
* CRUD operations
* Borrowing
* Returning
* Dashboard statistics
* Error handling
* Flash messages

---

# 13. Phase 11 — Dashboard

The dashboard was implemented as the main application page.

Route:

```text
/
```

The dashboard calculates statistics such as:

* Total books
* Available books
* Borrowed books
* Total members
* Active loans

The dashboard provides a quick overview of the current library status.

---

# 14. Phase 12 — Books Module

The Books module was implemented to manage the library catalog.

The application supports:

```text
Create
Read
Update
Delete
Search
```

Book fields include:

```text
book_id
title
author
genre
published_year
is_available
```

The backend validates required fields before inserting or updating records.

---

# 15. Phase 13 — Members Module

The Members module was implemented to manage registered members.

Member fields include:

```text
member_id
name
email
phone_number
join_date
```

The module supports:

```text
Create
Read
Update
Delete
Search
```

Deletion is protected when a member has borrowing history.

This prevents historical borrowing records from becoming inconsistent.

---

# 16. Phase 14 — Borrowing Module

The borrowing module connects books and members.

The borrowing process is:

```text
Select Member
     ↓
Select Available Book
     ↓
Submit Form
     ↓
Validate Member
     ↓
Validate Book
     ↓
Check Availability
     ↓
Create Loan
     ↓
Update Book Status
     ↓
Commit Transaction
```

When borrowing is successful:

```text
borrowing.return_date = NULL
books.is_available = 0
```

---

# 17. Phase 15 — Returning Books

The return process updates both the borrowing record and the book.

The workflow is:

```text
Select Active Loan
       ↓
Find Book
       ↓
Check Loan Status
       ↓
Set Return Date
       ↓
Set Book Available
       ↓
Commit Changes
```

The database is updated so that:

```text
return_date = current date
```

and:

```text
is_available = 1
```

This keeps the borrowing history while making the book available again.

---

# 18. Phase 16 — Frontend Development

After the backend routes were created, the frontend templates were implemented.

The templates are stored in:

```text
templates/
```

Main templates include:

```text
base.html
index.html
books.html
add_book.html
edit_book.html
members.html
add_member.html
edit_member.html
borrowing.html
borrow_book.html
```

---

# 19. Phase 17 — Shared Layout

The application uses:

```text
templates/base.html
```

as the shared layout.

This provides common elements such as:

* Navigation
* Page structure
* Flash messages
* Common styling references

Other templates extend the base template.

This avoids repeating the same HTML structure on every page.

---

# 20. Phase 18 — CSS Styling

The main stylesheet is:

```text
static/style.css
```

The stylesheet controls:

* Navigation
* Buttons
* Tables
* Forms
* Dashboard cards
* Status indicators
* Flash messages
* Page layout

The goal was to create a simple and consistent interface for the complete application.

---

# 21. Phase 19 — Validation

Validation was added to prevent invalid operations.

Examples include:

### Book validation

```text
Title is required
Author is required
Published year must be valid
```

### Borrowing validation

```text
Member must exist
Book must exist
Book must be available
```

### Return validation

```text
Loan must exist
Loan must not already be returned
```

---

# 22. Phase 20 — Business Rules

The application implements important business rules.

### Book availability

When a book is borrowed:

```text
is_available = 0
```

When it is returned:

```text
is_available = 1
```

### Borrowing history

Books with borrowing history are protected from deletion.

### Member history

Members with borrowing history are protected from deletion.

### Duplicate return

A loan that already has a return date cannot be returned again.

---

# 23. Phase 21 — Error Handling

Error handling was added to protect application operations.

Examples include:

* Invalid form data
* Missing book
* Missing member
* Unavailable book
* Already returned loan
* Database errors
* Invalid record deletion

The application uses Flask flash messages to communicate results.

---

# 24. Phase 22 — Search

Search functionality was added to improve access to library records.

Books can be searched using:

```text
Title
Author
Genre
```

Members can also be searched.

Search values are passed to parameterized SQL queries.

---

# 25. Phase 23 — Security Configuration

Sensitive configuration is stored in:

```text
.env
```

Example:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=librarydb
```

The `.env` file is excluded from Git using:

```text
.gitignore
```

Parameterized SQL queries are used to reduce SQL injection risks.

---

# 26. Phase 24 — Testing

Testing was performed progressively.

## Database Testing

The database was tested using SQL queries.

Examples:

```sql
SELECT * FROM books;
```

```sql
SELECT * FROM members;
```

```sql
SELECT * FROM borrowing;
```

---

## Connection Testing

Python was tested using:

```text
test_connection.py
```

---

## Application Testing

The following workflows were tested:

```text
Add Book
Edit Book
Search Book
Delete Book

Add Member
Edit Member
Search Member
Delete Member

Borrow Book
Return Book

Dashboard Statistics
```

---

# 27. Phase 25 — Borrowing and Return Testing

The most important business workflow was tested from beginning to end.

Example:

```text
Available Book
      ↓
Borrow Book
      ↓
Book becomes unavailable
      ↓
Loan becomes active
      ↓
Return Book
      ↓
Return date is stored
      ↓
Book becomes available
```

This verifies that the two related database tables remain synchronized.

---

# 28. Phase 26 — Documentation

The project documentation was organized into:

```text
README.md
docs/database-schema.md
docs/development-process.md
```

The README provides an overall description of the project.

The database documentation explains the database architecture.

This document explains the development process.

---

# 29. Phase 27 — Project Organization

The final project structure is organized into separate responsibilities:

```text
Library-Management-System/
│
├── app.py
├── database.py
├── test_connection.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_insert_data.sql
│   ├── 04_queries.sql
│   └── 05_advanced_queries.sql
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── add_book.html
│   ├── edit_book.html
│   ├── members.html
│   ├── add_member.html
│   ├── edit_member.html
│   ├── borrowing.html
│   └── borrow_book.html
│
├── static/
│   └── style.css
│
├── docs/
│   ├── database-schema.md
│   └── development-process.md
│
└── venv/
```

---

# 30. Complete Application Flow

The complete system can be represented as:

```text
                         USER
                           │
                           ▼
                     WEB BROWSER
                           │
                           ▼
                    ┌────────────┐
                    │  FRONTEND  │
                    │ HTML / CSS │
                    │  Jinja2    │
                    └─────┬──────┘
                          │
                          ▼
                    ┌────────────┐
                    │   FLASK    │
                    │  BACKEND   │
                    └─────┬──────┘
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
          Books        Members      Borrowing
             │            │            │
             └────────────┼────────────┘
                          │
                          ▼
                    SQL QUERIES
                          │
                          ▼
                    ┌────────────┐
                    │   MYSQL    │
                    │  librarydb │
                    └─────┬──────┘
                          │
                          ▼
                     SQL RESULT
                          │
                          ▼
                       FLASK
                          │
                          ▼
                     JINJA2
                          │
                          ▼
                     WEB PAGE
                          │
                          ▼
                         USER
```

---

# 31. Development Principles

The project follows several development principles.

## Separation of Responsibilities

Frontend, backend, and database responsibilities are separated.

```text
Frontend → Presentation
Backend  → Logic
Database → Data
```

## Reusable Components

The shared template reduces duplicated HTML.

## Centralized Database Connection

Database connection logic is maintained in one location.

## Validation Before Database Operations

Input is checked before modifying records.

## Data Integrity

Foreign keys and application rules protect relationships.

## Configuration Separation

Sensitive configuration is stored in environment variables.

---

# 32. Future Development

The current architecture can be extended with:

* Authentication
* User roles
* Password hashing
* Advanced permissions
* Overdue management
* Due dates
* Notifications
* Advanced reports
* Charts
* REST API
* Pagination
* Advanced search
* Docker
* CI/CD
* Cloud deployment
* Production MySQL
* Monitoring
* Automated tests

A possible future architecture is:

```text
                    USERS
                      │
                      ▼
                 WEB BROWSER
                      │
                      ▼
                  NGINX / HTTPS
                      │
                      ▼
               FLASK / GUNICORN
                      │
             ┌────────┼────────┐
             │        │        │
             ▼        ▼        ▼
           API     Web App   Auth
             │        │        │
             └────────┼────────┘
                      │
                      ▼
                 MYSQL DATABASE
                      │
                      ▼
                 BACKUP / CLOUD
```

---

# 33. Final Development Result

The development process produced a complete application with:

```text
Database
   +
SQL
   +
Python
   +
Flask
   +
HTML
   +
CSS
   +
Jinja2
   +
Validation
   +
Business Logic
   +
Testing
   +
Documentation
   +
Git/GitHub
```

The final system provides a complete workflow for managing library books, members, borrowing transactions, returns, and library statistics.

---

# 34. Summary

The development process followed a structured progression:

```text
1. Requirements
      ↓
2. Database Design
      ↓
3. SQL Scripts
      ↓
4. Sample Data
      ↓
5. Python Environment
      ↓
6. MySQL Connection
      ↓
7. Flask Backend
      ↓
8. Books Module
      ↓
9. Members Module
      ↓
10. Borrowing Module
      ↓
11. Return Workflow
      ↓
12. Frontend
      ↓
13. Validation
      ↓
14. Business Rules
      ↓
15. Testing
      ↓
16. Documentation
      ↓
17. Git/GitHub
```

This structure provides a clear development history and establishes a foundation for further improvements and production deployment.
