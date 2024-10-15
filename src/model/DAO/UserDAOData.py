from User import User
import sqlite3
from BookJSONSerializer import BookJSONSerializer
from IDAO import IDAO

class UserDAOData(IDAO):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def save(self, user: User):
        sql = '''
INSERT INTO user (name, cpf, age, bookList) VALUES (?, ?, ?, ?)
'''

        serializer = BookJSONSerializer()
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                user.name,
                user.age,
                user.cpf,
                serializer.toFile(user.booksWritten)
            ))

            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def update(self, cpf, user: User):
        sql = '''
UPDATE user 
SET name = ?, age = ?, bookList = ?
WHERE cpf = ?
'''

        serializer  = BookJSONSerializer()

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                user.name,
                user.age,
                user.cpf,
                serializer.toFile(user.booksWritten),
                cpf                
            ))

            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def remove(self, cpf):
        sql = 'DELETE FROM user WHERE cpf = ?'

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql, (cpf))
            self.connection.commit()

        except sqlite3.Error as e:
            print(e)

    def find(self, cpf):
        sql = 'SELECT * FROM user WHERE cpf = ?'
        serializer = BookJSONSerializer()

        try:
            
            cursor = self.connection.cursor()
            cursor.execute(sql, (cpf))
            row = cursor.fetchone()

            if row:
                return User(
                    row[0],
                    row[1],
                    row[2],
                    serializer.fromFile(row[3])
                )

        except sqlite3.Error as e:
            print(e)

    def findAll(self):
        sql = 'SELECT * FROM user'
        users = []
        serializer = BookJSONSerializer()

        try:

            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                users.append(User(
                    row[0],
                    row[1],
                    row[2],
                    serializer.fromFile(row[3])
                ))

        except sqlite3.Error as e:
            print(e)

        return users