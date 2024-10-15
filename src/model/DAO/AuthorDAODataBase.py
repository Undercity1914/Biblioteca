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