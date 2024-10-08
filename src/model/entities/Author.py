from Person import Person
from Book import Book
from typing import List

class Author(Person):
    def __init__(self, name=None, age=None, cpf=None, booksWritten=None):
        
        super().__init__(name, age, cpf)
        self.__booksWritten = booksWritten if booksWritten is not None else []
    
    @property
    def booksWritten(self) -> List[Book]:
        return self.__booksWritten
    
    @booksWritten.setter
    def booksWritten(self, booksWritten) -> None:
        self.__booksWritten = booksWritten

    def print(self):
        super().print()
        print()
        print("Books Written:\n")
        print()
        for c in self.booksWritten:
            print(c.print())
    
    def fill(self):
        bookList = []
        super().fill()
        p = ''

        print('-------------Book Fill--------------')
        while p is not 'n':
            book = Book()
            book.fill()
            bookList.append(book)
        
        self.bookList = bookList
        
    def toDict(self) -> dict:
        return{
            'name': self.name,
            'age': self.age,
            'cpf': self.cpf,
            'booksWritten': [book.toDict() for book in self.booksWritten]
        }
    
    def fromDict(data):
        author = Author(name=data['name'], age=data['age'], cpf=data['cpf'])
        author.booksWritten = [Book.fromDict(bookData) for bookData in data['booksWritten']]
        return author
        