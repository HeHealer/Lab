from library import books

# Class for searching books in the library
class LibrarySearch:

    # Constructor: gets reference to the shared book list
    def __init__(self):
        self.book_list = books.book_list

    # Search books by title (partial match allowed)
    def search_title(self, name):
        found = False

        # Loop through all books
        for b in self.book_list:
            # Case-insensitive match
            if name.lower() in b["title"].lower():
                print(b)
                found = True

        # If no match found
        if not found:
            print("No book found with that title")

    # Search books by author (partial match allowed)
    def search_author(self, name):
        found = False

        # Loop through all books
        for b in self.book_list:
            # Case-insensitive match
            if name.lower() in b["author"].lower():
                print(b)
                found = True

        # If no match found
        if not found:
            print("No book found with that author")

    # Show all available (not issued) books
    def search_available(self):
        available = books.get_available()  # Get available books

        if not available:
            print("No available books")
            return

        # Print each available book
        for b in available:
            print(b)