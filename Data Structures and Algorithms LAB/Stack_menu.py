max = int(input("Enter the max elements: "))
top = 0
stack = []

while True:
    print("1. Push\n2. Pop\n3. Display\n4. Peek\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter the element: ")
        top += 1
        if top <= max:
            stack.append(data)
        else:
            print("Stack Overflow...")
            top -= 1
    elif choice == 2:
        if top > 0:
            stack.pop()
            top -= 1
        else:
            print("Stack Underflow...")
    elif choice == 3:
        print(stack)
    elif choice == 4:
        if top == 0:
            print("Stack Underflow...")
        else:
            print(stack[top-1])
    elif choice == 5:
        print("System Terminated...")
        break
