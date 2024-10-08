import json
from typing import List
from User import User

class UserJSONSerializer:
    def __init__(self, patchFile=None) -> None:
        self.__patchFile = patchFile if patchFile is not None else ""

    @property
    def patchFile(self):
        return self.__patchFile

    def toFile(self, users: List[User]) -> None:
        try: 
            usersDict = [author.toDict() for author in users]
            jsonString = json.dumps(usersDict, indent=4) 
            with open(self.__patchFile, 'w') as f:
                f.write(jsonString)

            return jsonString
        except Exception as e:
            print('''
Erro ao salvar os usuarios em JSON

ERROR MESSAGE:
    
                
                  ''', 
                  e)

    def fromFile(self, jsonData) -> List[User]:
        try:
            usersDict = json.loads(jsonData)
            users = [User.fromDict(authorData) for authorData in usersDict]
            return users
        except Exception as e:
            print('''
Erro ao encontrar o arquivo

ERROR MESSAGE:
                  
''', e)
            return []
        