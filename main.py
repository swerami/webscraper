import argparse
import logging
import time

import requests

from scraper.fetch import FetchPage
from scraper.parse import Parser
from db.connection import ConnectToDB
import config


parser = argparse.ArgumentParser(description="Let's scrape books.toscrape!")
parser.add_argument("--pages", type=int, default=50, help="How many pages to scrape?")
parser.add_argument(
    "--delay",
    type=float,
    default=0.5,
    help="How much delay between fetching each page?",
)

args = parser.parse_args()


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
    for i in range(1, args.pages + 1):
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
            time.sleep(args.delay)


fetch_articles()
