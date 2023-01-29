from flask import render_template, request  # ADDED
from app import app
from models.book import Book
from models.book_list import books, add_book_to_library, remove_book_from_list


@app.route("/")
def index():
    return render_template("index.html", books=books)


@app.route("/single_book/<int:index>")
def single_book(index):
    return render_template("single_book.html", books=books[index])


@app.route("/", methods=["POST"])
def add_book():
    new_book_title = request.form["title"]
    new_book_author = request.form["author"]
    new_book_genre = request.form["genre"]
    new_book_available = (
        True
        if request.form["available"] == "checked" in request.form["available"]
        else False
    )
    add_new_book = Book(
        new_book_title, new_book_author, new_book_genre, new_book_available
    )
    add_book_to_library(add_new_book)
    return render_template("index.html", books=books)


@app.route("/delete/<int:index>", methods=["POST"])
def delete_book_from_list(index):
    remove_book_from_list(index)
    return render_template("index.html", books=books)
