from flask import Flask, request, jsonify
app = Flask(__name__)
books = [
    {"id": 1, "title": "Python Basics", "author": "John"},
    {"id": 2, "title": "Web Development", "author": "Smith"}
]
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "Title and author are required"}), 400
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201
if __name__ == "__main__":
    app.run(debug=True)