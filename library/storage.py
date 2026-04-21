from library import books,users,transactions
def save():
    try:
        with open("books.txt","w") as f:
            for b in books.book_list:
                f.write(b["title"]+","+b["author"]+","+str(b["issued"])+","+str(b.get("can_issue",True))+"\n")
        with open("users.txt","w") as f:
            for u in users.user_list:
                f.write(u["name"]+","+u["id"]+"\n")
        with open("issued.txt","w") as f:
            for book_index,data in transactions.issued_books.items():
                f.write(str(book_index)+"|"+str(data)+"\n")
    except:
        print("Error while saving data")
def load():
    try:
        books.book_list.clear()
        users.user_list.clear()
        transactions.issued_books.clear()
        with open("books.txt","r") as f:
            for line in f:
                try:
                    title,author,issued,can_issue=line.strip().split(",")
                    books.book_list.append({"title":title,"author":author,"issued":issued=="True","can_issue":can_issue=="True"})
                except:
                    continue
        with open("users.txt","r") as f:
            for line in f:
                try:
                    name,user_id=line.strip().split(",")
                    users.user_list.append({"name":name,"id":user_id})
                except:
                    continue
        with open("issued.txt","r") as f:
            for line in f:
                try:
                    key,value=line.strip().split("|")
                    transactions.issued_books[int(key)]=eval(value)
                except:
                    continue
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")
