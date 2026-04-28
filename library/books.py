book_list = []

from library import storage
import pandas as pd

class Library:

    def __init__(self):
        global book_list
        self.book_list = book_list

    # Returns total number of books
    def __len__(self):
        return len(self.book_list)

    # String representation of object
    def __str__(self):
        return f"Total books: {len(self.book_list)}"

    # Add a new book to the list
    def add(self, title, author, can_issue):
        self.book_list.append({
            "title": title,
            "author": author,
            "issued": False,                 # Book is not issued initially
            "can_issue": can_issue == "yes"  # Convert input to boolean
        })
        self.storage.save()  # Save data after adding
        print("Book added and saved!")

    # Display books with different options
    def display(self):
        if not self.book_list:
            print("No books available")
            return

        print("\n===== VIEW BOOKS =====")
        print("1 Show all books")
        print("2 Total count")
        print("3 Sort by title")
        print("4 Sort by author")

        choice = input("Enter choice: ")

        # Show all books
        if choice == "1":
            df = pd.DataFrame(self.book_list)
            df.index.name = "ID"
            print(df)

        # Show total count
        elif choice == "2":
            print("Total books:", len(self.book_list))

        # Sort by title and display
        elif choice == "3":
            self.sort_by_title()
            df = pd.DataFrame(self.book_list)
            df.index.name = "ID"
            print(df)

        # Sort by author and display
        elif choice == "4":
            self.sort_by_author()
            df = pd.DataFrame(self.book_list)
            df.index.name = "ID"
            print(df)

        else:
            print("Invalid choice!")

    # Delete a book by index
    def delete(self, index):
        try:
            self.book_list.pop(index)
            self.storage.save()  # Save after deletion
            print("Book deleted")
        except:
            print("Invalid index")

    # Update book details
    def update(self, index, title, author):
        try:
            self.book_list[index]["title"] = title
            self.book_list[index]["author"] = author
            self.storage.save()  # Save after update
            print("Book updated")
        except:
            print("Invalid index")

    # Get all available (not issued) books
    def get_available(self):
        return [b for b in self.book_list if not b["issued"]]

    # Mark a book as issued
    def mark_issued(self, index):
        try:
            # Check if book can be issued
            if not self.book_list[index]["can_issue"]:
                print("Reference book cannot be issued")
                return
            self.book_list[index]["issued"] = True
            self.storage.save()
        except:
            print("Invalid index")

    # Mark a book as returned
    def mark_returned(self, index):
        try:
            self.book_list[index]["issued"] = False
            self.storage.save()
        except:
            print("Invalid index")

    # Show all issued books
    def show_issued(self):
        if not self.book_list:
            print("No issued books")
            return

        # Filter issued books
        rows = [b for b in self.book_list if b["issued"]]

        if not rows:
            print("No issued books")
            return

        df = pd.DataFrame(rows)
        print(df)

    # Show books that cannot be issued (reference books)
    def show_reference_books(self):
        rows = [b for b in self.book_list if not b["can_issue"]]

        if not rows:
            print("No reference books available")
            return

        df = pd.DataFrame(rows)
        df.index.name = "ID"
        print(df)

    # Sort books by title (manual sorting)
    def sort_by_title(self):
        for i in range(len(self.book_list)):
            for j in range(i + 1, len(self.book_list)):
                if self.book_list[i]["title"] > self.book_list[j]["title"]:
                    # Swap books
                    self.book_list[i], self.book_list[j] = self.book_list[j], self.book_list[i]

    # Sort books by author (manual sorting)
    def sort_by_author(self):
        for i in range(len(self.book_list)):
            for j in range(i + 1, len(self.book_list)):
                if self.book_list[i]["author"] > self.book_list[j]["author"]:
                    # Swap books
                    self.book_list[i], self.book_list[j] = self.book_list[j], self.book_list[i]