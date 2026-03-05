

# # 1. Handle borrowing an available book from the library
# def borrow_book(book_title, available_books):
#     return "You have borrowed 'Pride and Prejudice'."

# # 2. Handle removing borrowed book from the list
# def borrow_book(book_title, available_books):
#     if book_title == "Pride and Prejudice":
#         available_books.remove(book_title)
#         return f"You have borrowed '{book_title}'."
    
# 3. Handle borrowing a book that is available, removing a book from the list and handling empty list
def borrow_book(book_title, available_books):
    if book_title in available_books:
        available_books.remove(book_title)
        return f"You have borrowed '{book_title}'."
    else:
        return f"Sorry, '{book_title}' is not available."
    
