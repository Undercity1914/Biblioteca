class Person:
    def __init__(self=None, name=None, age=None, cpf=None):
        self._name = name if name is not None else ""
        self._age = age if age is not None else ""
        self._cpf = cpf if cpf is not None else ""
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def print(self):
        print()
        print(f'''
Name: {self.name}"
Age: {self.age}
CPF: {self.cpf}
''')
        
    def fill(self):
        self.name = str(input("Name: "))
        self.age = str(input("Age: "))
        self.cpf = str(input("CPF: "))