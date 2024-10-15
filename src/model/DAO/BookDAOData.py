import sqlite3
from Book import Book
from IDAO import IDAO

class BookDAOData(IDAO):
    def __init__(self, connection):
        self.connection = connection

    def save(self, book: Book):
        sql = '''
INSERT INTO book (title, isbn, publicationYear) VALUES (?, ?, ?)
'''

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (
                book.title,
                book.isbn,
                book.publicationYear
            ))

            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def update(self, isbn, book: Book):
        sql = '''
UPDATE book
SET title = ?, isbn = ?, publicationYear = ?
WHERE isbn = ?
'''

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (
                book.title,
                book.isbn,
                book.publicationYear,
                isbn
            ))

            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def remove(self, isbn):
        sql = 'DELETE FROM book WHERE isbn'

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (isbn))
            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def find(self, isbn):
        sql = 'SELECT * FROM book WHERE isbn = ?'

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (isbn))
            row = cursor.fetchone()

            if row:
                return Book(
                    row[0],
                    row[1],
                    row[2]
                )

        except sqlite3.Error as e:
            print(e)

        return None

    def findAll(self):
        sql = 'SELECT * FROM book'
        books = []

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                books.append(Book(
                    row[0],
                    row[1],
                    row[2]
                ))

        except sqlite3.Error as e:
            print(e)

        return books