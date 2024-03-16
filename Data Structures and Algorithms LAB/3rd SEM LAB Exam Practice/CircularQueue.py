class Queue:
    def __init__(self):
        self.size = int(input("Enter the Queue size: "))
        self.elements = [0] * self.size
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.rear == -1:
            self.rear = self.front = 0
            self.elements[self.rear] = data
            return
        if self.rear != self.front:
            print("Queue Overflow...")
        else:
            self.rear = (self.rear + 1) % len(self.elements)
            self.elements[self.rear] = data

    def dequeue(self):
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.elements)

    def show(self):
        if self.front == -1:
            return
        trav = self.front
        while self.rear != trav:
            print(self.elements[trav+1])
            trav = (trav + 1) % len(self.elements)



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
