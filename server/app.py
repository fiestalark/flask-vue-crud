from flask import Flask, jsonify
from flask_cors import CORS

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
# In a production environment, you should only allow cross-origin requests 
# from the domain where the front-end application is hosted.
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# Sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# Route to get all books
@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })

if __name__ == '__main__':
    app.run()