from library import storage
class UserManager:
    def __init__(self):
        self.user_list=[]
    def __len__(self):
        return len(self.user_list)
    def add_user(self,name,user_id):
        self.user_list.append({"name":name,"id":user_id})
        storage.save()
        print("User added and saved!")
    def display_user(self):
        if not self.user_list:
            print("No users available")
            return
        for i,u in enumerate(self.user_list):
            print(i,u)
    def delete_user(self,user_id):
        found=False
        i=0
        while i<len(self.user_list):
            if self.user_list[i]["id"]==user_id:
                self.user_list.pop(i)
                found=True
            else:
                i+=1
        storage.save()
        if found:
            print("User deleted and saved!")
        else:
            print("User not found")
    def update_user(self,user_id,new_name):
        found=False
        for u in self.user_list:
            if u["id"]==user_id:
                u["name"]=new_name
                found=True
                break
        if found:
            storage.save()
            print("User updated and saved!")
        else:
            print("User not found")
    def find_user(self,user_id):
        for u in self.user_list:
            if u["id"]==user_id:
                print(u)
                return
        print("User not found")
    def count_users(self):
        print("Total users:",len(self.user_list))
    def menu(self):
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
                self.add_user(input("Enter name: "),input("Enter ID: "))
            elif c=="2":
                self.display_user()
            elif c=="3":
                self.update_user(input("Enter user ID: "),input("Enter new name: "))
            elif c=="4":
                self.delete_user(input("Enter user ID: "))
            elif c=="5":
                self.find_user(input("Enter user ID: "))
            elif c=="6":
                self.count_users()
            else:
                print("Invalid choice!")