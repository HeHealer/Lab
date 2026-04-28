from library import books, users, transactions

class Storage:

    def __init__(self):
        # shared references (IMPORTANT: same memory across system)
        self.books = books.book_list
        self.users = users.user_list
        self.transactions = transactions.issued_books

    def save(self):
        try:
            # save books
            with open("books.txt", "w") as f:
                for b in self.books:
                    f.write(str(b) + "\n")

            # save users
            with open("users.txt", "w") as f:
                for u in self.users:
                    f.write(str(u) + "\n")

            # save transactions
            with open("issued.txt", "w") as f:
                for k, v in self.transactions.items():
                    f.write(f"{k}|{v}\n")

        except Exception as e:
            print("Save error:", e)

    def load(self):
        try:
            # clear existing data safely
            self.books.clear()
            self.users.clear()
            self.transactions.clear()

            # load books
            try:
                with open("books.txt", "r") as f:
                    for line in f:
                        self.books.append(eval(line.strip()))
            except FileNotFoundError:
                pass

            # load users
            try:
                with open("users.txt", "r") as f:
                    for line in f:
                        self.users.append(eval(line.strip()))
            except FileNotFoundError:
                pass

            # load transactions
            try:
                with open("issued.txt", "r") as f:
                    for line in f:
                        key, value = line.strip().split("|")
                        self.transactions[int(key)] = value
            except FileNotFoundError:
                pass

            print("Data loaded successfully!")

        except Exception as e:
            print("Load error:", e)