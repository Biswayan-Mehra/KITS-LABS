class Queue:
    def __init__(self):
        self.elements = []
        self.size = int(input("Enter the Queue size: "))
        self.rear = 0

    def enqueue(self, data):
        if len(self.elements) == self.size:
            print("Queue Overflow...")
        else:
            self.elements.append(data)

    def dequeue(self):
        if self.rear == self.size or len(self.elements) == 0:
            self.rear = 0
            self.elements = []
            print("Queue UnderFlow...")
        else:
            self.rear += 1

    def show(self):
        print(self.elements[self.rear:])


queue = Queue()
while True:
    print("\nMenu:\n1.Enqueue\n2.Dequeue\n3.Show\n4.Exit\n")
    choice = int(input("Enter your Choice..."))
    if choice == 1:
        queue.enqueue(input("Enter the element..."))
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.show()
    elif choice == 4:
        print("System Terminated...")
        exit(0)
    else:
        print("Invalid Choice...")
