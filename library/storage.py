from library import books, users, transactions

# Class responsible for saving and loading data from files
class Storage:

    # Constructor: connects storage to existing data structures
    def __init__(self):
        self.books = books.book_list              # List of books
        self.users = users.user_list              # List of users
        self.transactions = transactions.issued_books  # Issued books data

    # String representation showing stored data counts
    def __str__(self):
        return f"Storage(books={len(self.books)},users={len(self.users)})"

    # Save all data to text files
    def save(self):
        try:
            # Save books data
            with open("books.txt", "w") as f:
                for b in self.books:
                    f.write(
                        b["title"] + "," +
                        b["author"] + "," +
                        str(b["issued"]) + "," +
                        str(b.get("can_issue", True)) + "\n"
                    )

            # Save users data
            with open("users.txt", "w") as f:
                for u in self.users:
                    f.write(u["name"] + "," + u["id"] + "\n")

            # Save issued books (transactions)
            with open("issued.txt", "w") as f:
                for book_index, data in self.transactions.items():
                    f.write(str(book_index) + "|" + str(data) + "\n")

        except:
            print("Error while saving data")

    # Load all data from text files
    def load(self):
        try:
            # Clear existing data before loading
            self.books.clear()
            self.users.clear()
            self.transactions.clear()

            # Load books data
            with open("books.txt", "r") as f:
                for line in f:
                    try:
                        title, author, issued, can_issue = line.strip().split(",")
                        self.books.append({
                            "title": title,
                            "author": author,
                            "issued": issued == "True",        # Convert to boolean
                            "can_issue": can_issue == "True"   # Convert to boolean
                        })
                    except:
                        continue  # Skip invalid lines

            # Load users data
            with open("users.txt", "r") as f:
                for line in f:
                    try:
                        name, user_id = line.strip().split(",")
                        self.users.append({
                            "name": name,
                            "id": user_id
                        })
                    except:
                        continue  # Skip invalid lines

            # Load issued books (transactions)
            with open("issued.txt", "r") as f:
                for line in f:
                    try:
                        key, value = line.strip().split("|")
                        self.transactions[int(key)] = eval(value)  # Convert string to object
                    except:
                        continue  # Skip invalid lines

            print("Data loaded successfully!")

        # If files do not exist
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")