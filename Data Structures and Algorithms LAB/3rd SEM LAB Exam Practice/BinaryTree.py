class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        newNode = BinaryNode(data)
        if root is None:
            return BinaryNode(data)
        if root.data < data:
            if root.right_child:
                self.insert(root.right_child, data)
            else:
                root.right_child = BinaryNode(data)
        elif root.data >= data:
            if root.left_child:
                self.insert(root.left_child, data)
            else:
                root.left_child = BinaryNode(data)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left_child)
        print(root.data, end=" ")
        self.inorder(root.right_child)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left_child)
        self.preorder(root.right_child)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left_child)
        self.postorder(root.right_child)
        print(root.data, end=" ")

BST = BinarySearchTree()
root = None
flag = True
while True:
    print("\nMenu\n1.Insert\n2.PreOrder\n3.InOrder\n4.PostOrder\n5.Exit\n")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        if flag == True:
            root = BinaryNode(int(input("Enter the data: ")))
            flag = False
        else:
            BST.insert(root, int(input("Enter the data: ")))
    elif choice == 2:
        BST.preorder(root)
    elif choice == 3:
        BST.inorder(root)
    elif choice == 4:
        BST.postorder(root)
    elif choice == 5:
        print("System Terminated...")
        exit(0)
    else:
        print("Invalid Choice...")