from library import storage
user_list = []
def add_user(name, user_id):
    user_list.append({
        "name": name,
        "id": user_id
    })
    storage.save()
    print("User added and saved!")
def display_user():
    if not user_list:
        print("No users available")
        return
    for i, u in enumerate(user_list):
        print(i, u)
def delete_user(user_id):
    found = False
    i = 0
    while i < len(user_list):
        if user_list[i]["id"] == user_id:
            user_list.pop(i)
            found = True
        else:
            i += 1
    storage.save()
    if found:
        print("User deleted and saved!")
    else:
        print("User not found")
def update_user(user_id, new_name):
    found = False
    for u in user_list:
        if u["id"] == user_id:
            u["name"] = new_name
            found = True
            break
    if found:
        storage.save()
        print("User updated and saved!")
    else:
        print("User not found")
def find_user(user_id):
    for u in user_list:
        if u["id"] == user_id:
            print(u)
            return
    print("User not found")
def count_users():
    print("Total users:", len(user_list))
def user():
    while True:
        print("\n===== USER MENU =====")
        print("1 Add User")
        print("2 View Users")
        print("3 Update User")
        print("4 Delete User")
        print("5 Find User")
        print("6 Count Users")
        c=input("Enter choice: ")
        if c=="1":
            add_user(input("Enter name: "),input("Enter ID: "))
        elif c=="2":
            display_user()
        elif c=="3":
            update_user(input("Enter user ID: "),input("Enter new name: "))
        elif c=="4":
            delete_user(input("Enter user ID: "))
        elif c=="5":
            find_user(input("Enter user ID: "))
        elif c=="6":
            count_users()
        else:
            print("Invalid choice!")