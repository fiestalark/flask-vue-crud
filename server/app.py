from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Instantiate the app
app = Flask(__name__)

# Config
app.config['ENV'] = 'development'
#app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    read = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'read': self.read
        }
    
with app.app_context():
    db.create_all()

# Enable CORS
# In a production environment, you should only allow cross-origin requests 
# from the domain where the front-end application is hosted.
CORS(app, resources={r'/*': {'origins': '*'}})

def create_response(status, message=None, books=None):
    response = {'status': status}
    if message:
        response['message'] = message
    if books is not None:
        response['books'] = books
    return jsonify(response)

def reset_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database has been reset.")


# Route to get all books
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return create_response('error', 'No data provided'), 400
        
        title = data.get('title')
        author = data.get('author')

        if not title or not author:
            return create_response('error', 'Title and author are required'), 400
        try:  
            new_book = Book(
                title=title,
                author=author,
                read=data.get('read', False)
            )
            db.session.add(new_book)
            db.session.commit()
            return create_response('success', 'Book added!'), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return create_response('error', f"Database error: {str(e)}"), 500
    else:
        try:
            books = Book.query.all()
            return create_response('success', 'Books loaded!', books=[book.to_dict() for book in books] ), 201
        except SQLAlchemyError as e:
            create_response('error', f"Database error: {str(e)}"), 500

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    if request.method == 'PUT':
        data = request.get_json()
        if not data: 
            return create_response('error', 'No data provided'), 400
        try:
            book = db.session.get(Book, book_id)
            if book:
                book.title = data.get('title')
                book.author = data.get('author')
                book.read = data.get('read', book.read)
                db.session.commit()
            return create_response('success', 'Book updated!'), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            create_response('error', f"Database error: {str(e)}"), 500
    if request.method == 'DELETE':
        try:
            remove_book(book_id)
            return create_response('success', 'Book removed!'), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            create_response('error', f"Database error: {str(e)}"), 500


def remove_book(book_id):
    book = db.session.get(Book, book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False

if __name__ == '__main__':
    #reset_database()
    app.run()