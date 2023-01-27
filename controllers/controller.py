from flask import render_template, request  # ADDED
from app import app
from models.book import Book
from models.book_list import books


@app.route("/")
def index():
    return render_template("index.html", books=books)


@app.route("/single_book/<int:index>")
def single_book(index):
    return render_template("single_book.html", books=books[index])
