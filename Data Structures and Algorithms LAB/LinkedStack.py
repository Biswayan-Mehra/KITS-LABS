class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head is None:
            print("Stack UnderFlow...")
        else:
            self.head = self.head.next

    def show(self):
        linkNode = self.head
        while linkNode is not None:
            print(linkNode.data + " -->", end=" ")
            linkNode = linkNode.next
        print("None")


linklist = LinkedList()
choice = 0
while choice != 4:
    print("\nMenu:\n1.Push\n2.Pop\n3.Show\n4.Exit\n")
    choice = int(input("Enter the Choice..."))
    if choice == 1:
        linklist.push(input("Enter the element..."))
    elif choice == 2:
        linklist.pop()
    elif choice == 3:
        linklist.show()
    elif choice == 4:
        print("System Terminated...")
        exit(0)
    else:
        print("Invalid Choice...")
