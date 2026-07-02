from bs4 import BeautifulSoup

import logging

logger = logging.getLogger(__name__)


class Parser:
    def __init__(self, html):
        self.html = html

    def parse(self):
        soup = BeautifulSoup(self.html, "html.parser")
        return soup

    def parse_articles(self):
        parsedHtml = self.parse()
        articles = parsedHtml.find_all("article")
        article_list = list()

        for article in articles:
            h3_tag = article.find("h3")
            title = ""
            if h3_tag:
                title_tag = h3_tag.find("a")
                if title_tag:
                    title = title_tag["title"]
            price = article.find("p", class_="price_color").text
            rating = article.find("p", class_="star-rating")["class"][1]
            img = article.find("img", class_="thumbnail")["src"]
            article_list.append(dict(title=title, price=price, rating=rating, img=img))
        return article_list
