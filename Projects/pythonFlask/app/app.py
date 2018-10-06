from flask import Flask, jsonify

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

# route w a route decorator
# decorator binds a function to a url
@app.route('/')
def hello_world():
    return "Hey Buddy!"

#GET /store
@app.route('/books')
def get_books():
    return jsonify({'books': books})

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