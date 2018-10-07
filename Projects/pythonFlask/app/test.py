def validBookObj(bookObj):
    if ("name" in bookObj and "price" in bookObj and "isbn" in bookObj):
        return True
    return False

validObj = {
  "name": "F",
  "price": 1.99,
  "isbn": 2039485
}

noName = {
  "price": 1.99,
  "isbn": 2039485
}
noPrice = {
  "name": "F",
  "isbn": 2039485
}
noIsbn = {
  "name": "F",
  "price": 1.99,
}
noNothing = {}