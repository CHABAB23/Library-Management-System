# 📚 Library Management System

A full-stack **Library Management System** built with **Python, Flask, MySQL, HTML, CSS, and Jinja2**.

The application provides a complete digital workflow for managing books, library members, borrowing operations, returns, availability, and dashboard statistics.

The project combines a relational MySQL database with a Flask backend and a server-rendered web frontend to create a structured library management application.

---

# 📖 Project Overview

The Library Management System is designed to manage the main operations of a library through a centralized web application.

Instead of managing books, members, and borrowing records manually, the application provides a structured system where users can:

* Manage books
* Add, edit, search, and delete books
* Manage library members
* Add, edit, search, and delete members
* Borrow books
* Return books
* Track active loans
* Track borrowing history
* Check book availability
* View library statistics
* Search library records
* Maintain relationships between books, members, and borrowing transactions
* Store all data in a MySQL relational database

The application is divided into three major technical layers:

```text
┌───────────────────────────────────────────────────────────┐
│                  LIBRARY MANAGEMENT SYSTEM                │
└─────────────────────────────┬─────────────────────────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
       ┌───────────┐    ┌───────────┐    ┌───────────┐
       │ FRONTEND  │    │  BACKEND  │    │ DATABASE  │
       └───────────┘    └───────────┘    └───────────┘
             │                │                │
             ▼                ▼                ▼
          HTML/CSS          Flask/Python       MySQL
          Jinja2            Routes             Tables
          Forms             Business Logic     Relationships
          UI                Validation         SQL
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                    COMPLETE APPLICATION
```

The frontend provides the user interface, the backend processes requests and applies business rules, and MySQL stores the application data.

---

# 🏛️ Complete Project Description

The project is more than a simple database.

It is a complete web application composed of several interconnected components:

```text
                         LIBRARY MANAGEMENT SYSTEM
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
     FRONTEND                   BACKEND                   DATABASE
        │                          │                          │
   HTML / CSS                  Flask / Python              MySQL
   Jinja2 Templates            Routes                      SQL
   Forms                       Business Logic              Tables
   Navigation                 Validation                   Relationships
   Dashboard UI               Error Handling
        │                          │
        │                    ┌─────┼─────────┐
        │                    │     │         │
        ▼                    ▼     ▼         ▼
   User Interface          Books Members   Borrowing
        │                    │     │         │
        └────────────────────┼─────┼─────────┘
                             │
                             ▼
                         Dashboard
                             │
                             ▼
                    Statistics / Reports
```

The system works through communication between the frontend, backend, and database.

For example, when a user borrows a book:

```text
User
 │
 ▼
Frontend
 │
 │ POST /borrowing/borrow
 ▼
Flask Backend
 │
 ├── Check member
 ├── Check book
 ├── Check availability
 ├── Create borrowing record
 └── Update book availability
 │
 ▼
MySQL Database
 │
 ├── borrowing table
 └── books table
 │
 ▼
Flask
 │
 ▼
Frontend
 │
 ▼
Success Message
```

This architecture allows each part of the system to have a specific responsibility.

---

# 🖥️ Frontend

The frontend is the part of the application that users interact with.

It is built using:

* HTML
* CSS
* Jinja2 templates
* Flask template rendering

The frontend provides pages for:

```text
Dashboard
Books
Members
Borrowing
Add Book
Edit Book
Add Member
Edit Member
Borrow Book
```

## Frontend Responsibilities

The frontend is responsible for:

* Displaying information
* Providing navigation
* Showing forms
* Collecting user input
* Displaying database records
* Showing success messages
* Showing error messages
* Displaying book availability
* Displaying borrowing history
* Providing search interfaces

The frontend does not directly communicate with MySQL.

Instead:

```text
Frontend
    ↓
Flask Backend
    ↓
MySQL Database
```

This separation keeps the application organized.

---

# 🎨 HTML and Jinja2

The application uses Flask's Jinja2 template engine.

A shared layout is defined in:

```text
templates/base.html
```

Other pages extend the base template.

Example structure:

```text
templates/
│
├── base.html
├── index.html
├── books.html
├── add_book.html
├── edit_book.html
├── members.html
├── add_member.html
├── edit_member.html
├── borrowing.html
└── borrow_book.html
```

Using a shared base template avoids duplicating the navigation and common page structure.

---

# 🎨 CSS

The application uses:

```text
static/style.css
```

The stylesheet controls:

* Page layout
* Navigation
* Buttons
* Tables
* Dashboard cards
* Forms
* Success messages
* Error messages
* Book availability indicators
* Responsive layout behavior

Example:

```text
static/
└── style.css
```

---

# ⚙️ Backend

The backend is responsible for the application's logic.

It is built using:

* Python
* Flask
* MySQL Connector
* python-dotenv

Main backend file:

```text
app.py
```

Database connection file:

```text
database.py
```

The backend acts as the bridge between the frontend and database.

```text
             ┌─────────────┐
             │   FRONTEND  │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │    FLASK    │
             │   BACKEND   │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │    MYSQL    │
             │  DATABASE   │
             └─────────────┘
```

---

# 🧠 Backend Responsibilities

The Flask backend handles:

* HTTP requests
* URL routing
* Database operations
* Business logic
* Validation
* Search
* CRUD operations
* Borrowing operations
* Returning operations
* Error handling
* Flash messages
* Page rendering
* Redirects

---

# 🛣️ Application Routes

The application contains routes for the main operations.

## Dashboard

```text
GET /
```

Displays:

* Total books
* Available books
* Borrowed books
* Total members
* Active loans

---

## Books

```text
GET /books
GET /books/add
POST /books/add
GET /books/edit/<book_id>
POST /books/edit/<book_id>
POST /books/delete/<book_id>
```

These routes manage the book catalog.

---

## Members

```text
GET /members
GET /members/add
POST /members/add
GET /members/edit/<member_id>
POST /members/edit/<member_id>
POST /members/delete/<member_id>
```

These routes manage library members.

---

## Borrowing

```text
GET /borrowing
GET /borrowing/borrow
POST /borrowing/borrow
POST /borrowing/return/<loan_id>
```

These routes manage borrowing and returning operations.

---

# 📚 Books Management

The Books module manages the library catalog.

Each book contains:

```text
book_id
title
author
genre
published_year
is_available
```

Users can:

* View books
* Search books
* Add books
* Edit books
* Delete books when permitted
* Check availability

Example:

```text
The Great Gatsby
Author: F. Scott Fitzgerald
Genre: Fiction
Published Year: 1925
Status: Borrowed
```

---

# 👥 Members Management

The Members module manages registered library members.

Each member contains:

```text
member_id
name
email
phone_number
join_date
```

Users can:

* View members
* Search members
* Add members
* Edit members
* Delete members when permitted
* View member borrowing history

---

# 📖 Borrowing Management

The Borrowing module manages relationships between:

```text
Book
   +
Member
   +
Borrowing Transaction
```

A borrowing record contains:

```text
loan_id
book_id
member_id
borrow_date
return_date
librarian_id
```

The system records when a book is borrowed and when it is returned.

---

# 🔄 Borrowing Workflow

When a user borrows a book:

```text
1. Select a member
        ↓
2. Select an available book
        ↓
3. Submit borrowing form
        ↓
4. Backend validates member
        ↓
5. Backend validates book
        ↓
6. Backend checks availability
        ↓
7. Create borrowing record
        ↓
8. Set book availability = 0
        ↓
9. Commit transaction
        ↓
10. Show success message
```

The database therefore keeps the borrowing operation synchronized with the book's availability.

---

# 🔙 Returning a Book

When a book is returned:

```text
1. Select active loan
        ↓
2. Backend finds the book
        ↓
3. Check that the loan is active
        ↓
4. Set return_date = current date
        ↓
5. Set book availability = 1
        ↓
6. Commit changes
        ↓
7. Show success message
```

Example:

```text
Before return:

Book:
The Great Gatsby
Availability: Borrowed

Loan:
Return Date: NULL
```

After return:

```text
Book:
The Great Gatsby
Availability: Available

Loan:
Return Date: 2026-09-26
```

---

# 📊 Dashboard

The dashboard provides an overview of the library.

It displays statistics such as:

```text
Total Books
Available Books
Borrowed Books
Total Members
Active Loans
```

Conceptually:

```text
┌────────────────┐
│  Total Books   │
│       6        │
└────────────────┘

┌────────────────┐
│Available Books │
│       5        │
└────────────────┘

┌────────────────┐
│ Borrowed Books │
│       1        │
└────────────────┘

┌────────────────┐
│ Total Members  │
│       3        │
└────────────────┘
```

The dashboard obtains its information from MySQL through Flask.

---

# 🗄️ Database

The database is implemented using:

**MySQL**

Database name:

```text
librarydb
```

The database contains three main tables:

```text
books
members
borrowing
```

---

# 📚 Books Table

```text
books
├── book_id
├── title
├── author
├── genre
├── published_year
└── is_available
```

Purpose:

Stores information about every book in the library.

---

# 👤 Members Table

```text
members
├── member_id
├── name
├── email
├── phone_number
└── join_date
```

Purpose:

Stores information about registered library members.

---

# 🔄 Borrowing Table

```text
borrowing
├── loan_id
├── book_id
├── member_id
├── borrow_date
├── return_date
└── librarian_id
```

Purpose:

Stores borrowing transactions.

---

# 🔗 Database Relationships

The database uses foreign keys.

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

The borrowing table connects books and members.

This allows the application to answer questions such as:

* Which member borrowed a book?
* Which book is currently borrowed?
* When was the book borrowed?
* When was it returned?
* Which books has a member borrowed?
* Which books are currently available?

---

# 🧩 Entity Relationship Structure

```text
┌──────────────────────┐
│       BOOKS          │
├──────────────────────┤
│ PK book_id           │
│ title                │
│ author               │
│ genre                │
│ published_year       │
│ is_available         │
└──────────┬───────────┘
           │
           │ 1
           │
           │
           │ N
┌──────────▼───────────┐
│     BORROWING        │
├──────────────────────┤
│ PK loan_id           │
│ FK book_id           │
│ FK member_id         │
│ borrow_date          │
│ return_date          │
│ librarian_id         │
└──────────┬───────────┘
           │
           │ N
           │
           │ 1
┌──────────▼───────────┐
│      MEMBERS         │
├──────────────────────┤
│ PK member_id         │
│ name                 │
│ email                │
│ phone_number         │
│ join_date            │
└──────────────────────┘
```

---

# 🧱 Database Integrity

The system uses relational database constraints to protect data consistency.

Examples:

* Primary keys identify records uniquely.
* Foreign keys connect related records.
* `NOT NULL` protects required fields.
* `AUTO_INCREMENT` generates identifiers.
* InnoDB provides transactional support.
* UTF-8 supports international text.

---

# 🔐 Business Rules

The application implements important business rules.

## Rule 1 — A book must exist before borrowing

The backend verifies the selected book.

## Rule 2 — A member must exist

The backend verifies the selected member.

## Rule 3 — Only available books can be borrowed

The backend checks:

```text
is_available = 1
```

## Rule 4 — Borrowed books become unavailable

After borrowing:

```text
is_available = 0
```

## Rule 5 — Returned books become available

After returning:

```text
is_available = 1
```

## Rule 6 — A returned loan cannot be returned again

The backend checks:

```text
return_date IS NULL
```

## Rule 7 — Books with borrowing history are protected

A book that has borrowing records cannot simply be deleted.

This protects historical data.

## Rule 8 — Members with borrowing history are protected

Members with borrowing records cannot simply be deleted.

This protects relationships and historical information.

---

# 🔍 Search Functionality

The application supports searching.

For books, users can search by:

```text
Title
Author
Genre
```

The backend uses parameterized SQL queries.

Example:

```sql
SELECT *
FROM books
WHERE title LIKE %s
   OR author LIKE %s
   OR genre LIKE %s;
```

This allows users to quickly find records.

---

# 🧮 SQL Layer

The project includes dedicated SQL scripts.

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

# 🏗️ Database Creation

The first script creates the database:

```text
01_create_database.sql
```

It creates:

```text
librarydb
```

---

# 🏗️ Table Creation

The second script creates:

```text
books
members
borrowing
```

and defines their relationships.

---

# 🌱 Sample Data

The third script inserts sample books, members, and borrowing records.

Example books include:

```text
The Great Gatsby
1984
To Kill a Mockingbird
The Hobbit
The Alchemist
Clean Code
```

---

# 🔎 Basic SQL Queries

The fourth SQL file contains queries for:

* All books
* All members
* Borrowing records
* Available books
* Borrowed books
* Books by genre
* Books published after a specific year
* Counts
* Active loans
* Returned books
* Borrowing history
* Complete reports

---

# 🚀 Advanced SQL Queries

The advanced SQL file contains queries for:

* Complete borrowing reports
* Currently borrowed books
* Books borrowed by members
* Books by genre
* Members with active loans
* Books never borrowed
* Most borrowed books
* Books between specific years
* Title searches
* Members who joined in a specific year
* Total borrowing records
* Average borrowing activity
* Availability status
* Member borrowing history
* Dashboard statistics

These queries demonstrate practical SQL reporting and analysis.

---

# 🔌 Backend–Database Connection

The database connection is centralized in:

```text
database.py
```

The application uses:

```text
mysql-connector-python
```

The connection configuration is loaded from environment variables.

```text
Python
   │
   ▼
database.py
   │
   ▼
MySQL Connector
   │
   ▼
MySQL
   │
   ▼
librarydb
```

This prevents database connection code from being duplicated throughout the application.

---

# 🔐 Environment Configuration

Database credentials are stored in:

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

This prevents database credentials from being committed to the repository.

---

# 🛡️ Security

The application includes several basic security practices.

## Environment Variables

Sensitive database credentials are stored outside the source code.

## Parameterized SQL

Database queries use parameters rather than directly concatenating user input.

This reduces SQL injection risk.

## POST Requests

Destructive operations such as deleting records use POST requests.

## Validation

User input is validated before database operations.

For example:

* Required title
* Required author
* Valid publication year
* Existing member
* Existing book
* Available book
* Valid borrowing record

---

# ✅ Input Validation

The backend validates data before storing it.

For example, when adding a book:

```text
Title
Author
Genre
Published Year
```

The publication year must be a valid integer within the application's accepted range.

Invalid data produces an error message instead of being inserted.

---

# ⚠️ Error Handling

The application handles common errors such as:

* Missing book
* Missing member
* Book unavailable
* Loan already returned
* Invalid form data
* Database errors
* Attempted deletion of records with history

The application uses Flask flash messages to communicate results to users.

---

# 💬 Flash Messages

The application provides feedback after operations.

Examples:

```text
Book added successfully.
```

```text
Book updated successfully.
```

```text
Book borrowed successfully.
```

```text
Book returned successfully.
```

```text
This book cannot be deleted because it has borrowing history.
```

This improves the user experience and makes operations easier to understand.

---

# 🏗️ Application Architecture

The project follows a simple layered architecture.

```text
┌────────────────────────────────────────────┐
│                  FRONTEND                  │
│                                            │
│ HTML + CSS + Jinja2 Templates              │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│                  BACKEND                   │
│                                            │
│ Flask Routes                               │
│ Business Logic                             │
│ Validation                                 │
│ Error Handling                             │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│              DATABASE LAYER               │
│                                            │
│ MySQL Connector                            │
│ SQL Queries                                │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│                   MYSQL                   │
│                                            │
│ Books | Members | Borrowing                │
└────────────────────────────────────────────┘
```

---

# 🔄 Complete Data Flow

A typical request follows this path:

```text
USER
 │
 ▼
WEB BROWSER
 │
 ▼
HTML FORM
 │
 ▼
FLASK ROUTE
 │
 ▼
VALIDATION
 │
 ▼
BUSINESS LOGIC
 │
 ▼
SQL QUERY
 │
 ▼
MYSQL DATABASE
 │
 ▼
DATABASE RESULT
 │
 ▼
FLASK
 │
 ▼
JINJA2 TEMPLATE
 │
 ▼
HTML RESPONSE
 │
 ▼
USER
```

This is the central architecture of the application.

---

# 🧪 Testing

Testing is performed at several levels.

## Database Testing

The database is tested using MySQL queries.

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

# 🔌 Connection Testing

The project includes:

```text
test_connection.py
```

It verifies that Python can successfully connect to MySQL.

Expected result:

```text
SUCCESS: Connected to MySQL database!
Connected database: librarydb
```

---

# 🧪 Application Testing

Important workflows are tested through the web application.

### Books

```text
Add book
Edit book
Search book
Delete book
```

### Members

```text
Add member
Edit member
Search member
Delete member
```

### Borrowing

```text
Borrow available book
Attempt to borrow unavailable book
Return active loan
Attempt to return already returned loan
```

### Dashboard

```text
Check total books
Check available books
Check borrowed books
Check members
Check active loans
```

---

# 📁 Project Structure

The complete project structure is:

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

The virtual environment is normally excluded from Git.

---

# 📄 Important Files

## `app.py`

Main Flask application.

Contains:

* Routes
* Business logic
* Validation
* CRUD operations
* Borrowing logic
* Returning logic
* Dashboard logic

---

## `database.py`

Responsible for creating the MySQL connection.

---

## `test_connection.py`

Tests the Python-to-MySQL connection.

---

## `templates/`

Contains all frontend HTML templates.

---

## `static/style.css`

Contains application styling.

---

## `.env`

Contains local environment configuration.

It should never be committed to Git.

---

## `requirements.txt`

Contains Python dependencies.

Example dependencies include:

```text
Flask
mysql-connector-python
python-dotenv
```

---

# 🧰 Technology Stack

## Frontend

```text
HTML5
CSS3
Jinja2
```

## Backend

```text
Python
Flask
```

## Database

```text
MySQL
```

## Database Driver

```text
mysql-connector-python
```

## Configuration

```text
python-dotenv
```

## Development Environment

```text
Visual Studio Code
Windows
PowerShell
MySQL CLI
MySQL Workbench
```

## Version Control

```text
Git
GitHub
```

---

# 🛠️ Installation

## 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Library-Management-System
```

---

# 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 4. Configure Environment Variables

Create:

```text
.env
```

Add:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=librarydb
```

Use your local MySQL password.

Do not publish the `.env` file.

---

# 5. Create the Database

Open MySQL:

```bash
mysql -u root -p
```

Then execute:

```sql
SOURCE sql/01_create_database.sql;
SOURCE sql/02_create_tables.sql;
SOURCE sql/03_insert_data.sql;
```

---

# 6. Test the Connection

Run:

```bash
python test_connection.py
```

Expected:

```text
SUCCESS: Connected to MySQL database!
Connected database: librarydb
```

---

# 7. Start the Application

Run:

```bash
python app.py
```

The Flask application will start locally.

Open the address displayed by Flask in your browser.

---

# 🌐 Application Workflow

The normal workflow is:

```text
Start Application
       │
       ▼
Dashboard
       │
       ├───────────────┐
       ▼               ▼
     Books           Members
       │               │
       └───────┬───────┘
               ▼
           Borrowing
               │
        ┌──────┴──────┐
        ▼             ▼
      Borrow         Return
        │             │
        └──────┬──────┘
               ▼
           Dashboard
               │
               ▼
        Updated Statistics
```

---

# 📚 Example Complete Business Scenario

A library member named:

```text
John Smith
```

wants to borrow:

```text
Clean Code
```

The workflow is:

```text
John Smith
    │
    ▼
Open Borrowing
    │
    ▼
Select John Smith
    │
    ▼
Select Clean Code
    │
    ▼
Submit
    │
    ▼
Flask validates the request
    │
    ▼
MySQL checks the book
    │
    ▼
Book is available
    │
    ▼
Borrowing record created
    │
    ▼
Clean Code becomes unavailable
    │
    ▼
Dashboard statistics update
```

When the book is returned:

```text
Return request
      │
      ▼
Find loan
      │
      ▼
Set return_date
      │
      ▼
Set is_available = 1
      │
      ▼
Commit database changes
      │
      ▼
Book becomes available
```

---

# 📈 Project Development Process

The project was developed progressively through several layers.

## Phase 1 — Database Design

The database was designed first.

```text
Database
   ↓
Tables
   ↓
Relationships
   ↓
Constraints
   ↓
Sample Data
```

---

## Phase 2 — SQL Development

SQL queries were created to retrieve and analyze the data.

```text
Basic Queries
      ↓
Filtering
      ↓
Joins
      ↓
Aggregations
      ↓
Advanced Reports
```

---

## Phase 3 — Python Database Connection

Python was connected to MySQL using:

```text
mysql-connector-python
```

The connection was isolated in:

```text
database.py
```

---

## Phase 4 — Flask Backend

Flask was introduced to create the web application.

Routes were implemented for:

```text
Books
Members
Borrowing
Returning
Dashboard
```

---

## Phase 5 — Frontend

HTML templates and CSS were added.

The application received:

* Navigation
* Tables
* Forms
* Buttons
* Dashboard cards
* Status indicators
* Flash messages

---

## Phase 6 — Validation and Business Logic

Business rules were implemented to protect the database.

Examples:

```text
Unavailable book → Cannot borrow
Returned loan → Cannot return again
Existing borrowing history → Cannot delete book
Existing borrowing history → Cannot delete member
```

---

## Phase 7 — Testing

The complete workflow was tested:

```text
Create
Read
Update
Delete
Borrow
Return
Search
Dashboard
```

---

## Phase 8 — Documentation

The project documentation includes:

```text
README
Database Schema
Development Process
SQL Documentation
```

---

# 📝 Documentation

The `docs/` directory contains additional project documentation.

Example:

```text
docs/
│
├── database-schema.md
└── development-process.md
```

The database documentation explains:

* Tables
* Columns
* Primary keys
* Foreign keys
* Relationships
* Data structure

The development documentation explains:

* Project architecture
* Development phases
* Implementation decisions
* Testing process

---

# 🔀 Git and GitHub

Git is used for version control.

The project can be organized into commits such as:

```text
Initial project setup
Create MySQL database
Create database tables
Add sample data
Add SQL queries
Connect Python to MySQL
Create Flask application
Add books management
Add members management
Add borrowing workflow
Add return workflow
Add dashboard
Add validation
Improve UI
Add documentation
```

This creates a clear development history.

---

# 🚀 Git Workflow

Typical workflow:

```bash
git status
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Build library management system"
```

Push:

```bash
git push
```

---

# 🔒 Files Excluded From Git

The `.gitignore` file contains:

```text
venv/
__pycache__/
*.pyc
.env
```

This prevents unnecessary or sensitive files from being uploaded.

---

# 📊 Current Application Capabilities

The current system supports:

### Database

* MySQL database
* Relational tables
* Primary keys
* Foreign keys
* Sample data
* SQL queries
* Advanced SQL reports

### Backend

* Flask
* Routing
* CRUD operations
* Business logic
* Validation
* Error handling
* Database integration
* Flash messages

### Frontend

* HTML
* CSS
* Jinja2
* Navigation
* Forms
* Tables
* Dashboard
* Search

### Library Operations

* Book management
* Member management
* Borrowing
* Returning
* Availability tracking
* Borrowing history
* Dashboard statistics

---

# 📌 Current Architecture

The complete current architecture can be summarized as:

```text
                        USER
                         │
                         ▼
                  ┌─────────────┐
                  │   BROWSER   │
                  └──────┬──────┘
                         │
                         ▼
              ┌─────────────────────┐
              │      FRONTEND       │
              │                     │
              │ HTML + CSS + Jinja2 │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │       FLASK         │
              │      BACKEND        │
              │                     │
              │ Routes              │
              │ Business Logic      │
              │ Validation          │
              │ Error Handling      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ DATABASE CONNECTION │
              │                     │
              │ MySQL Connector     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │        MYSQL        │
              │                     │
              │ Books               │
              │ Members             │
              │ Borrowing           │
              └─────────────────────┘
```

---

# 🔮 Future Improvements

The current application provides the core library workflow. The architecture can be extended with additional features.

## Authentication

Add:

```text
Login
Logout
User accounts
Password hashing
Roles
Permissions
```

Possible roles:

```text
Administrator
Librarian
Staff
```

---

## Advanced Dashboard

Future dashboard features could include:

* Charts
* Monthly borrowing statistics
* Most borrowed books
* Most active members
* Overdue books
* Recent borrowing activity
* Recent returns

---

## Overdue Management

Add:

```text
Due date
Overdue status
Overdue reports
Notifications
```

---

## Pagination

Large datasets could use pagination:

```text
Previous | 1 | 2 | 3 | Next
```

---

## Advanced Search

Future search options:

```text
Title
Author
Genre
Year
Availability
Member
Borrow date
Return date
```

---

## REST API

The backend could later expose an API:

```text
GET    /api/books
POST   /api/books
GET    /api/books/<id>
PUT    /api/books/<id>
DELETE /api/books/<id>
```

This would allow other applications to communicate with the library system.

---

# ☁️ Production Architecture

A future production deployment could use:

```text
                    INTERNET
                       │
                       ▼
                ┌──────────────┐
                │   FRONTEND   │
                │ Web Browser  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Web Server   │
                │ Nginx        │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Flask App    │
                │ Gunicorn     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ MySQL        │
                │ Database     │
                └──────────────┘
```

The application could eventually be deployed using cloud infrastructure.

Possible components include:

```text
Cloud Hosting
Managed MySQL
Object Storage
Reverse Proxy
HTTPS
CI/CD
Monitoring
Logging
Backups
```

---

# 🐳 Containerization

The project can also be containerized using Docker.

Possible architecture:

```text
Docker
│
├── Flask Application
│
├── MySQL
│
└── Network
```

A future implementation could include:

```text
Dockerfile
docker-compose.yml
```

---

# 🔄 CI/CD

A future development pipeline could be:

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub
    │
    ▼
CI Pipeline
    │
    ├── Test
    ├── Lint
    └── Build
    │
    ▼
Deployment
    │
    ▼
Production
```

---

# 📊 Possible Monitoring

A production version could include:

* Application logs
* Database monitoring
* Error tracking
* Performance monitoring
* Health checks
* Backup monitoring

---

# 🧠 Technical Concepts Demonstrated

This project demonstrates practical experience with:

### SQL

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* `WHERE`
* `LIKE`
* `JOIN`
* `GROUP BY`
* `ORDER BY`
* `COUNT`
* `AVG`
* `CASE`
* Foreign keys
* Primary keys
* Transactions

### Python

* Functions
* Modules
* Environment variables
* Exception handling
* Database connections
* Application logic

### Flask

* Routes
* Templates
* Forms
* Request handling
* Redirects
* Flash messages
* URL parameters

### Web Development

* HTML
* CSS
* Forms
* Tables
* Navigation
* Server-side rendering

### Database Design

* Relational modeling
* Primary keys
* Foreign keys
* Relationships
* Data integrity

### Software Engineering

* Project structure
* Separation of concerns
* Configuration management
* Version control
* Documentation
* Testing

---

# 🎯 Project Objectives

The main objectives of the system are:

1. Centralize library information.
2. Simplify book management.
3. Simplify member management.
4. Track borrowing transactions.
5. Track returned books.
6. Maintain book availability.
7. Protect data relationships.
8. Provide useful library statistics.
9. Provide a structured web interface.
10. Demonstrate a complete database-backed web application architecture.

---

# 🏁 Conclusion

The Library Management System combines a relational database, backend application, and web frontend into one complete application.

The architecture is based on three main technical layers:

```text
Frontend
   ↓
Backend
   ↓
Database
```

The frontend provides the interface.

The Flask backend manages requests, validation, business rules, and communication with the database.

MySQL stores the application's persistent data and relationships.

The main library modules work together:

```text
Books
  │
  ├──────────────┐
  │              │
  ▼              ▼
Members       Borrowing
  │              │
  └──────┬───────┘
         ▼
     Dashboard
         │
         ▼
    Statistics
```

The result is a structured library management platform capable of managing the complete lifecycle of books, members, borrowing transactions, and returns.

The project also provides a foundation for future development such as authentication, advanced reporting, REST APIs, Docker, CI/CD, cloud deployment, monitoring, and production database infrastructure.

---

# 👨‍💻 Author

**Khalid Chabab**

Library Management System
Python • Flask • MySQL • HTML • CSS • SQL • Git/GitHub

---

# ⭐ Project Highlights

```text
✔ Full-stack web application
✔ Flask backend
✔ MySQL relational database
✔ HTML/CSS frontend
✔ Jinja2 templates
✔ CRUD operations
✔ Book management
✔ Member management
✔ Borrowing workflow
✔ Return workflow
✔ Availability tracking
✔ Search functionality
✔ Dashboard statistics
✔ SQL reporting
✔ Data validation
✔ Error handling
✔ Environment configuration
✔ Git/GitHub ready
✔ Documentation
✔ Production expansion path
```
