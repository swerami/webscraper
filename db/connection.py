import sqlite3

from config import db_url
import os

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
        query = "INSERT OR IGNORE INTO books (title, img, price, rating) VALUES (:title, :img, :price, :rating)"
        db = self.get_connection()
        db.executemany(query, article_list)
        db.commit()
        db.close()
