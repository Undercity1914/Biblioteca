import sys

sys.path.append("C:\\Users\\marco\\OneDrive\\Documentos\\PadraoMVC_Python\\src\\model\\file")

from IDAO import IDAO
from Author import Author
from AuthorJSONSerializer import AuthorJSONSerializer
from FilePersistence import FilePersistence

class AuthorDAOFile(IDAO):
    def __init__(self, patchFile):
        self.__patchFile = patchFile
        self.__authors = []
        self.__serializer = AuthorJSONSerializer("AuthorList.json")
        self.__filePersistence = FilePersistence()

    @property
    def authors(self):
        return self.__authors
    
    @authors.setter
    def authors(self, authors):
        self.__authors = authors
    
    def save(self, author: Author) -> None:
        authors = self.findAll() if self.findAll() is not None else []
        authors.append(author)
        self.authors = authors

        jsonData = self.__serializer.toFile(authors)
        self.__filePersistence.saveToFile(jsonData, self.__patchFile)
            

    def update(self, code, obj):
        pass

    def remove(self, code):
        author = self.find(code)
        if isinstance(Author, author):
            if author is not None:
                authors = self.findAll()
                authors.remove(author)

                jsonData = self.__serializer.toFile(authors)
                self.__filePersistence.saveToFile(jsonData, self.__patchFile)

    def find(self, code):
        authors = self.findAll()

        for author in self.__authors:
            if author.cpf == code:
                return author
        
        return None


    def findAll(self):
        jsonData = self.__filePersistence.loadFromFile(self.__patchFile)
        return self.__serializer.fromFile(jsonData)
    
    