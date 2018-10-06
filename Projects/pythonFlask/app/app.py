from flask import Flask

app = Flask(__name__)
print (__name__)

# route w a route decorator
# decorator binds a function to a url
@app.route('/')
def hello_world():
    return "Hey Buddy!"

#app.run(port=5000)
app.run(host='0.0.0.0')