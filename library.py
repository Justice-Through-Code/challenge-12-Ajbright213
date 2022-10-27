from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []

    def add_title(self, title, author):
        """Add a Book object with the given title and author to the book list"""
 
        self.books.append(Book(title, author))

    def count_books(self):
        return len(self.books)
        """Return the number of books currently in the booklist"""
        



    def remove_title(self, title):
        count = 0
        for item in self.books:
            if item.title == title:
                self.books.pop(count)
            count += 1

        """Remove a book from the book list"""
        
        

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []


    def display_books(self):
        for book in self.books:
            print(book)