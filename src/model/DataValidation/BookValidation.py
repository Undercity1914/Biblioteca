from Book import Book
from BookException import BookException

class BookValidation:
    def validation(self, title=None, isbn=None, publicationYear=None) -> Book:
        book = Book()
        if title is None:
            raise BookException("Titulo nao pode ser nulo.")
        book.title = title

        if isbn is None:
            raise BookException("ISBN nao pode ser nulo.")
        book.isbn = isbn

        if publicationYear is None:
            raise BookException("Ano de publicação nao pode ser nulo.")
        book.publicationYear = publicationYear

        return book