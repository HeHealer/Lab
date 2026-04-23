from library import books, users, transactions, search, analytics, storage

# Main class for Library Management System
class LibrarySystem:
    
    # Constructor: initializes all modules
    def __init__(self):
        self.books = books              # Handles book-related operations
        self.users = users              # Handles user-related operations
        self.transactions = transactions# Handles issuing/returning books
        self.search = search            # Handles search functionality
        self.analytics = analytics      # Handles analytics/reporting
        self.storage = storage          # Handles data load/save

    # Menu-driven interface
    def menu(self):
        self.storage.load()  # Load stored data at the start

        while True:
            # Display menu options
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1 Add Book")
            print("2 View Books")
            print("3 User")
            print("4 Issue Book")
            print("5 Return Book")
            print("6 Search Book by Title")
            print("7 Search Book by Author")
            print("8 View Analytics")
            print("9 View Issued Books")
            print("10 View Reference Books")
            print("11 Update Book")
            print("12 Delete Book")
            print("13 Exit")

            choice = input("Enter choice: ")

            try:
                # Add a new book
                if choice == "1":
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    can_issue = input("Can this book be issued? (yes/no): ").lower()
                    self.books.add(title, author, can_issue)

                # Display all books
                elif choice == "2":
                    self.books.display()

                # User-related operations
                elif choice == "3":
                    self.users.user()

                # Issue a book to a user
                elif choice == "4":
                    self.transactions.issue(
                        int(input("Enter book index: ")),
                        input("Enter user ID: ")
                    )

                # Return a book
                elif choice == "5":
                    self.transactions.return_book(
                        int(input("Enter book index: ")),
                        input("Enter user ID: ")
                    )

                # Search book by title
                elif choice == "6":
                    self.search.search_title(
                        input("Enter title to search: ")
                    )

                # Search book by author
                elif choice == "7":
                    self.search.search_author(
                        input("Enter author to search: ")
                    )

                # View analytics/report
                elif choice == "8":
                    self.analytics.analytic()

                # View issued books
                elif choice == "9":
                    self.transactions.view_issued()

                # Show reference (non-issuable) books
                elif choice == "10":
                    self.books.show_reference_books()

                # Update book details
                elif choice == "11":
                    self.books.update(
                        int(input("Enter book index: ")),
                        input("Enter new title: "),
                        input("Enter new author: ")
                    )

                # Delete a book
                elif choice == "12":
                    self.books.delete(
                        int(input("Enter book index: "))
                    )

                # Exit the system
                elif choice == "13":
                    print("Exiting system...")
                    break

                # Handle invalid menu choice
                else:
                    print("Invalid choice!")

            # Handle invalid integer input
            except ValueError:
                print("Invalid input!")

            # Catch any other unexpected errors
            except Exception as e:
                print("Error:", e)


# Create object and start the system
LibrarySystem().menu()