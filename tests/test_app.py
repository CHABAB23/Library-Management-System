import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_dashboard(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Library" in response.data


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
            "genre": "Test",
            "published_year": "2024"
        }
    )

    assert response.status_code == 200
    assert b"Title and author are required." in response.data