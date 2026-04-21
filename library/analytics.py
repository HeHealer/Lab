import pandas as pd
import numpy as np
from library import books
def df():
    return pd.DataFrame(books.book_list)
def summary():
    d = df()
    if d.empty:
        print("No data")
        return
    print("Total:", len(d))
    print("Authors:", d["author"].nunique())
def random_book():
    d = df()
    if len(d) == 0:
        print("No books")
        return
    i = np.random.randint(0, len(d))
    print(d.iloc[i])
def books_per_author():
    d = df()
    if d.empty:
        print("No data")
        return
    counts = d["author"].value_counts()
    print("\nBooks per Author:")
    print(counts)
def show_file_data():
    try:
        d = pd.read_csv("books.txt", names=["title", "author", "issued"])
        print(d)
    except:
        print("File not found")
def menu():
    while True:
        print("\n===== ANALYTICS MENU =====")
        print("1 Summary")
        print("2 Random Book")
        print("3 Books per Author")
        c=input("Enter choice: ")
        if c=="1":
            summary()
        elif c=="2":
            random_book()
        elif c=="3":
            books_per_author()
        else:
            print("Invalid choice!")