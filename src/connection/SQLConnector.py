import sqlite3
from sqlite3 import Error

class SQLConnector:
    def __init__(self, dataBase):
        self.connection = self.creatConnection(dataBase)
        if self.connection is not None:
            self.createTableAuthor()
            self.createTableUser()
            self.createTableBook()
        
        else:
            print("Connection not exists!")
    
    def creatConnection(self, dataBase):
        connection = None

        try:
            connection = sqlite3.connect(dataBase)
        
        except Error as e:
            print(e)
        
        return connection
    
    def createTableAuthor(self):
        sql = '''
CREATE TABLE IF NOT EXISTS author(
    ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age TEXT NOT NULL,
    cpf TEXT NOT NULL,
    bookList TEXT NOT NULL
);
'''
        self.executeQuery(sql)
    
    def createTableUser(self):
        sql = '''
CREATE TABLE IF NOT EXISTS user(
    ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age TEXT NOT NULL,
    cpf TEXT NOT NULL,
    booklist TEXT NOT NULL
);
'''
        self.executeQuery(sql)

    def createTableBook(self):
        sql = '''
CREATE TABLE IF NOT EXISTS book(
    ID INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    isbn TEXT NOT NULL,
	publicationYear TEXT NOT NULL
);
'''


    def executeQuery(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        
        except Error as e:
            print(e)

    def closeConnection(self):
        if self.connection:
            self.connection.close()
    