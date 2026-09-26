-- ============================================
-- Library Management System
-- Insert Sample Data
-- ============================================

USE librarydb;

-- ============================================
-- Insert Books
-- ============================================

INSERT INTO books
(title, author, genre, published_year, is_available)
VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 0),
('1984', 'George Orwell', 'Dystopian', 1949, 1),
('To Kill a Mockingbird', 'Harper Lee', 'Classic', 1960, 1),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy Adventure', 1937, 1),
('The Alchemist', 'Paulo Coelho', 'Adventure', 1988, 1),
('Clean Code', 'Robert C. Martin', 'Programming', 2008, 1);

-- ============================================
-- Insert Members
-- ============================================

INSERT INTO members
(name, email, phone_number, join_date)
VALUES
('Alen King', 'alenking@example.com', '0612345678', '2026-09-20'),
('Alece Hofman', 'alecehofman@example.com', '0612345679', '2026-09-22'),
('John Smith', 'johnsmith@example.com', '0612345680', '2026-09-26');

-- ============================================
-- Insert Borrowing Records
-- ============================================

INSERT INTO borrowing
(book_id, member_id, borrow_date, return_date, librarian_id)
VALUES
(1, 1, '2026-09-20', NULL, NULL),
(2, 2, '2026-08-10', '2026-08-15', NULL),
(4, 1, '2026-09-26', '2026-09-26', NULL);

-- ============================================
-- End of Sample Data
-- ============================================