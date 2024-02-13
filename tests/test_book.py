from lib.Book import *

"""
book constructs an id, title and author_name
"""

def test_book_constructs():
    book = Book(1, 'test_book', 'test_author')
    assert book.id == 1
    assert book.title == 'test_book'
    assert book.author_name == 'test_author'

"""
we can format books to strings nicely 
"""
def test_books_format_nicely():
    book = Book(1, 'test_book', 'test_author')
    assert str(book) == "Book(1, test_book, test_author)"

"""
compare 2 identical books and have them to be equal
"""

def test_books_are_equal():
    book_1 = Book(1, 'test_book', 'test_author')
    book_2 = Book(1, 'test_book', 'test_author')
    assert book_1 == book_2