from library import books,storage
import time
issued_books={}
issue_count={}
def str_to_seconds(date_str):
    y,m,d=map(int,date_str.split("-"))
    return time.mktime((y,m,d,0,0,0,0,0,0))
def issue(index,user_id):
    if index>=len(books.book_list):
        print("Invalid book index")
        return
    if not books.book_list[index]["can_issue"]:
        print("Reference book cannot be issued")
        return
    if books.book_list[index]["issued"]:
        print("Book already issued")
        return
    if index not in issue_count:
        issue_count[index]={}
    if user_id not in issue_count[index]:
        issue_count[index][user_id]=0
    if issue_count[index][user_id]>=2:
        print("User can issue this book only 2 times")
        return
    if index not in issued_books:
        issued_books[index]={}
    if user_id in issued_books[index]:
        print("User already has this book issued")
        return
    issue_date=input("Enter issue date (YYYY-MM-DD): ")
    try:
        str_to_seconds(issue_date)
    except:
        print("Invalid date format")
        return
    issued_books[index][user_id]={"issue_date":issue_date}
    issue_count[index][user_id]+=1
    books.mark_issued(index)
    storage.save()
    print("Book issued successfully!")
def return_book(index,user_id):
    if index not in issued_books or user_id not in issued_books[index]:
        print("Book not issued by this user")
        return
    return_date=input("Enter return date (YYYY-MM-DD): ")
    try:
        i_sec=str_to_seconds(issued_books[index][user_id]["issue_date"])
        r_sec=str_to_seconds(return_date)
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
    del issued_books[index][user_id]
    if not issued_books[index]:
        del issued_books[index]
    books.mark_returned(index)
    storage.save()
    print("Book returned successfully!")
def view_issued():
    if not issued_books:
        print("No issued books")
        return
    for b,data in issued_books.items():
        for user,info in data.items():
            print("Book:",b,"User:",user,"Issue Date:",info["issue_date"])