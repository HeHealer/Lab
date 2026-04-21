from library import storage
import pandas as pd
book_list=[]
def add(title,author,can_issue):
    book_list.append({"title":title,"author":author,"issued":False,"can_issue":can_issue=="yes"})
    storage.save()
    print("Book added and saved!")
def display():
    if not book_list:
        print("No books available")
        return
    print("\n===== VIEW BOOKS =====")
    print("1 Show all books")
    print("2 Total count")
    print("3 Sort by title")
    print("4 Sort by author")
    choice=input("Enter choice: ")
    if choice=="1":
        df=pd.DataFrame(book_list)
        df.index.name="ID"
        print(df)
    elif choice=="2":
        print("Total books:",len(book_list))
    elif choice=="3":
        sort_by_title()
        df=pd.DataFrame(book_list)
        df.index.name="ID"
        print(df)
    elif choice=="4":
        sort_by_author()
        df=pd.DataFrame(book_list)
        df.index.name="ID"
        print(df)
    else:
        print("Invalid choice!")
def delete(index):
    try:
        book_list.pop(index)
        storage.save()
        print("Book deleted")
    except:
        print("Invalid index")
def update(index,title,author):
    try:
        book_list[index]["title"]=title
        book_list[index]["author"]=author
        storage.save()
        print("Book updated")
    except:
        print("Invalid index")
def get_available():
    return [b for b in book_list if not b["issued"]]
def mark_issued(index):
    try:
        if not book_list[index]["can_issue"]:
            print("Reference book cannot be issued")
            return
        book_list[index]["issued"]=True
        storage.save()
    except:
        print("Invalid index")
def mark_returned(index):
    try:
        book_list[index]["issued"]=False
        storage.save()
    except:
        print("Invalid index")
def show_issued():
    if not book_list:
        print("No issued books")
        return
    rows=[b for b in book_list if b["issued"]]
    if not rows:
        print("No issued books")
        return
    df=pd.DataFrame(rows)
    print(df)
def show_reference_books():
    rows=[b for b in book_list if not b["can_issue"]]
    if not rows:
        print("No reference books available")
        return
    df=pd.DataFrame(rows)
    df.index.name="ID"
    print(df)
def sort_by_title():
    for i in range(len(book_list)):
        for j in range(i+1,len(book_list)):
            if book_list[i]["title"]>book_list[j]["title"]:
                book_list[i],book_list[j]=book_list[j],book_list[i]
def sort_by_author():
    for i in range(len(book_list)):
        for j in range(i+1,len(book_list)):
            if book_list[i]["author"]>book_list[j]["author"]:
                book_list[i],book_list[j]=book_list[j],book_list[i]
