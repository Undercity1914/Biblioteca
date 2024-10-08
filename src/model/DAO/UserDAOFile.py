from UserJSONSerializer import UserJSONSerializer
from FilePersistence import FilePersistence
from User import User
from typing import List

class UserDAOFile:
    def __init__(self, patchFile):
        self.__patchFile = patchFile
        self.__users = []
        self.__serializer = UserJSONSerializer("UserList.json")
        self.__filePersistence = FilePersistence()

    @property
    def users(self) -> List[User]:
        return self.__users
    
    @users.setter
    def users(self, users) -> None:
        self.__users = users
    
    def save(self, user: User) -> None:
        users = self.findAll() if self.findAll() is not None else []
        users.append(user)
        self.users = users

        jsonData = self.__serializer.toFile(users)
        self.__filePersistence.saveToFile(jsonData, self.__patchFile)
            

    def update(self, code, obj) -> None:
        pass

    def remove(self, code) -> None:
        user = self.find(code)
        if isinstance(User, user):
            if user is not None:
                users = self.findAll()
                users.remove(user)

                jsonData = self.__serializer.toFile(users)
                self.__filePersistence.saveToFile(jsonData, self.__patchFile)

    def find(self, code) -> User:
        users = self.findAll()

        for user in self.__users:
            if user.cpf == code:
                return user
        
        return None


    def findAll(self):
        jsonData = self.__filePersistence.loadFromFile(self.__patchFile)
        return self.__serializer.fromFile(jsonData)
    
    