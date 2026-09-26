-- ============================================
-- Library Management System
-- Basic SQL Queries
-- ============================================

USE librarydb;

-- ============================================
-- 1. Display all books
-- ============================================

SELECT *
FROM books;


-- ============================================
-- 2. Display all members
-- ============================================

SELECT *
FROM members;


-- ============================================
-- 3. Display all borrowing records
-- ============================================

SELECT *
FROM borrowing;


-- ============================================
-- 4. Find available books
-- ============================================

SELECT
    book_id,
    title,
    author,
    genre,
    published_year
FROM books
WHERE is_available = 1;


-- ============================================
-- 5. Find borrowed books
-- ============================================

SELECT
    book_id,
    title,
    author,
    genre,
    published_year
FROM books
WHERE is_available = 0;


-- ============================================
-- 6. Find books by genre
-- ============================================

SELECT
    title,
    author,
    genre
FROM books
WHERE genre = 'Programming';


-- ============================================
-- 7. Find books published after 1950
-- ============================================

SELECT
    title,
    author,
    published_year
FROM books
WHERE published_year > 1950
ORDER BY published_year;


-- ============================================
-- 8. Count total books
-- ============================================

SELECT COUNT(*) AS total_books
FROM books;


-- ============================================
-- 9. Count available books
-- ============================================

SELECT COUNT(*) AS available_books
FROM books
WHERE is_available = 1;


-- ============================================
-- 10. Count borrowed books
-- ============================================

SELECT COUNT(*) AS borrowed_books
FROM books
WHERE is_available = 0;


-- ============================================
-- 11. Count total members
-- ============================================

SELECT COUNT(*) AS total_members
FROM members;


-- ============================================
-- 12. Display active loans
-- ============================================

SELECT
    loan_id,
    book_id,
    member_id,
    borrow_date
FROM borrowing
WHERE return_date IS NULL;


-- ============================================
-- 13. Display returned books
-- ============================================

SELECT
    loan_id,
    book_id,
    member_id,
    borrow_date,
    return_date
FROM borrowing
WHERE return_date IS NOT NULL;


-- ============================================
-- 14. Display borrowing history with book title
-- ============================================

SELECT
    borrowing.loan_id,
    books.title,
    borrowing.borrow_date,
    borrowing.return_date
FROM borrowing
JOIN books
    ON borrowing.book_id = books.book_id;


-- ============================================
-- 15. Display borrowing history with member name
-- ============================================

SELECT
    borrowing.loan_id,
    members.name,
    borrowing.borrow_date,
    borrowing.return_date
FROM borrowing
JOIN members
    ON borrowing.member_id = members.member_id;


-- ============================================
-- 16. Complete borrowing report
-- ============================================

SELECT
    borrowing.loan_id,
    books.title AS book_title,
    members.name AS member_name,
    borrowing.borrow_date,
    borrowing.return_date
FROM borrowing
JOIN books
    ON borrowing.book_id = books.book_id
JOIN members
    ON borrowing.member_id = members.member_id
ORDER BY borrowing.borrow_date DESC;