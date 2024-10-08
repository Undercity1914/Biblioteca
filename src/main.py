import sys

sys.path.append("C:\\Users\\marco\\OneDrive\\Documentos\\PadraoMVC_Python\\src\\model\\DAO")
sys.path.append("C:\\Users\\marco\\OneDrive\\Documentos\\PadraoMVC_Python\\src\\model\\entities")

from AuthorDAOFile import AuthorDAOFile
from Author import Author

archive = AuthorDAOFile("AuthorList.json")

print(archive.findAll())

author = Author()

authors = archive.findAll()

for author in authors:
    author.print()