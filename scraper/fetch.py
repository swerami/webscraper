import requests

import logging

logger = logging.getLogger(__name__)


class FetchPage:
    def __init__(self, url):
        self.url = url

    def fetch(self, arg):
        url = f"{self.url}{arg}"
        try:
            response = requests.get(url)
            response.encoding = "utf-8"
            logger.info("fetched %s successfully", url)
            return response
        except requests.exceptions as e:
            logger.exception("error occurred when fetching %s: %s", url, e)
