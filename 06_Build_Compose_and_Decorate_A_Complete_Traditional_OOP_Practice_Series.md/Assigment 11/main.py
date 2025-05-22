class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Whenever a new Book instance is created, increment the class counter
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        """Class method to increment the total_books counter."""
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        """Optional helper to retrieve the current total."""
        return cls.total_books

    def __repr__(self):
        return f"<Book title={self.title!r} author={self.author!r}>"

# Example usage:
if __name__ == "__main__":
    print(Book.get_total_books())  # → 0

    b1 = Book("1984", "George Orwell")
    print(Book.get_total_books())  # → 1

    b2 = Book("To Kill a Mockingbird", "Harper Lee")
    b3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print(Book.get_total_books())  # → 3
