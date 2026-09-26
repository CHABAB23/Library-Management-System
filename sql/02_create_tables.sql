-- ============================================
-- Library Management System
-- Create Tables
-- ============================================

USE librarydb;


-- ============================================
-- Books Table
-- ============================================

CREATE TABLE IF NOT EXISTS books (
    book_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100) DEFAULT NULL,
    published_year INT DEFAULT NULL,
    is_available TINYINT(1) DEFAULT 1,

    PRIMARY KEY (book_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;


-- ============================================
-- Members Table
-- ============================================

CREATE TABLE IF NOT EXISTS members (
    member_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) DEFAULT NULL,
    phone_number VARCHAR(15) DEFAULT NULL,
    join_date DATE DEFAULT NULL,

    PRIMARY KEY (member_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;


-- ============================================
-- Borrowing Table
-- ============================================

CREATE TABLE IF NOT EXISTS borrowing (
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

) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;