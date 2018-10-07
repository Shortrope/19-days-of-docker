from flask import Flask, jsonify, request

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
    return "Hey Buddy!"

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
        return "True"
    return "False"
    

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