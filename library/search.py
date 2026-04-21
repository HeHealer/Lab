from library import books
def search_title(name):
    found = False
    for b in books.book_list:
        if name.lower() in b["title"].lower():
            print(b)
            found = True
    if not found:
        print("No book found with that title")
def search_author(name):
    found = False
    for b in books.book_list:
        if name.lower() in b["author"].lower():
            print(b)
            found = True
    if not found:
        print("No book found with that author")
def search_available():
    available = books.get_available()
    if not available:
        print("No available books")
        return
    for b in available:
        print(b)
