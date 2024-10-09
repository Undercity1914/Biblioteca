from Author import Author
from AuthorException import AuthorException

class AuthorValidation:
    def validation(self, name=None, age=None, cpf=None):
        author = Author()

        if name is None:
            raise AuthorException("Nome nao pode ser vazio")
        
        author.name = name

        if age is None:
            raise AuthorException("Idade nao pode ser vazia")
        
        author.age = age
        
        if cpf is None:
            raise AuthorException("CPF nao pode estar vazia")
        
        author.cpf = cpf

        return author