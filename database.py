import sqlite3

class mydatabase:

    def __init__(self):
        self.db = sqlite3.connect("books-collection.db")
        self.cursor = self.db.cursor()

    def create_book(self):
        self.cursor.execute(
            "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

    def insert_book(self):
        self.cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
        self.db.commit()



