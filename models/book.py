class Book:
    def __init__(self, title, author, genre, available):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def book_checked(self, book):
        if self.checked_out == True:
            return True
