import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Over The Mountain", "Jill Goldstein", "Non-Fiction", True)

    def test_book_checked(self):
        self.assertEqual(True, self.book.book_checked(self.book.title))
