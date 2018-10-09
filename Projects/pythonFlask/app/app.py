from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 9780000
    },
    {
        'name': 'The Cat in The Hat',
        'price': 6.99,
        'isbn': 9780001
    }
]


def validBookObj(bookObj):
    if ("name" in bookObj and "price" in bookObj and "isbn" in bookObj):
        return True
    return False



# route w a route decorator
# decorator binds a function to a url
@app.route('/')
def hello_world():
    return "<h1>Hey Buddy!</h1><h2>Welcome to my pyflask docker dev environment!</h2>"

#GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

#POST add_book
@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if validBookObj(request_data):
        new_book = {
            "name": request_data["name"],
            "price": request_data["price"],
            "isbn": request_data["isbn"]
        }
        books.append(new_book)
        response = Response("", 201, mimetype="application/json")
        response.headers["location"] = "/books/" + str(new_book["isbn"])
        return response
    else:
        invalidBookObjErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Required Properties: {'name': 'bookname', 'price': 7.99, 'isbn': 123456789}"
        }
    return Response(json.dumps(invalidBookObjErrorMsg), 400, mimetype="application/json")
    

#GET /books/9780xxxx
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    retval = {}
    for book in books:
        if book["isbn"] == isbn:
            retval = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(retval)



#app.run(port=5000)
app.run(host='0.0.0.0')
