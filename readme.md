![Python](https://img.shields.io/badge/Python-3.12-202020?style=for-the-badge&logo=python&logoColor=FFD343&labelColor=0D1117)
![pytest](https://img.shields.io/badge/pytest-202020?style=for-the-badge&logo=pytest&logoColor=white&labelColor=0D1117)
![SQLite](https://img.shields.io/badge/SQLite-202020?style=for-the-badge&logo=sqlite&logoColor=4DB8FF&labelColor=0D1117)
# Web Scraper
a python web scraper that collects book data from books.toescrape.com into a SQLite database.

## 1. What it does
scrapes title, price, rating, and image for each book, stores it in an SQLite database. The tool was designed to be **re-runnable**, which refreshes the data without creating duplicates.

## 2. Features
* CLI flags for pages and delay (--pages, --delay)
* Automatic retries with exponential backoff on network failure (like 5xx errors)
* Upsert so re-runs updates prices without inserting duplicates
* Logging to file + console with rotation 
* Tested with pytest

## 3. Setup
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

I use python 3.12.3, so make sure you have the same version or newer.

## 4. Usage
* `python3 main.py`: scrapes all pages, with default delay
* `python3 main.py --pages 3 --delay 2`: scrapes 3 pages, 2s delay for each
* `python3 main.py --help`: see all options 

## 5. How it works
I have separated each functionality to its own class to ensure separation of concern.
* fetch.py handles fetching the page and returning the response
* parse.py handles parsing the html page and returning a list of dictionaries of every article
* connection.py handles initiating the db, creating the connection, and inserting the list of books into the db
* main.py orchestrates all that in one function and handles exceptions should they occur

## 6. Design decisions 
* SQLite - doesn't require any setup, only a single file and very fit for the purpose of this project.
* Upsert on title - since there are no keys, I used title as the primary key. re-runs will only update the price if they are different, and it will not create duplicates.
* Retry + backoff - handled transient network/5xx errors to prevent skipping an entire page should they occur. 
* Delay between requests - don't wanna hammer the server haha.

## 7. Running tests
run: `python -m pytest`
