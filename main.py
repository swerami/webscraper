import logging
import time

import requests

from scraper.fetch import FetchPage
from scraper.parse import Parser
from db.connection import ConnectToDB
import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("basic.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
logger.info("Starting app...")

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
            continue

        except Exception as e:
            continue

        finally:
            time.sleep(config.delay)


fetch_articles()
