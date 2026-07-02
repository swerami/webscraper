import sqlite3

from config import db_url
import os

import logging

logger = logging.getLogger(__name__)

schemapath = os.getcwd() + "/db/schema.sql"


class ConnectToDB:
    def get_connection(self):
        return sqlite3.connect(db_url)

    def init_db(self):
        connection = self.get_connection()
        with open(schemapath) as f:
            schema = f.read()
            connection.executescript(schema)
            connection.commit()
            connection.close()

    def insert_articles(self, article_list):
        try:
            query = "INSERT OR IGNORE INTO books (title, img, price, rating) VALUES (:title, :img, :price, :rating)"
            db = self.get_connection()
            cursor = db.executemany(query, article_list)
            db.commit()
            db.close()
            logger.info(
                "%s article of %s have been successfully stored in the database!",
                cursor.rowcount,
                len(article_list),
            )
        except sqlite3.Error as e:
            logger.exception(
                "an error has occurred while trying to insert articles. Error message: %s",
                e,
            )
