import os

class FilePersistence:
    def __init__(self) -> None:
        pass

    def saveToFile(self, text, patchFile) -> None:
        try:
            with open(patchFile, 'w')as file:
                file.write(text)
        except IOError as e:
            print(e)

    def loadFromFile(self, patchFile) -> None:
        content = ''
        try:
            if os.path.exists(patchFile):
                with open(patchFile, 'r') as file:
                    content = file.read()
                return content

        except IOError as e:
            print(e)