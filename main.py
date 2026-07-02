import time

import requests

from scraper.fetch import FetchPage
from scraper.parse import Parser
from db.connection import ConnectToDB
import config

fetch = FetchPage(config.base_url)
db = ConnectToDB()
db.init_db()


def fetch_articles():
    for i in range(1, 51):
        try:
            response = fetch.fetch(f"/catalogue/page-{i}.html")
            if response.status_code == 404:
                break
            else:
                print(f"Downloading page {i}...")
            parser = Parser(response.text)
            parsed_articles = parser.parse_articles()

            db.insert_articles(parsed_articles)
        except requests.exceptions.RequestException as e:
            print(f"page {i}: network error -> {e}")
            continue

        except Exception as e:
            print(f"page {i}: failed to parse/insert ->> {e}")
            continue

        finally:
            time.sleep(config.delay)


# fetch_articles()
