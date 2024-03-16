class stack:
    def __init__(self):
        self.elements = []
        self.size = int(input("Enter the stack size: "))

    def push(self, data):
        if len(self.elements) == self.size:
            print("Stack OverFlow...")
        else:
            self.elements.append(data)

    def pop(self):
        if len(self.elements) == 0:
            print("Stack UnderFlow...")
        else:
            self.elements.pop()

    def peek(self):
        if len(self.elements) == 0:
            print("Stack UnderFlow...")
        else:
            print(self.elements[-1])

    def show(self):
        print(self.elements)


stack = stack()
while True:
    print("\nMenu:\n1.Push\n2.Pop\n3.Show\n4.Peek\n5.Exit\n")
    choice = int(input("Enter your Choice..."))
    if choice == 1:
        stack.push(input("Enter the element..."))
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.show()
    elif choice == 4:
        stack.peek()
    elif choice == 5:
        print("System Terminated...")
        exit(0)
    else:
        print("Invalid Choice...")
