-- ============================================
-- Library Management System
-- Advanced SQL Queries
-- ============================================

USE librarydb;


-- ============================================
-- 1. Complete borrowing report
-- ============================================

SELECT
    b.title AS book_title,
    m.name AS member_name,
    br.borrow_date,
    br.return_date
FROM borrowing br
JOIN books b
    ON br.book_id = b.book_id
JOIN members m
    ON br.member_id = m.member_id
ORDER BY br.borrow_date DESC;


-- ============================================
-- 2. Currently borrowed books
-- ============================================

SELECT
    b.title AS book_title,
    b.author,
    m.name AS member_name,
    br.borrow_date
FROM borrowing br
JOIN books b
    ON br.book_id = b.book_id
JOIN members m
    ON br.member_id = m.member_id
WHERE br.return_date IS NULL
ORDER BY br.borrow_date;


-- ============================================
-- 3. Number of books borrowed by each member
-- ============================================

SELECT
    m.member_id,
    m.name,
    COUNT(br.loan_id) AS total_borrowings
FROM members m
LEFT JOIN borrowing br
    ON m.member_id = br.member_id
GROUP BY
    m.member_id,
    m.name
ORDER BY total_borrowings DESC;


-- ============================================
-- 4. Number of books in each genre
-- ============================================

SELECT
    genre,
    COUNT(*) AS total_books
FROM books
GROUP BY genre
ORDER BY total_books DESC;


-- ============================================
-- 5. Members with active loans
-- ============================================

SELECT DISTINCT
    m.member_id,
    m.name,
    m.email
FROM members m
JOIN borrowing br
    ON m.member_id = br.member_id
WHERE br.return_date IS NULL;


-- ============================================
-- 6. Books that have never been borrowed
-- ============================================

SELECT
    b.book_id,
    b.title,
    b.author
FROM books b
LEFT JOIN borrowing br
    ON b.book_id = br.book_id
WHERE br.loan_id IS NULL;


-- ============================================
-- 7. Most borrowed books
-- ============================================

SELECT
    b.book_id,
    b.title,
    b.author,
    COUNT(br.loan_id) AS borrow_count
FROM books b
LEFT JOIN borrowing br
    ON b.book_id = br.book_id
GROUP BY
    b.book_id,
    b.title,
    b.author
ORDER BY borrow_count DESC;


-- ============================================
-- 8. Books published between 1900 and 2000
-- ============================================

SELECT
    title,
    author,
    published_year
FROM books
WHERE published_year BETWEEN 1900 AND 2000
ORDER BY published_year;


-- ============================================
-- 9. Search books by title
-- ============================================

SELECT
    book_id,
    title,
    author,
    genre
FROM books
WHERE title LIKE '%The%';


-- ============================================
-- 10. Members who joined in 2026
-- ============================================

SELECT
    member_id,
    name,
    email,
    join_date
FROM members
WHERE YEAR(join_date) = 2026
ORDER BY join_date;


-- ============================================
-- 11. Total borrowing records
-- ============================================

SELECT COUNT(*) AS total_borrowing_records
FROM borrowing;


-- ============================================
-- 12. Average number of borrowings per member
-- ============================================

SELECT
    AVG(borrow_count) AS average_borrowings
FROM (
    SELECT
        member_id,
        COUNT(*) AS borrow_count
    FROM borrowing
    GROUP BY member_id
) AS member_borrowings;


-- ============================================
-- 13. Books with their availability status
-- ============================================

SELECT
    book_id,
    title,
    author,
    CASE
        WHEN is_available = 1 THEN 'Available'
        ELSE 'Borrowed'
    END AS availability_status
FROM books
ORDER BY title;


-- ============================================
-- 14. Members and their borrowing history
-- ============================================

SELECT
    m.name AS member_name,
    b.title AS book_title,
    br.borrow_date,
    br.return_date
FROM members m
LEFT JOIN borrowing br
    ON m.member_id = br.member_id
LEFT JOIN books b
    ON br.book_id = b.book_id
ORDER BY
    m.name,
    br.borrow_date DESC;


-- ============================================
-- 15. Dashboard statistics in one query
-- ============================================

SELECT
    (SELECT COUNT(*) FROM books) AS total_books,

    (SELECT COUNT(*)
     FROM books
     WHERE is_available = 1) AS available_books,

    (SELECT COUNT(*)
     FROM books
     WHERE is_available = 0) AS borrowed_books,

    (SELECT COUNT(*) FROM members) AS total_members,

    (SELECT COUNT(*)
     FROM borrowing
     WHERE return_date IS NULL) AS active_loans;