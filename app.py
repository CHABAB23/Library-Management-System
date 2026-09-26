from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection

app = Flask(__name__)

app.secret_key = "library-management-secret-key"

@app.route("/")
def home():

    connection = get_db_connection()
    cursor = connection.cursor()

    # Total books
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    # Available books
    cursor.execute("""
        SELECT COUNT(*)
        FROM books
        WHERE is_available = 1
    """)
    available_books = cursor.fetchone()[0]

    # Borrowed books
    cursor.execute("""
        SELECT COUNT(*)
        FROM books
        WHERE is_available = 0
    """)
    borrowed_books = cursor.fetchone()[0]

    # Total members
    cursor.execute("SELECT COUNT(*) FROM members")
    total_members = cursor.fetchone()[0]

    # Active loans
    cursor.execute("""
        SELECT COUNT(*)
        FROM borrowing
        WHERE return_date IS NULL
    """)
    active_loans = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        total_books=total_books,
        available_books=available_books,
        borrowed_books=borrowed_books,
        total_members=total_members,
        active_loans=active_loans
    )

# Books Management


@app.route("/books")
def books():

    search = request.args.get("search", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if search:
        cursor.execute("""
            SELECT
                book_id,
                title,
                author,
                genre,
                published_year,
                is_available
            FROM books
            WHERE title LIKE %s
               OR author LIKE %s
               OR genre LIKE %s
            ORDER BY book_id
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))
    else:
        cursor.execute("""
            SELECT
                book_id,
                title,
                author,
                genre,
                published_year,
                is_available
            FROM books
            ORDER BY book_id
        """)

    books = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "books.html",
        books=books,
        search=search
    )


@app.route("/books/add", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        genre = request.form.get("genre", "").strip()
        published_year = request.form.get("published_year", "").strip()

        # Validate required fields
        if not title or not author:
            flash("Title and author are required.", "error")
            return render_template("add_book.html")

        # Validate published year
        if published_year:
            try:
                published_year = int(published_year)

                if published_year < 0 or published_year > 2100:
                    flash(
                        "Published year must be between 0 and 2100.",
                        "error"
                    )
                    return render_template("add_book.html")

            except ValueError:
                flash(
                    "Published year must be a valid number.",
                    "error"
                )
                return render_template("add_book.html")
        else:
            published_year = None

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""
                INSERT INTO books
                (title, author, genre, published_year, is_available)
                VALUES (%s, %s, %s, %s, 1)
            """, (
                title,
                author,
                genre or None,
                published_year
            ))

            connection.commit()

            flash("Book added successfully!", "success")

        except Exception as error:

            connection.rollback()

            flash(
                f"Could not add book: {error}",
                "error"
            )

        finally:

            cursor.close()
            connection.close()

        return redirect(url_for("books"))

    return render_template("add_book.html")



@app.route("/books/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):

    connection = get_db_connection()

    if request.method == "POST":

        title = request.form["title"]
        author = request.form["author"]
        genre = request.form["genre"]
        published_year = request.form["published_year"]

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE books
            SET title = %s,
                author = %s,
                genre = %s,
                published_year = %s
            WHERE book_id = %s
        """, (
            title,
            author,
            genre,
            published_year,
            book_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        flash("Book updated successfully!", "success")

        return redirect(url_for("books"))

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM books
        WHERE book_id = %s
    """, (book_id,))

    book = cursor.fetchone()

    cursor.close()
    connection.close()

    if book is None:
        return "Book not found", 404

    return render_template("edit_book.html", book=book)


@app.route("/books/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check whether this book has borrowing history
        cursor.execute("""
            SELECT COUNT(*)
            FROM borrowing
            WHERE book_id = %s
        """, (book_id,))

        borrowing_count = cursor.fetchone()[0]

        if borrowing_count > 0:
            flash(
                "Cannot delete this book because it has borrowing history.",
                "error"
            )

            return redirect(url_for("books"))

        # Delete the book
        cursor.execute("""
            DELETE FROM books
            WHERE book_id = %s
        """, (book_id,))

        if cursor.rowcount == 0:
            flash("Book not found.", "error")
        else:
            connection.commit()
            flash("Book deleted successfully!", "success")

    except Exception as error:

        connection.rollback()

        flash(
            f"Could not delete book: {error}",
            "error"
        )

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("books"))


# Members Management

# MEMBERS
@app.route("/members")
def members():

    search = request.args.get("search", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if search:
        cursor.execute("""
            SELECT
                member_id,
                name,
                email,
                phone_number,
                join_date
            FROM members
            WHERE name LIKE %s
               OR email LIKE %s
            ORDER BY member_id
        """, (
            f"%{search}%",
            f"%{search}%"
        ))
    else:
        cursor.execute("""
            SELECT
                member_id,
                name,
                email,
                phone_number,
                join_date
            FROM members
            ORDER BY member_id
        """)

    members = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "members.html",
        members=members,
        search=search
    )


@app.route("/members/add", methods=["GET", "POST"])
def add_member():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        join_date = request.form["join_date"]

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO members
            (name, email, phone_number, join_date)
            VALUES (%s, %s, %s, %s)
        """, (
            name,
            email,
            phone_number,
            join_date
        ))

        connection.commit()

        cursor.close()
        connection.close()

        flash("Member added successfully!", "success")

        return redirect(url_for("members"))

    return render_template("add_member.html")



@app.route("/members/edit/<int:member_id>", methods=["GET", "POST"])
def edit_member(member_id):

    connection = get_db_connection()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        join_date = request.form["join_date"]

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE members
            SET name = %s,
                email = %s,
                phone_number = %s,
                join_date = %s
            WHERE member_id = %s
        """, (
            name,
            email,
            phone_number,
            join_date,
            member_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("members"))

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM members
        WHERE member_id = %s
    """, (member_id,))

    member = cursor.fetchone()

    cursor.close()
    connection.close()

    if member is None:
        return "Member not found", 404

    return render_template(
        "edit_member.html",
        member=member
    )

@app.route("/members/delete/<int:member_id>", methods=["POST"])
def delete_member(member_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check whether this member has borrowing history
        cursor.execute("""
            SELECT COUNT(*)
            FROM borrowing
            WHERE member_id = %s
        """, (member_id,))

        borrowing_count = cursor.fetchone()[0]

        if borrowing_count > 0:
            flash(
                "Cannot delete this member because they have borrowing history.",
                "error"
            )

            return redirect(url_for("members"))

        # Delete the member
        cursor.execute("""
            DELETE FROM members
            WHERE member_id = %s
        """, (member_id,))

        if cursor.rowcount == 0:
            flash("Member not found.", "error")
        else:
            connection.commit()
            flash("Member deleted successfully!", "success")

    except Exception as error:

        connection.rollback()

        flash(
            f"Could not delete member: {error}",
            "error"
        )

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("members"))


#  the Borrowing System 📚

@app.route("/borrowing")
def borrowing():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            borrowing.loan_id,
            books.title,
            members.name,
            borrowing.borrow_date,
            borrowing.return_date
        FROM borrowing
        JOIN books
            ON borrowing.book_id = books.book_id
        JOIN members
            ON borrowing.member_id = members.member_id
        ORDER BY borrowing.loan_id DESC
    """)

    loans = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "borrowing.html",
        loans=loans
    )


@app.route("/borrowing/borrow", methods=["GET", "POST"])
def borrow_book():

    connection = get_db_connection()

    if request.method == "POST":

        book_id = request.form.get("book_id")
        member_id = request.form.get("member_id")

        cursor = connection.cursor()

        try:
            # Check member
            cursor.execute("""
                SELECT member_id
                FROM members
                WHERE member_id = %s
            """, (member_id,))

            member = cursor.fetchone()

            if member is None:
                flash("Selected member does not exist.", "error")
                return redirect(url_for("borrow_book"))

            # Check book
            cursor.execute("""
                SELECT book_id, is_available
                FROM books
                WHERE book_id = %s
            """, (book_id,))

            book = cursor.fetchone()

            if book is None:
                flash("Selected book does not exist.", "error")
                return redirect(url_for("borrow_book"))

            # Check availability
            if book[1] == 0:
                flash("This book is already borrowed.", "error")
                return redirect(url_for("borrow_book"))

            # Create borrowing record
            cursor.execute("""
                INSERT INTO borrowing
                (
                    book_id,
                    member_id,
                    borrow_date,
                    return_date
                )
                VALUES (%s, %s, CURDATE(), NULL)
            """, (
                book_id,
                member_id
            ))

            # Mark book as unavailable
            cursor.execute("""
                UPDATE books
                SET is_available = 0
                WHERE book_id = %s
            """, (book_id,))

            connection.commit()

            flash("Book borrowed successfully!", "success")

        except Exception as error:

            connection.rollback()

            flash(
                f"Could not borrow book: {error}",
                "error"
            )

        finally:

            cursor.close()
            connection.close()

        return redirect(url_for("borrowing"))

    # Get available books
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            book_id,
            title,
            author
        FROM books
        WHERE is_available = 1
        ORDER BY title
    """)

    books = cursor.fetchall()

    # Get members
    cursor.execute("""
        SELECT
            member_id,
            name,
            email
        FROM members
        ORDER BY name
    """)

    members = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "borrow_book.html",
        books=books,
        members=members
    )



    

@app.route("/borrowing/return/<int:loan_id>", methods=["POST"])
def return_book(loan_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    # Find the book associated with this loan
    cursor.execute("""
        SELECT book_id, return_date
        FROM borrowing
        WHERE loan_id = %s
    """, (loan_id,))

    loan = cursor.fetchone()

    if loan is None:
        cursor.close()
        connection.close()
        return "Loan not found", 404

    book_id = loan[0]
    return_date = loan[1]

    # Check if the book was already returned
    if return_date is not None:
        cursor.close()
        connection.close()
        return "This book has already been returned.", 400

    # Mark borrowing record as returned
    cursor.execute("""
        UPDATE borrowing
        SET return_date = CURDATE()
        WHERE loan_id = %s
    """, (loan_id,))

    # Make the book available again
    cursor.execute("""
        UPDATE books
        SET is_available = 1
        WHERE book_id = %s
    """, (book_id,))

    connection.commit()

    cursor.close()
    connection.close()

    flash("Book returned successfully!", "success")

    return redirect(url_for("borrowing"))
    



if __name__ == "__main__":
    app.run(debug=True)