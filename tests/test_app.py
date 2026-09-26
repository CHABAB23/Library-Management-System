import pytest

from app import app
from database import get_db_connection


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


# ============================================================
# DASHBOARD
# ============================================================

def test_dashboard(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Library" in response.data


# ============================================================
# BOOKS
# ============================================================

def test_books_page(client):
    response = client.get("/books")

    assert response.status_code == 200
    assert b"Books" in response.data


def test_add_book_page(client):
    response = client.get("/books/add")

    assert response.status_code == 200
    assert b"Add" in response.data


def test_add_book_validation(client):
    response = client.post(
        "/books/add",
        data={
            "title": "",
            "author": "",
            "genre": "Testing",
            "published_year": "2024"
        }
    )

    assert response.status_code == 200
    assert b"Title and author are required." in response.data


def test_add_book(client):
    title = "Pytest Library Test Book"

    try:
        response = client.post(
            "/books/add",
            data={
                "title": title,
                "author": "Test Author",
                "genre": "Testing",
                "published_year": "2025"
            },
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Book added successfully!" in response.data
        assert title.encode() in response.data

    finally:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM books WHERE title = %s",
            (title,)
        )

        connection.commit()
        cursor.close()
        connection.close()


def test_search_books(client):
    response = client.get("/books?search=Gatsby")

    assert response.status_code == 200
    assert b"The Great Gatsby" in response.data


def test_edit_book(client):
    original_title = "Pytest Edit Book"
    updated_title = "Pytest Edited Book"

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO books
            (title, author, genre, published_year, is_available)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                original_title,
                "Test Author",
                "Testing",
                2025,
                1
            )
        )

        connection.commit()

        book_id = cursor.lastrowid

        response = client.post(
            f"/books/edit/{book_id}",
            data={
                "title": updated_title,
                "author": "Updated Author",
                "genre": "Updated Genre",
                "published_year": "2026"
            },
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Book updated successfully!" in response.data
        assert updated_title.encode() in response.data

    finally:
        cursor.execute(
            """
            DELETE FROM books
            WHERE title IN (%s, %s)
            """,
            (original_title, updated_title)
        )

        connection.commit()
        cursor.close()
        connection.close()


def test_delete_book(client):
    title = "Pytest Delete Book"

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO books
            (title, author, genre, published_year, is_available)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                title,
                "Delete Author",
                "Testing",
                2025,
                1
            )
        )

        connection.commit()

        book_id = cursor.lastrowid

        response = client.post(
            f"/books/delete/{book_id}",
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Book deleted successfully!" in response.data

        cursor.execute(
            "SELECT * FROM books WHERE book_id = %s",
            (book_id,)
        )

        assert cursor.fetchone() is None

    finally:
        cursor.execute(
            "DELETE FROM books WHERE title = %s",
            (title,)
        )

        connection.commit()
        cursor.close()
        connection.close()


def test_cannot_delete_book_with_borrowing_history(client):
    response = client.post(
        "/books/delete/1",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert (
        b"Cannot delete this book because it has borrowing history."
        in response.data
    )


# ============================================================
# MEMBERS
# ============================================================

def test_members_page(client):
    response = client.get("/members")

    assert response.status_code == 200
    assert b"Members" in response.data


def test_add_member_page(client):
    response = client.get("/members/add")

    assert response.status_code == 200
    assert b"Add" in response.data


def test_add_member(client):
    email = "pytest.member@example.com"

    try:
        response = client.post(
            "/members/add",
            data={
                "name": "Pytest Member",
                "email": email,
                "phone_number": "0600000000",
                "join_date": "2026-09-26"
            },
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Member added successfully!" in response.data
        assert b"Pytest Member" in response.data

    finally:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM members WHERE email = %s",
            (email,)
        )

        connection.commit()
        cursor.close()
        connection.close()


def test_search_members(client):
    response = client.get("/members?search=Alen")

    assert response.status_code == 200
    assert b"Alen King" in response.data


def test_edit_member(client):
    original_email = "pytest.edit.member@example.com"
    updated_email = "pytest.edited.member@example.com"

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO members
            (name, email, phone_number, join_date)
            VALUES (%s, %s, %s, %s)
            """,
            (
                "Pytest Edit Member",
                original_email,
                "0611111111",
                "2026-09-26"
            )
        )

        connection.commit()

        member_id = cursor.lastrowid

        response = client.post(
            f"/members/edit/{member_id}",
            data={
                "name": "Pytest Edited Member",
                "email": updated_email,
                "phone_number": "0622222222",
                "join_date": "2026-09-27"
            },
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Pytest Edited Member" in response.data

    finally:
        cursor.execute(
            """
            DELETE FROM members
            WHERE email IN (%s, %s)
            """,
            (original_email, updated_email)
        )

        connection.commit()
        cursor.close()
        connection.close()


def test_delete_member(client):
    email = "pytest.delete.member@example.com"

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO members
            (name, email, phone_number, join_date)
            VALUES (%s, %s, %s, %s)
            """,
            (
                "Pytest Delete Member",
                email,
                "0633333333",
                "2026-09-26"
            )
        )

        connection.commit()

        member_id = cursor.lastrowid

        response = client.post(
            f"/members/delete/{member_id}",
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Member deleted successfully!" in response.data

        cursor.execute(
            "SELECT * FROM members WHERE member_id = %s",
            (member_id,)
        )

        assert cursor.fetchone() is None

    finally:
        cursor.execute(
            "DELETE FROM members WHERE email = %s",
            (email,)
        )

        connection.commit()
        cursor.close()
        connection.close()


# ============================================================
# BORROWING
# ============================================================

def test_borrowing_page(client):
    response = client.get("/borrowing")

    assert response.status_code == 200
    assert b"Borrowing" in response.data


def test_borrow_book_page(client):
    response = client.get("/borrowing/borrow")

    assert response.status_code == 200
    assert response.status_code == 200


def test_borrow_and_return_book(client):
    book_title = "Pytest Borrow Book"
    member_email = "pytest.borrow.member@example.com"

    connection = get_db_connection()
    cursor = connection.cursor()

    book_id = None
    member_id = None
    loan_id = None

    try:
        # ----------------------------------------------------
        # Create temporary book
        # ----------------------------------------------------

        cursor.execute(
            """
            INSERT INTO books
            (title, author, genre, published_year, is_available)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                book_title,
                "Borrow Test Author",
                "Testing",
                2025,
                1
            )
        )

        book_id = cursor.lastrowid

        # ----------------------------------------------------
        # Create temporary member
        # ----------------------------------------------------

        cursor.execute(
            """
            INSERT INTO members
            (name, email, phone_number, join_date)
            VALUES (%s, %s, %s, %s)
            """,
            (
                "Pytest Borrow Member",
                member_email,
                "0644444444",
                "2026-09-26"
            )
        )

        member_id = cursor.lastrowid

        connection.commit()

        # ----------------------------------------------------
        # Borrow book
        # ----------------------------------------------------

        response = client.post(
            "/borrowing/borrow",
            data={
                "book_id": str(book_id),
                "member_id": str(member_id)
            },
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Book borrowed successfully!" in response.data

        # ----------------------------------------------------
        # Use a fresh connection to verify book status
        # ----------------------------------------------------

        check_connection = get_db_connection()
        check_cursor = check_connection.cursor()

        check_cursor.execute(
            """
            SELECT is_available
            FROM books
            WHERE book_id = %s
            """,
            (book_id,)
        )

        result = check_cursor.fetchone()

        assert result is not None
        assert result[0] == 0

        # ----------------------------------------------------
        # Find active loan
        # ----------------------------------------------------

        check_cursor.execute(
            """
            SELECT loan_id
            FROM borrowing
            WHERE book_id = %s
              AND member_id = %s
              AND return_date IS NULL
            ORDER BY loan_id DESC
            LIMIT 1
            """,
            (book_id, member_id)
        )

        loan = check_cursor.fetchone()

        assert loan is not None

        loan_id = loan[0]

        check_cursor.close()
        check_connection.close()

        # ----------------------------------------------------
        # Return book
        # ----------------------------------------------------

        response = client.post(
            f"/borrowing/return/{loan_id}",
            follow_redirects=True
        )

        assert response.status_code == 200
        assert b"Book returned successfully!" in response.data

        # ----------------------------------------------------
        # Fresh connection for return verification
        # ----------------------------------------------------

        check_connection = get_db_connection()
        check_cursor = check_connection.cursor()

        check_cursor.execute(
            """
            SELECT return_date
            FROM borrowing
            WHERE loan_id = %s
            """,
            (loan_id,)
        )

        result = check_cursor.fetchone()

        assert result is not None
        assert result[0] is not None

        # ----------------------------------------------------
        # Verify book is available again
        # ----------------------------------------------------

        check_cursor.execute(
            """
            SELECT is_available
            FROM books
            WHERE book_id = %s
            """,
            (book_id,)
        )

        result = check_cursor.fetchone()

        assert result is not None
        assert result[0] == 1

        check_cursor.close()
        check_connection.close()

    finally:
        # ----------------------------------------------------
        # Cleanup borrowing record
        # ----------------------------------------------------

        cleanup_connection = get_db_connection()
        cleanup_cursor = cleanup_connection.cursor()

        if book_id is not None:
            cleanup_cursor.execute(
                """
                DELETE FROM borrowing
                WHERE book_id = %s
                """,
                (book_id,)
            )

        # Cleanup temporary book
        if book_id is not None:
            cleanup_cursor.execute(
                """
                DELETE FROM books
                WHERE book_id = %s
                """,
                (book_id,)
            )

        # Cleanup temporary member
        if member_id is not None:
            cleanup_cursor.execute(
                """
                DELETE FROM members
                WHERE member_id = %s
                """,
                (member_id,)
            )

        cleanup_connection.commit()

        cleanup_cursor.close()
        cleanup_connection.close()

        cursor.close()
        connection.close()