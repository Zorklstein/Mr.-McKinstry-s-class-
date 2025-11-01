from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))

    def __repr__(self):
        return F'{self.name} - {self.description}'
   
@app.route('/')
def index():
    return 'Hello'

@app.route("/books")
def getBooks():
    books = Book.query,all()
    output = []
    for book in books:
        bookData = {'title': book.title, 'author': book.author}
        output.append(bookData)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"title": book.name, 'author': book.author}


@app.route('books', methods = ['POST'])
def add_book():
    book = book(title = request.json['title'], author = request.json['author'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods = ['DELETE'])
def deleteBook():
    book = Book.query.get(id)
    db.session.delete(book)