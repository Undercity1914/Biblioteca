class Book:
    def __init__(self, title=None, isbn=None, publicationYear=None):
        self.__title = title if title is not None else ''
        self.__isbn = isbn if isbn is not None else ''
        self.__publicationYear = publicationYear if publicationYear is not None else ''
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn
    
    @property
    def publicationYear(self):
        return self.__publicationYear
    
    @publicationYear.setter
    def publicationYear(self, publicationYear):
        self.__publicationYear = publicationYear

    def print(self):
        print()
        print(f'''
              
Title: {self.title}
ISBN: {self.isbn}
Publication Year: {self.publicationYear}

''')
    
        
    def fill(self):
        self.title = str(input("Title: "))
        self.isbn = str(input("ISBN: "))
        self.publicationYear = str(input("Publication Year: "))
    