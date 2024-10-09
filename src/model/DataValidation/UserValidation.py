from User import User
from UserException import UserException

class UserValidation:
    def validation(self, name=None, age=None, cpf=None):
        user = User()

        if name is None:
            raise UserException("O nome nao pode ser nulo")
        user.name = name

        if age is None:
            raise UserException("A idade nao pode ser nula")
        user.age = age

        if cpf is None:
            raise UserException("O CPF nao pode ser nulo")
        user.cpf = cpf

        return user