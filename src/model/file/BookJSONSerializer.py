from Book import Book
from typing import List
import json

class BookJSONSerializer:
    def __init__(self, patchFile=None) -> None:
        self.__patchFile = patchFile if patchFile is not None else ""

    @property
    def patchFile(self):
        return self.__patchFile

    def toFile(self, books: List[Book]) -> None:
        try: 
            booksDict = [book.toDict() for book in books]
            jsonString = json.dumps(booksDict, indent=4) 
            with open(self.__patchFile, 'w') as f:
                f.write(jsonString)

            return jsonString
        except Exception as e:
            print('''
Erro ao salvar os autores em JSON

ERROR MESSAGE:
    
                
                  ''', 
                  e)

    def fromFile(self, jsonData) -> List[Book]:
        try:
            booksDict = json.loads(jsonData)
            books = [Book.fromDict(bookData) for bookData in booksDict]
            return books
        except Exception as e:
            print('''
Erro ao encontrar o arquivo

ERROR MESSAGE:
                  
''', e)
            return []
        