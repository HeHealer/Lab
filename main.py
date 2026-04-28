from library import books, users, transactions, search, analytics, storage

class LibrarySystem:

    def __init__(self):
        self.books = books.Library()
        self.users = users.UserManager()
        self.transactions = transactions.Transactions()
        self.search = search.LibrarySearch()
        self.analytics = analytics.LibraryAnalytics()
        self.storage = storage.Storage()
        self.books.storage = self.storage
        self.users.storage = self.storage
        self.transactions.storage = self.storage

    def menu(self):
        self.storage.load()

        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1 Add Book")
            print("2 View Books")
            print("3 User Menu")
            print("4 Issue Book")
            print("5 Return Book")
            print("6 Search by Title")
            print("7 Search by Author")
            print("8 View Analytics")
            print("9 View Issued Books")
            print("10 Reference Books")
            print("11 Update Book")
            print("12 Delete Book")
            print("13 Exit")

            choice = input("Enter choice: ")

            try:
                if choice == "1":
                    self.books.add(
                        input("Title: "),
                        input("Author: "),
                        input("Can issue (yes/no): ")
                    )
                    self.storage.save()   # ✅ FIX

                elif choice == "2":
                    self.books.display()

                elif choice == "3":
                    self.users.menu()

                elif choice == "4":
                    self.transactions.issue(
                        int(input("Book index: ")),
                        input("User ID: ")
                    )
                    self.storage.save()   # ✅ FIX

                elif choice == "5":
                    self.transactions.return_book(
                        int(input("Book index: ")),
                        input("User ID: ")
                    )
                    self.storage.save()   # ✅ FIX

                elif choice == "6":
                    self.search.search_title(input("Title: "))

                elif choice == "7":
                    self.search.search_author(input("Author: "))

                elif choice == "8":
                    self.analytics.analytic()

                elif choice == "9":
                    self.transactions.view_issued()

                elif choice == "10":
                    self.books.show_reference_books()

                elif choice == "11":
                    self.books.update(
                        int(input("Index: ")),
                        input("New title: "),
                        input("New author: ")
                    )
                    self.storage.save()   # ✅ FIX

                elif choice == "12":
                    self.books.delete(int(input("Index: ")))
                    self.storage.save()   # ✅ FIX

                elif choice == "13":
                    print("Exiting...")
                    break

                else:
                    print("Invalid choice!")

            except ValueError:
                print("Invalid input!")

            except Exception as e:
                print("Error:", e)


LibrarySystem().menu()
