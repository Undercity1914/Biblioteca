from Person import Person
from Book import Book

class Author(Person):
    def __init__(self, name=None, age=None, cpf=None, booksWritten=None):
        if all([name, age, cpf, booksWritten]):
            super().__init__(name, age, cpf)
            self.__booksWritten = booksWritten
        else:
            super().__init__()
            self.__booksWritten = []
    
    @property
    def booksWritten(self):
        return self.__booksWritten
    
    @booksWritten.setter
    def booksWritten(self, booksWritten):
        self.__booksWritten = booksWritten

    def print(self):
        super().print()
        print()
        print("Books Written:\n")
        print()
        for c in self.booksWritten:
            print(c.print())
    
    def fill(self):
        super().fill()
        more = 's'
        book = Book()

        print("------------Book fill---------------")
        
        while more == 's':
            book.fill()
            self.booksWritten.append(book)
            more = str(input("Você deseja adicionar mais livros?[s/n] "))
        
