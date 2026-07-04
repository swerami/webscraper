from db.connection import ConnectToDB
import pytest


@pytest.fixture
def db(tmp_path):
    connecttodb = ConnectToDB(tmp_path / "test.db")
    connecttodb.init_db()
    return connecttodb


def test_insert(db):
    db.insert_articles([{"title": "X", "price": "£1", "rating": "One", "img": "y.jpg"}])

    rows = db.get_connection().execute("SELECT title, price FROM books").fetchall()
    assert rows == [("X", "£1")]
