from library import storage
import pandas as pd
class Library:
    def __init__(self):
        self.book_list=[]
    def __len__(self):
        return len(self.book_list)
    def __str__(self):
        return f"Total books: {len(self.book_list)}"
    def add(self,title,author,can_issue):
        self.book_list.append({"title":title,"author":author,"issued":False,"can_issue":can_issue=="yes"})
        storage.save()
        print("Book added and saved!")
    def display(self):
        if not self.book_list:
            print("No books available")
            return
        print("\n===== VIEW BOOKS =====")
        print("1 Show all books")
        print("2 Total count")
        print("3 Sort by title")
        print("4 Sort by author")
        choice=input("Enter choice: ")
        if choice=="1":
            df=pd.DataFrame(self.book_list)
            df.index.name="ID"
            print(df)
        elif choice=="2":
            print("Total books:",len(self.book_list))
        elif choice=="3":
            self.sort_by_title()
            df=pd.DataFrame(self.book_list)
            df.index.name="ID"
            print(df)
        elif choice=="4":
            self.sort_by_author()
            df=pd.DataFrame(self.book_list)
            df.index.name="ID"
            print(df)
        else:
            print("Invalid choice!")
    def delete(self,index):
        try:
            self.book_list.pop(index)
            storage.save()
            print("Book deleted")
        except:
            print("Invalid index")
    def update(self,index,title,author):
        try:
            self.book_list[index]["title"]=title
            self.book_list[index]["author"]=author
            storage.save()
            print("Book updated")
        except:
            print("Invalid index")
    def get_available(self):
        return [b for b in self.book_list if not b["issued"]]
    def mark_issued(self,index):
        try:
            if not self.book_list[index]["can_issue"]:
                print("Reference book cannot be issued")
                return
            self.book_list[index]["issued"]=True
            storage.save()
        except:
            print("Invalid index")
    def mark_returned(self,index):
        try:
            self.book_list[index]["issued"]=False
            storage.save()
        except:
            print("Invalid index")
    def show_issued(self):
        if not self.book_list:
            print("No issued books")
            return
        rows=[b for b in self.book_list if b["issued"]]
        if not rows:
            print("No issued books")
            return
        df=pd.DataFrame(rows)
        print(df)
    def show_reference_books(self):
        rows=[b for b in self.book_list if not b["can_issue"]]
        if not rows:
            print("No reference books available")
            return
        df=pd.DataFrame(rows)
        df.index.name="ID"
        print(df)
    def sort_by_title(self):
        for i in range(len(self.book_list)):
            for j in range(i+1,len(self.book_list)):
                if self.book_list[i]["title"]>self.book_list[j]["title"]:
                    self.book_list[i],self.book_list[j]=self.book_list[j],self.book_list[i]
    def sort_by_author(self):
        for i in range(len(self.book_list)):
            for j in range(i+1,len(self.book_list)):
                if self.book_list[i]["author"]>self.book_list[j]["author"]:
                    self.book_list[i],self.book_list[j]=self.book_list[j],self.book_list[i]