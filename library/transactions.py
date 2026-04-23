from library import books,storage
import time
class Transactions:
    def __init__(self):
        self.issued_books={}
        self.issue_count={}
    def str_to_seconds(self,date_str):
        y,m,d=map(int,date_str.split("-"))
        return time.mktime((y,m,d,0,0,0,0,0,0))
    def issue(self,index,user_id):
        if index>=len(books.book_list):
            print("Invalid book index")
            return
        if not books.book_list[index]["can_issue"]:
            print("Reference book cannot be issued")
            return
        if books.book_list[index]["issued"]:
            print("Book already issued")
            return
        if index not in self.issue_count:
            self.issue_count[index]={}
        if user_id not in self.issue_count[index]:
            self.issue_count[index][user_id]=0
        if self.issue_count[index][user_id]>=2:
            print("User can issue this book only 2 times")
            return
        if index not in self.issued_books:
            self.issued_books[index]={}
        if user_id in self.issued_books[index]:
            print("User already has this book issued")
            return
        issue_date=input("Enter issue date (YYYY-MM-DD): ")
        try:
            self.str_to_seconds(issue_date)
        except:
            print("Invalid date format")
            return
        self.issued_books[index][user_id]={"issue_date":issue_date}
        self.issue_count[index][user_id]+=1
        books.mark_issued(index)
        storage.save()
        print("Book issued successfully!")
    def return_book(self,index,user_id):
        if index not in self.issued_books or user_id not in self.issued_books[index]:
            print("Book not issued by this user")
            return
        return_date=input("Enter return date (YYYY-MM-DD): ")
        try:
            i_sec=self.str_to_seconds(self.issued_books[index][user_id]["issue_date"])
            r_sec=self.str_to_seconds(return_date)
        except:
            print("Invalid date format")
            return
        days=int((r_sec-i_sec)/(60*60*24))
        if days<0:
            print("Return date cannot be before issue date")
            return
        if days>20:
            print("Late return! Fine =", (days-20)*2, "Rs")
        else:
            print("Returned on time")
        del self.issued_books[index][user_id]
        if not self.issued_books[index]:
            del self.issued_books[index]
        books.mark_returned(index)
        storage.save()
        print("Book returned successfully!")
    def view_issued(self):
        if not self.issued_books:
            print("No issued books")
            return
        for b,data in self.issued_books.items():
            for user,info in data.items():
                print("Book:",b,"User:",user,"Issue Date:",info["issue_date"])