### Library Management System ###

"""
Entities (Classes) to Create:

Book Class:

Attributes: title, author, isbn, is_available (boolean).

Methods: borrow(), return_book().

User Class:

Attributes: name, user_id, borrowed_books (list of Book objects).

Methods: borrow_book(book), return_book(book).

Library Class:

Attributes: name, catalog (list of Book objects), registered_users (list of User objects).

Methods: add_book(), register_user(), display_catalog().
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"The book '{self.title}' has been borrowed successfully.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.is_available = True
        print(f"The book '{self.title}' has been returned successfully.")

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"[{self.isbn}] {self.title} by {self.author} ({status})")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Could not lend '{book.title}' to {self.name}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = {}  # Dictionary: {isbn: Book_object}
        self.users = {}    # Dictionary: {user_id: User_object}

    def add_book(self, book):
        self.catalog[book.isbn] = book
        print(f"Book '{book.title}' added to {self.name}'s catalog.")

    def register_user(self, user):
        self.users[user.user_id] = user
        print(f"User '{user.name}' (ID: {user.user_id}) registered successfully.")

    def search_books(self, query):
        """Searches for books matching ISBN, title, or author."""
        query_lower = query.strip().lower()
        results = []

        # 1. Direct search by ISBN
        if query in self.catalog:
            results.append(self.catalog[query])
            return results

        # 2. Search by Title or Author (partial matches allowed)
        for book in self.catalog.values():
            if query_lower in book.title.lower() or query_lower in book.author.lower():
                results.append(book)

        return results

    def display_catalog(self):
        print(f"\n--- {self.name} Catalog ---")
        if not self.catalog:
            print("The catalog is empty.")
            return
        for book in self.catalog.values():
            book.display_info()


# ==========================================
# DATA INITIALIZATION
# ==========================================
my_library = Library("Library of UCR")

# Initial collection
books = [
    Book("1984", "George Orwell", "9780451524935"),
    Book("To Kill a Mockingbird", "Harper Lee", "9780060935467"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"),
    Book("Pride and Prejudice", "Jane Austen", "9780141439518"),
    Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488"),
    Book("The Hobbit", "J.R.R. Tolkien", "9780547928227"),
    Book("Fahrenheit 451", "Ray Bradbury", "9781451673319"),
    Book("Moby-Dick", "Herman Melville", "9781503280786"),
    Book("War and Peace", "Leo Tolstoy", "9780199232765"),
    Book("Crime and Punishment", "Fyodor Dostoevsky", "9780140449136")
]

for b in books:
    my_library.add_book(b)

# Sample user
default_user = User("Mauricio", "U001")
my_library.register_user(default_user)


# ==========================================
# INTERACTIVE MENU SYSTEM
# ==========================================
while True:
    print(f"\n===== {my_library.name.upper()} SYSTEM =====")
    print("1. Display Full Catalog")
    print("2. Search Book (by Title, Author, or ISBN)")
    print("3. Add New Book")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Exit")

    option = input("Select an option (1-6): ").strip()

    if option == "1":
        my_library.display_catalog()

    elif option == "2":
        query = input("Enter Title, Author, or ISBN to search: ")
        matches = my_library.search_books(query)
        if matches:
            print(f"\nFound {len(matches)} result(s):")
            for b in matches:
                b.display_info()
        else:
            print("No books found matching your query.")

    elif option == "3":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        if isbn in my_library.catalog:
            print("Error: A book with this ISBN already exists.")
        else:
            new_book = Book(title, author, isbn)
            my_library.add_book(new_book)

    elif option == "4":
        query = input("Enter Title, Author, or ISBN of the book to borrow: ")
        matches = my_library.search_books(query)

        if not matches:
            print("Book not found in catalog.")
        elif len(matches) == 1:
            selected_book = matches[0]
            default_user.borrow_book(selected_book)
        else:
            print("\nMultiple books found. Please choose one by entering its number:")
            for idx, b in enumerate(matches, 1):
                print(f"{idx}. [{b.isbn}] {b.title} - {b.author}")
            try:
                choice = int(input("Selection number: ")) - 1
                if 0 <= choice < len(matches):
                    default_user.borrow_book(matches[choice])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif option == "5":
        if not default_user.borrowed_books:
            print(f"{default_user.name} has no borrowed books.")
        else:
            print("\nCurrently Borrowed Books:")
            for idx, b in enumerate(default_user.borrowed_books, 1):
                print(f"{idx}. {b.title} [{b.isbn}]")
            try:
                choice = int(input("Select book number to return: ")) - 1
                if 0 <= choice < len(default_user.borrowed_books):
                    selected_book = default_user.borrowed_books[choice]
                    default_user.return_book(selected_book)
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif option == "6":
        print("Exiting System. Goodbye!")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 6.")


"""
Library Management System - Core Module
Author: Mauricio Gutierrez Piedra(MapiiedrA)
Date: 2/9/2026
License: MIT
"""
