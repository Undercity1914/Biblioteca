import sqlite3
from BookJSONSerializer import BookJSONSerializer
from Author import Author
from IDAO import IDAO

class Author(IDAO):
    

    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def save(self, author: Author):
        sql = '''
INSERT INTO author (name, cpf, age, bookList) VALUES (?, ?, ?, ?)
'''

        serializer = BookJSONSerializer()
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                author.name,
                author.age,
                author.cpf,
                serializer.toFile(author.booksWritten)
            ))

            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def update(self, cpf, author: Author):
        sql = '''
UPDATE author 
SET name = ?, age = ?, bookList = ?
WHERE cpf = ?
'''

        serializer  = BookJSONSerializer()

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                author.name,
                author.age,
                author.cpf,
                serializer.toFile(author.booksWritten),
                cpf                
            ))

            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def remove(self, cpf):
        sql = 'DELETE FROM author WHERE cpf = ?'

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (cpf))
            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def find(self, cpf):
        sql = 'SELECT * FROM author WHERE cpf = ?'
        serializer = BookJSONSerializer()

        try:
            
            cursor = self.connection.cursor()
            cursor.execute(sql, (cpf))
            row = cursor.fetchone()

            if row:
                return Author(
                    row[0],
                    row[1],
                    row[2],
                    serializer.fromFile(row[3])
                )

        except sqlite3.Error as e:
            print(e)

        return None

    def findAll(self):
        sql = 'SELECT * FROM author'
        auhtors = []
        serializer = BookJSONSerializer()

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                auhtors.append(Author(
                    row[0],
                    row[1],
                    row[2],
                    serializer.fromFile(row[3])
                ))

        except sqlite3.Error as e:
            print(e)

        return auhtors