CREATE TABLE IF NOT EXISTS books(
    bookId INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    img TEXT,
    price TEXT,
    rating TEXT
)
