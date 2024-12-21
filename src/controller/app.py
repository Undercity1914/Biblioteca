import sys
from flask import Flask, jsonify, request
sys.path.append("C:\\Users\\marco\\OneDrive\\Documentos\\PadraoMVC_Python\\src\\connection")
from SQLConnector import SQLConnector

connection = SQLConnector("dataBase.db")

app = Flask(__name__)

@app.route("/authors", methods=['GET'])
def getAuthors():
    cursor = connection.connection.cursor()

    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()

    authorsList = []

    for row in authors:
        author = {
            'ID': row[0],
            'name': row[1],
            'age': row[2],
            'cpf': row[3],
            'bookList': row[4]
        }
        authorsList.append(author)

    return jsonify(authorsList)

@app.route("/search", methods=['GET'])
def search():
    book_name = request.args.get('book', '')
    author_name = request.args.get('author', '')

    cursor = connection.connection.cursor()

    query = """
    SELECT a.ID, a.name, a.age, a.cpf, a.bookList
    FROM author a
    JOIN book b ON a.ID = b.author_id
    WHERE b.name LIKE ? AND a.name LIKE ?
    """
    params = (f"%{book_name}%", f"%{author_name}%")
    cursor.execute(query, params)
    
    results = cursor.fetchall()

    authorsList = []

    for row in results:
        author = {
            'ID': row[0],
            'name': row[1],
            'age': row[2],
            'cpf': row[3],
            'bookList': row[4]
        }
        authorsList.append(author)

    return jsonify(authorsList)

app.run(port=8000, host='localhost', debug=True)
