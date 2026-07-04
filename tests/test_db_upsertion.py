from db.connection import ConnectToDB
import pytest


@pytest.fixture
def db(tmp_path):
    conn = ConnectToDB(tmp_path / "test2.db")
    conn.init_db()
    return conn


def test_db_upsertion(db):
    db.insert_articles(
        [{"title": "Hello", "price": "29", "img": "imageLink", "rating": "Three"}]
    )

    db.insert_articles(
        [{"title": "Hello", "price": "300", "img": "imageLink", "rating": "Three"}]
    )

    rows = db.get_connection().execute("SELECT title, price FROM books").fetchall()
    assert rows == [("Hello", "300")]
