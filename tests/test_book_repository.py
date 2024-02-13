from lib.BookRepository import *
from lib.Book import *

def test_all(db_connection):
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new AlbRepository
    result = repository.all()
    assert result == [  Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
                        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
                        Book(3, 'Emma', 'Jane Austen'),
                        Book(4, 'Dracula', 'Bram Stoker'),
                        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
