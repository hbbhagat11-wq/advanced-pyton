

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}


    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

  
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    def issue_book(self, book_id, patron_id):
        if book_id in self.books and patron_id in self.patrons:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.available:
                book.available = False
                patron.borrowed_books.append(book.title)
                print(f"Book '{book.title}' issued to {patron.name}.")
            else:
                print("Book is not available.")
        else:
            print("Invalid Book ID or Patron ID.")


    def return_book(self, book_id, patron_id):
        if book_id in self.books and patron_id in self.patrons:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.title in patron.borrowed_books:
                patron.borrowed_books.remove(book.title)
                book.available = True
                print(f"Book '{book.title}' returned successfully.")
            else:
                print("This patron did not borrow the book.")
        else:
            print("Invalid Book ID or Patron ID")    # Display books
    def display_books(self):
        print("\nLibrary Books")
        for book in self.books.values():
            status = "Available" if book.available else "Issued"
            print(f"{book.book_id} - {book.title} by {book.author} ({status})")


library = Library()


library.add_book(Book(1, "Python Programming", "John Smith"))
library.add_book(Book(2, "Data Structures", "Jane Doe"))

library.register_patron(Patron(101, "Alice"))
library.register_patron(Patron(102, "Bob"))
library.display_books()

library.issue_book(1, 101)
library.display_books()
library.return_book(1, 101)


library.display_books()