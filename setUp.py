from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
# if starting a new terminal alway enter in theses commands
#   export FLASK_APP=(name of python file)
#   export FLASK_ENV=development
#   flask run


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    publisher = db.Column(db.String(80), unique=False, nullable=False)
    
    def __repr__(self):
        return f"{self.book_name}, made by {self.author} and {self.publisher}"



#making a route 
@app.route('/')
def index():
    return "hello"

@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in books:
        book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}
        output.append(book_data)
    return {"Books": output}