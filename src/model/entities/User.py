from Person import Person
from typing import List
from Book import Book

class User(Person):
    def __init__(self=None, name=None, age=None, cpf=None, bookList=None):
        super().__init__(name, age, cpf)
        self.__bookList = bookList if bookList is not None else []

    @property
    def bookList(self) -> List[Book]:
        return self.__bookList
    
    @bookList.setter
    def bookList(self, bookList) -> None:
        self.__bookList = bookList
    
    def print(self) -> None:
        super().print()
        for book in self.bookList:
            book.print()
    
    def fill(self) -> None:
        bookList = []
        super().fill()
        p = ''
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
            'bookList': [book.toDict() for book in self.bookList]
        }
    
    def fromDict(data):
        user = User(name=data['name'], age=data['age'], cpf=data['cpf'])
        user.bookList = [Book.fromDict(bookData) for bookData in data['bookList']]
        return user