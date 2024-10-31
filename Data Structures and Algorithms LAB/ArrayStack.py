# Define a Stack class to manage a stack structure
class stack:
    def __init__(self):
        # Initialize the stack with an empty list and set its size
        self.elements = []
        self.size = int(input("Enter the stack size: "))

    def push(self, data):
        # Add an element to the stack if it has not reached its size limit
        if len(self.elements) == self.size:
            print("Stack OverFlow...")
        else:
            self.elements.append(data)

    def pop(self):
        # Remove the top element from the stack if it is not empty
        if len(self.elements) == 0:
            print("Stack UnderFlow...")
        else:
            self.elements.pop()

    def peek(self):
        # Display the top element without removing it if the stack is not empty
        if len(self.elements) == 0:
            print("Stack UnderFlow...")
        else:
            print(self.elements[-1])

    def show(self):
        # Display all elements in the stack
        print(self.elements)


# Instantiate a stack object and display a menu for stack operations
stack = stack()
while True:
    print("\nMenu:\n1.Push\n2.Pop\n3.Show\n4.Peek\n5.Exit\n")
    choice = int(input("Enter your Choice..."))

    if choice == 1:
        # Call push method to add an element
        stack.push(input("Enter the element..."))
    elif choice == 2:
        # Call pop method to remove the top element
        stack.pop()
    elif choice == 3:
        # Call show method to display all elements in the stack
        stack.show()
    elif choice == 4:
        # Call peek method to display the top element
        stack.peek()
    elif choice == 5:
        # Exit the program
        print("System Terminated...")
        exit(0)
    else:
        # Handle invalid menu choices
        print("Invalid Choice...")
