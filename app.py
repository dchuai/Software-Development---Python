from flask import Flask, request, jsonify

app = Flask(__name__)

# My Sample data for testing
books = [
    {"id": 1, "The Money Class": "Book1", "author": "Suze ORMAN", "publisher": "Group"},
    {"id": 2, "The World is Open": "Book2", "author": "Curtis J. Bonk", "publisher": "Jossey Bass"},
    {"id": 3, "Jump Start Your Growth": "Book3", "author": "John C. Maxwell", "publisher": "John Maxwell"},
    # Add more books as needed
]

# Routes for CRUD operations
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({'book': book})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(new_book)
    return jsonify({'message': 'Book added successfully'})

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        data = request.get_json()
        book.update({
            'book_name': data['book_name'],
            'author': data['author'],
            'publisher': data['publisher']
        })
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
