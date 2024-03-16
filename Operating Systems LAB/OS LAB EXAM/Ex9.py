import os
path ="C:/Users/mehra/Codes/"
while True:
    n = int(input("1.Create Directory 2.Create File 3.Delete File 4.Search File 5.Display 6.Exit\n"))
    if n==1:
        os.mkdir(path+input("Enter dir name: "))
    elif n==2:
        with open(path+input("Enter dir name:")+"/"+input("Enter file name: "), "w") as f:
            f.write(input("Enter data: "))   
    elif n==3:
        os.remove(path+input("Enter dir name:")+"/"+input("Enter file name: "))        
    elif n==4:
        if os.path.exists(path+input("Enter dir name:")+"/"+input("Enter file name: ")):
            print("File found.")
        else:
            print("File not found.")      
    elif n==5:
        for dir in os.listdir(path+input("Enter dir name:")+"/"):
            print("->"+dir, end='')
    elif n==6:
        exit(0)
