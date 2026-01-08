'''
AGGREGATION = "Has-a" relationship
One object (whole) contains other objects (parts)
Parts can exist independently of the whole
'''
# WHOLE OBJECT (contains parts)
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List of Book objects
        
    def add_book(self, book):  # Adds existing Book objects
        self.books.append(book)
        
    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

# PART OBJECTS (independent)
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

# CREATE PARTS FIRST (can exist alone)
book1 = Book("Chethan Bhagat", "Five point someone")
book2 = Book("Mahabharatam", "Vinayaka")
book3 = Book("Any", "No title")

# CREATE WHOLE (Library)
library = Library("Tenali Open Library")

# ADD PARTS TO WHOLE (aggregation)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Even if library closes, books still exist!
print(f"Library: {library.name}")
library.show_books()

# PROOF: Books exist independently
print(f"\nBook1 still exists: {book1.title}")
# Even without library: book2.title still works