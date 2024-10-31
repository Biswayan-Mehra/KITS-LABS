# Define a Queue class to manage a queue structure
class Queue:
    def __init__(self):
        # Initialize the queue with an empty list, set its size, and start the rear pointer at 0
        self.elements = []
        self.size = int(input("Enter the Queue size: "))
        self.rear = 0

    def enqueue(self, data):
        # Add an element to the queue if it has not reached its size limit
        if len(self.elements) == self.size:
            print("Queue Overflow...")
        else:
            self.elements.append(data)

    def dequeue(self):
        # Remove an element from the queue if it is not empty
        if self.rear == self.size or len(self.elements) == 0:
            # Reset rear pointer and empty the queue on underflow
            self.rear = 0
            self.elements = []
            print("Queue UnderFlow...")
        else:
            # Move the rear pointer to the next element
            self.rear += 1

    def show(self):
        # Display the current elements from the rear pointer onwards
        print(self.elements[self.rear:])


# Instantiate a Queue object and display a menu for queue operations
queue = Queue()
while True:
    print("\nMenu:\n1.Enqueue\n2.Dequeue\n3.Show\n4.Exit\n")
    choice = int(input("Enter your Choice..."))

    if choice == 1:
        # Call enqueue method to add an element
        queue.enqueue(input("Enter the element..."))
    elif choice == 2:
        # Call dequeue method to remove an element
        queue.dequeue()
    elif choice == 3:
        # Call show method to display the queue elements
        queue.show()
    elif choice == 4:
        # Exit the program
        print("System Terminated...")
        exit(0)
    else:
        # Handle invalid menu choices
        print("Invalid Choice...")
