import pandas as pd
import numpy as np
from library import books

# Class for handling analytics of the library system
class LibraryAnalytics:

    # Constructor: gets the data source (book list)
    def __init__(self):
        self.data_source = books.book_list  # List of books

    # Convert data source into a pandas DataFrame
    def df(self):
        return pd.DataFrame(self.data_source)

    # Returns total number of books (len(object) support)
    def __len__(self):
        return len(self.data_source)

    # String representation of the object
    def __str__(self):
        d = self.df()
        if d.empty:
            return "No data"
        # Shows total books and number of unique authors
        return f"Total books: {len(d)}, Authors: {len(set(d['author']))}"

    # Prints summary of data
    def summary(self):
        d = self.df()
        if d.empty:
            print("No data")
            return
        print("Total:", len(d))  # Total number of books
        print("Authors:", len(set(d["author"])))  # Unique authors

    # Displays a random book from the dataset
    def random_book(self):
        d = self.df()
        if len(d) == 0:
            print("No books")
            return
        i = np.random.randint(0, len(d))  # Random index
        print(d.iloc[i])  # Print random row

    # Shows number of books per author
    def books_per_author(self):
        d = self.df()
        if d.empty:
            print("No data")
            return
        counts = d["author"].value_counts()  # Count books per author
        print("\nBooks per Author:")
        print(counts)

    # Reads and displays data from file
    def show_file_data(self):
        try:
            # Read file assuming comma-separated values
            d = pd.read_csv("books.txt", names=["title", "author", "issued"])
            print(d)
        except:
            print("File not found")

    # Menu for analytics options
    def menu(self):
        while True:
            print("\n===== ANALYTICS MENU =====")
            print("1 Summary")
            print("2 Random Book")
            print("3 Books per Author")
            c = input("Enter choice: ")
            if c == "1":
                self.summary()  # Show summary
            elif c == "2":
                self.random_book()  # Show random book
            elif c == "3":
                self.books_per_author()  # Show author-wise count
            else:
                print("Invalid choice!")