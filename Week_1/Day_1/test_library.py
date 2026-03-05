
from library import borrow_book #import the function we will implement

# Scenario 1: Borrow an available book
def test_borrow_available_book():
    available_books = ["Moby Dick", "1984", "Pride and Prejudice"]
    message = borrow_book("Pride and Prejudice", available_books)
    assert message == "You have borrowed 'Pride and Prejudice'."

# Scenario 2: Borrow a book that has already been borrowed and removed from the list
def test_book_removed_after_borrowing():
    available_books = ["Moby Dick", "1984", "Pride and Prejudice"]
    message =borrow_book("Pride and Prejudice", available_books)
    
    assert message == "You have borrowed 'Pride and Prejudice'."

# Scenario 3: Borrow a book that is not available.
def test_borrow_unavailable_book():
    available_books = ["Moby Dick", "1984", "Pride and Prejudice"]
    message = borrow_book("Things Fall Apart", available_books)
    
    assert message == "Sorry, 'Things Fall Apart' is not available."

# Scenario 4: Borrow a book from an empty list of available books.
def test_borrow_from_empty_list():
    available_books = []
    message = borrow_book("Moby Dick", available_books)
    
    assert message == "Sorry, 'Moby Dick' is not available."