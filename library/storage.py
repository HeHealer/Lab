from library import books,users,transactions
class Storage:
    def __init__(self):
        self.books=books.book_list
        self.users=users.user_list
        self.transactions=transactions.issued_books
    def __str__(self):
        return f"Storage(books={len(self.books)},users={len(self.users)})"
    def save(self):
        try:
            with open("books.txt","w") as f:
                for b in self.books:
                    f.write(b["title"]+","+b["author"]+","+str(b["issued"])+","+str(b.get("can_issue",True))+"\n")
            with open("users.txt","w") as f:
                for u in self.users:
                    f.write(u["name"]+","+u["id"]+"\n")
            with open("issued.txt","w") as f:
                for book_index,data in self.transactions.items():
                    f.write(str(book_index)+"|"+str(data)+"\n")
        except:
            print("Error while saving data")
    def load(self):
        try:
            self.books.clear()
            self.users.clear()
            self.transactions.clear()
            with open("books.txt","r") as f:
                for line in f:
                    try:
                        title,author,issued,can_issue=line.strip().split(",")
                        self.books.append({"title":title,"author":author,"issued":issued=="True","can_issue":can_issue=="True"})
                    except:
                        continue
            with open("users.txt","r") as f:
                for line in f:
                    try:
                        name,user_id=line.strip().split(",")
                        self.users.append({"name":name,"id":user_id})
                    except:
                        continue
            with open("issued.txt","r") as f:
                for line in f:
                    try:
                        key,value=line.strip().split("|")
                        self.transactions[int(key)]=eval(value)
                    except:
                        continue
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")