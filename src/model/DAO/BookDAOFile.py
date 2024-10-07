from Book import Book
from BookJSONSerializer import BookJSONSerializer
from FilePersistence import FilePersistence

class BookDAOFile:
    def __init__(self, patchFile):
        self.__patchFile = patchFile
        self.__books = []
        self.__filePersistence = FilePersistence()
        self.__serializer = BookJSONSerializer()

    @property
    def books(self):
        return self.__books
    
    @books.setter
    def books(self, books):
        self.__books = books
    
    def save(self, book):
        if isinstance(Book, book):
            books = self.findAll()
            self.books.append(book)

            jsonData = self.__serializer.toFile(books)
            self.__filePersistence.saveToFile(jsonData, self.__patchFile)

    def update(self, code, obj):
        pass

    def remove(self, code):
        book = self.find(code)
        if isinstance(Book, book):
            if book is not None:
                books = self.findAll()
                books.remove(book)

                jsonData = self.__serializer.toFile(books)
                self.__filePersistence.saveToFile(jsonData, self.__patchFile)

    def find(self, code):
        books = self.findAll()

        for book in self.__books:
            if book.isbn == code:
                return book
        
        return None


    def findAll(self):
        jsonData = self.__filePersistence.loadFromFile(self.__patchFile)
        return self.__serializer.fromFile(jsonData)