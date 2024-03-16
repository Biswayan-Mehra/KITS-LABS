class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        linkNode = self.head
        if self.head is None:
            self.head = newNode
            return
        while linkNode.next is not None:
            linkNode = linkNode.next
        linkNode.next = newNode

    def delete(self, data):
        linkNode = self.head
        if self.head is None:
            return
        elif linkNode.data == data:
            self.head = linkNode.next
        while linkNode.next is not None:
            if linkNode.next.data == data:
                break
            linkNode = linkNode.next
        if linkNode.next is None:
            return
        linkNode.next = linkNode.next.next

    def show(self):
        linkNode = self.head
        while linkNode is not None:
            print(linkNode.data + " -->", end=" ")
            linkNode = linkNode.next
        print("None")


linklist = LinkedList()
choice = 0
while choice != 4:
    print("\nMenu:\n1.Insert\n2.Delete\n3.Show\n4.Exit\n")
    choice = int(input("Enter the Choice..."))
    if choice == 1:
        linklist.insert(input("Enter the element..."))
    elif choice == 2:
        linklist.delete(input("Enter the element to delete..."))
    elif choice == 3:
        linklist.show()
    elif choice == 4:
        print("System Terminated...")
        exit(0)
    else:
        print("Invalid Choice...")
