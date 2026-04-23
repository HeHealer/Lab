from library import books
class LibrarySearch:
    def __init__(self):
        self.book_list=books.book_list
    def search_title(self,name):
        found=False
        for b in self.book_list:
            if name.lower() in b["title"].lower():
                print(b)
                found=True
        if not found:
            print("No book found with that title")
    def search_author(self,name):
        found=False
        for b in self.book_list:
            if name.lower() in b["author"].lower():
                print(b)
                found=True
        if not found:
            print("No book found with that author")
    def search_available(self):
        available=books.get_available()
        if not available:
            print("No available books")
            return
        for b in available:
            print(b)