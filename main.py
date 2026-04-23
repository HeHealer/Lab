from library import books,users,transactions,search,analytics,storage
class LibrarySystem:
    def __init__(self):
        self.books=books
        self.users=users
        self.transactions=transactions
        self.search=search
        self.analytics=analytics
        self.storage=storage
    def menu(self):
        self.storage.load()
        while True:
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
            choice=input("Enter choice: ")
            try:
                if choice=="1":
                    title=input("Enter book title: ")
                    author=input("Enter author name: ")
                    can_issue=input("Can this book be issued? (yes/no): ").lower()
                    self.books.add(title,author,can_issue)
                elif choice=="2":
                    self.books.display()
                elif choice=="3":
                    self.users.user()
                elif choice=="4":
                    self.transactions.issue(int(input("Enter book index: ")),input("Enter user ID: "))
                elif choice=="5":
                    self.transactions.return_book(int(input("Enter book index: ")),input("Enter user ID: "))
                elif choice=="6":
                    self.search.search_title(input("Enter title to search: "))
                elif choice=="7":
                    self.search.search_author(input("Enter author to search: "))
                elif choice=="8":
                    self.analytics.analytic()
                elif choice=="9":
                    self.transactions.view_issued()
                elif choice=="10":
                    self.books.show_reference_books()
                elif choice=="11":
                    self.books.update(int(input("Enter book index: ")),input("Enter new title: "),input("Enter new author: "))
                elif choice=="12":
                    self.books.delete(int(input("Enter book index: ")))
                elif choice=="13":
                    print("Exiting system...")
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid input!")
            except Exception as e:
                print("Error:",e)
LibrarySystem().menu()