import requests


class FetchPage:
    def __init__(self, url):
        self.url = url

    def fetch(self, arg):
        response = requests.get(f"{self.url}{arg}")
        response.encoding = "utf-8"
        return response
