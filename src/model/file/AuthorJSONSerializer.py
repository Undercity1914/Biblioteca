import json

from typing import List
from Author import Author

class AuthorJSONSerializer:
    def __init__(self, patchFile=None) -> None:
        self.__patchFile = patchFile if patchFile is not None else ""

    @property
    def patchFile(self):
        return self.__patchFile

    def toFile(self, authors: List[Author]) -> None:
        try: 
            authorsDict = [author.toDict() for author in authors]
            jsonString = json.dumps(authorsDict, indent=4) 
            with open(self.__patchFile, 'w') as f:
                f.write(jsonString)

            return jsonString
        except Exception as e:
            print('''
Erro ao salvar os autores em JSON

ERROR MESSAGE:
    
                
                  ''', 
                  e)

    def fromFile(self, jsonData) -> List[Author]:
        try:
            authorsDict = json.loads(jsonData)
            authors = [Author.fromDict(authorData) for authorData in authorsDict]
            return authors
        except Exception as e:
            print('''
Erro ao encontrar o arquivo

ERROR MESSAGE:
                  
''', e)
            return []
        