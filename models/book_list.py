from models.book import Book

book1 = Book(
    "We Have Always Lived in the Castle", "Shirley Jackson", "Fiction, Thriller", False
)
book2 = Book("All My Friends are Superheroes", "Andrew Kaufman", "Fiction", True)
book3 = Book("Conspiracies", "Andy Thomas", "Non-Fiction", False)

books = [book1, book2, book3]


def add_book_to_library(add_new_book):
    books.append(add_new_book)


def remove_book_from_list(book_index):
    del books[book_index]
