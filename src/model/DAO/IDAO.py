from abc import ABC, abstractmethod

class IDAO(ABC):
    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def update(self, code, obj):
        pass
    
    @abstractmethod
    def remove(self, code):
        pass

    @abstractmethod
    def find(self, code):
        pass

    @abstractmethod
    def findAll(self):
        pass