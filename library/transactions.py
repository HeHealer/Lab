issued_books = {}
from library import books, storage
import time

# Class to manage issuing and returning of books
class Transactions:

    # Constructor: initializes issued books and issue count tracking
    def __init__(self):
        self.issued_books = {}   # {book_index: {user_id: {issue_date}}}
        self.issue_count = {}    # {book_index: {user_id: count}}

    # Convert date string (YYYY-MM-DD) into seconds
    def str_to_seconds(self, date_str):
        y, m, d = map(int, date_str.split("-"))
        return time.mktime((y, m, d, 0, 0, 0, 0, 0, 0))

    # Issue a book to a user
    def issue(self, index, user_id):

        # Check if index is valid
        if index >= len(books.book_list):
            print("Invalid book index")
            return

        # Check if book can be issued
        if not books.book_list[index]["can_issue"]:
            print("Reference book cannot be issued")
            return

        # Check if already issued
        if books.book_list[index]["issued"]:
            print("Book already issued")
            return

        # Initialize issue count tracking
        if index not in self.issue_count:
            self.issue_count[index] = {}

        if user_id not in self.issue_count[index]:
            self.issue_count[index][user_id] = 0

        # Limit: user can issue same book only 2 times
        if self.issue_count[index][user_id] >= 2:
            print("User can issue this book only 2 times")
            return

        # Initialize issued_books structure
        if index not in self.issued_books:
            self.issued_books[index] = {}

        # Check if user already has this book
        if user_id in self.issued_books[index]:
            print("User already has this book issued")
            return

        # Take issue date input
        issue_date = input("Enter issue date (YYYY-MM-DD): ")

        # Validate date format
        try:
            self.str_to_seconds(issue_date)
        except:
            print("Invalid date format")
            return

        # Store issue record
        self.issued_books[index][user_id] = {"issue_date": issue_date}

        # Increase issue count
        self.issue_count[index][user_id] += 1

        # Mark book as issued
        books.mark_issued(index)

        # Save data
        storage.save()

        print("Book issued successfully!")

    # Return a book
    def return_book(self, index, user_id):

        # Check if book is actually issued to the user
        if index not in self.issued_books or user_id not in self.issued_books[index]:
            print("Book not issued by this user")
            return

        # Take return date input
        return_date = input("Enter return date (YYYY-MM-DD): ")

        try:
            # Convert dates to seconds
            i_sec = self.str_to_seconds(self.issued_books[index][user_id]["issue_date"])
            r_sec = self.str_to_seconds(return_date)
        except:
            print("Invalid date format")
            return

        # Calculate number of days
        days = int((r_sec - i_sec) / (60 * 60 * 24))

        # Check invalid date logic
        if days < 0:
            print("Return date cannot be before issue date")
            return

        # Fine calculation (after 20 days)
        if days > 20:
            print("Late return! Fine =", (days - 20) * 2, "Rs")
        else:
            print("Returned on time")

        # Remove record after return
        del self.issued_books[index][user_id]

        # Clean up empty entries
        if not self.issued_books[index]:
            del self.issued_books[index]

        # Mark book as returned
        books.mark_returned(index)

        # Save updated data
        storage.save()

        print("Book returned successfully!")

    # View all issued books
    def view_issued(self):

        # Check if any books are issued
        if not self.issued_books:
            print("No issued books")
            return

        # Display issued book details
        for b, data in self.issued_books.items():
            for user, info in data.items():
                print("Book:", b, "User:", user, "Issue Date:", info["issue_date"])