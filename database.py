import sqlite3

class mydatabase:

    def __init__(self):
        self.db = sqlite3.connect("books-collection.db")