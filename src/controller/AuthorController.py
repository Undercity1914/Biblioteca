from IDAO import IDAO
from Author import Author
from AuthorValidation import AuthorValidation

class AuthorController:
    def __init__(self, repository: IDAO) -> None:
        self.__repository = repository

    @property
    def repository(self) -> IDAO:
        return self.__repository
    
    def add(self, name=None, age=None, cpf=None) -> None:
        validation = AuthorValidation()
        author = validation.validation()

        self.repository.save(author)