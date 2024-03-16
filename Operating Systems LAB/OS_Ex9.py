import os

class Two_level_dir:
    def __init__(self):
        self.users = {}
        self.path = "."
        self.logged_in = False

    def add_user(self, name, pwd):
        if name in self.users.keys():
            return
        self.users[name] = pwd
        os.mkdir(os.path.join(".", name))

    def login(self, name, pwd):
        self.logged_in = False
        if self.users.get(name) == pwd:
            self.path = os.path.join(".", name)
            self.logged_in = True
        else:
            self.path = "."
    
    def make_dir(self, dir_):
        os.mkdir(os.path.join(self.path, dir_))
    
    def create_file(self, f_name, data):
        with open(os.path.join(self.path, f_name), "a") as f:
            f.write(data)
    
    def update_path(self, path = ""):
        if os.path.exists(path) and os.path.commonpath((path, self.path)) != ".":
            self.path = path
        elif path == "..":
            self.path = os.path.split(path)[0]
        else:
            self.path = os.path.join(self.path, path)
    
    def display(self, path = "."):
        dirs = os.listdir(path)
        for dir_ in dirs:
            print("-> ", dir_)
    
    def display_rec(self, path = ".", start = ""):
        try:
            content = os.listdir(path)
            for item in content:
                print(start, "-> ", item, sep = "")
                self.display_rec(os.path.join(path, item), start + "   ")
        except:
            pass

manager = Two_level_dir()
while True:
    if not manager.logged_in:
        print("Enter \n1 to create a user and \n2 to login to existing: ")
        c = int(input())
        name = input("Enter name: ")
        pwd = input("Enter pwd: ")
        if c == 1:
            manager.add_user(name, pwd)
        if c == 2:
            manager.login(name, pwd)
            if not manager.logged_in:
                print("Invalid login")
    else:
        print("\nCurrently at", manager.path)
        print("Enter \n0 to update path\n1 to create a directory\
        \n2 to create file\
        \n3 to display\
        \n4 to display recursive: ")
        c = int(input())
        if c == 0:
            print("Currently at", manager.path)
            p = input("Move to: ")
            manager.update_path(p)
        if c == 1:
            dir_ = input("Enter directory name: ")
            manager.make_dir(dir_)
        elif c == 2:
            f_name = input("Enter file name: ")
            data = input("Enter file contents: ")
            manager.create_file(f_name, data)
        elif c == 3:
            manager.display(manager.path)
        elif c == 4:
            manager.display_rec(manager.path)
