
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Hello, World!</h2>"

@app.route('/greeting/<name>')
def greet(name):
    return '<h1> Hello, %s! </h1>'%name
@app.route('/counter/<n>')
def counter(n):
    if int(n) ==1:
        return '<h1> Counter  on%d!</h1>'%int(n)
    if int(n) ==2:
        return '<h1> Counter  two%d!</h1>'%int(n)
    if int(n) ==3:
        return '<h1> Counter  three%d!</h1>'%int(n)
    if int(n) ==4:
        return '<h1> Counter  four%d!</h1>'%int(n)
    if int(n) ==5:
        return '<h1> Counter  five%d!</h1>'%int(n)
    else:
        return '<h1> out of range</h1>'


if __name__ == '__main__':
    app.run(debug=True)