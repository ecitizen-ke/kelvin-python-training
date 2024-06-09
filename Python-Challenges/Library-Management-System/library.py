from book import Book


class Library:
    def __init__(self):
        """
        Initializes a Library object with an empty list of books.
        """
        self.books = []

    def add_book(self, title, author, num_copies):
        """
        Adds a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            num_copies (int): The number of copies of the book to add.
        """
        self.books.append(Book(title, author, num_copies))
        print("Book added successfully")

    def display_books(self):
        """
        Displays all books in the library.
        """
        print("Library Books:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def search_book(self, title):
        """
        Searches for a book in the library by title.

        Args:
            title (str): The title of the book to search for.
        """
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book}")
                found = True
                break
        if not found:
            print("Book not found")

    def check_out_copy(self, title):
        """
        Checks out a copy of a book from the library.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                book.check_out_copy()
                return
        print("Book not found")

    def return_copy(self, title):
        """
        Returns a copy of a book to the library.

        Args:
            title (str): The title of the book to return.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_copy()
                return
        print("Book not found")

    def display_checked_out_copies(self):
        """
        Displays all copies of books that are currently checked out.
        """
        checked_out_books = [
            book for book in self.books if book.checked_out_copies > 0]
        if checked_out_books:
            print("Checked Out Copies:")
            for book in checked_out_books:
                print(book)
        else:
            print("No copies are currently checked out.")
