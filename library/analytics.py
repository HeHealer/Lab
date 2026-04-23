import pandas as pd
import numpy as np
from library import books
class LibraryAnalytics:
    def __init__(self):
        self.data_source=books.book_list
    def df(self):
        return pd.DataFrame(self.data_source)
    def __len__(self):
        return len(self.data_source)
    def __str__(self):
        d=self.df()
        if d.empty:
            return "No data"
        return f"Total books: {len(d)}, Authors: {len(set(d['author']))}"
    def summary(self):
        d=self.df()
        if d.empty:
            print("No data")
            return
        print("Total:",len(d))
        print("Authors:",len(set(d["author"])))
    def random_book(self):
        d=self.df()
        if len(d)==0:
            print("No books")
            return
        i=np.random.randint(0,len(d))
        print(d.iloc[i])
    def books_per_author(self):
        d=self.df()
        if d.empty:
            print("No data")
            return
        counts=d["author"].value_counts()
        print("\nBooks per Author:")
        print(counts)
    def show_file_data(self):
        try:
            d=pd.read_csv("books.txt",names=["title","author","issued"])
            print(d)
        except:
            print("File not found")
    def menu(self):
        while True:
            print("\n===== ANALYTICS MENU =====")
            print("1 Summary")
            print("2 Random Book")
            print("3 Books per Author")
            c=input("Enter choice: ")
            if c=="1":
                self.summary()
            elif c=="2":
                self.random_book()
            elif c=="3":
                self.books_per_author()
            else:
                print("Invalid choice!")