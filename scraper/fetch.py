import time

import requests

import logging

from config import backoff, retries

logger = logging.getLogger(__name__)


class FetchPage:
    def __init__(self, url):
        self.url = url

    def fetch(self, query):

        url = f"{self.url}{query}"
        for attempt in range(1, retries + 1):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                response.encoding = "utf-8"
                logger.info("fetched %s successfully", url)
                return response
            except requests.exceptions.HTTPError as e:
                if e.response.status_code < 500:
                    raise
                last_error = e

            except requests.exceptions.RequestException as e:
                last_error = e

            if attempt == retries:
                raise last_error

            wait = backoff * (2 ** (attempt - 1))
            logger.warning(
                "page %s attempt %s failed, retrying in %ss", query, attempt, wait
            )
            time.sleep(wait)
