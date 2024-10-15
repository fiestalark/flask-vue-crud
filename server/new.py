from flask import jsonify, request

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    if request.method == 'POST':
        data = request.get_json()
        new_book = Book(
            title=data.get('title'),
            author=data.get('author'),
            read=data.get('read', False)
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': 'Book added!',
            'book': new_book.to_dict()
        }), 201
    else:  # GET request
        books = Book.query.all()
        return jsonify({
            'status': 'success',
            'books': [book.to_dict() for book in books]
        })

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        new_book = Book(
            title=post_data.get('title'),
            author=post_data.get('author'),
            read=post_data.get('read')
        )
        db.session.add(new_book)
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:
        books = Book.query.all()
        response_object['books'] = [book.to_dict() for book in books]
    return jsonify(response_object)