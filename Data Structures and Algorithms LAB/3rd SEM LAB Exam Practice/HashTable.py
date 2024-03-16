def hashing(value):
    HashTable[value % len(HashTable)].append(value)


def show():
    for i in range(len(HashTable)):
        print(i, end=" ")
        for j in range(len(HashTable[i])):
            print(" --> ", HashTable[i][j], end=" ")
        print()

def search(value):
    index = value % len(HashTable)
    for i in range(len(HashTable[index])):
        if value == HashTable[index][i]:
            print(index, ", ", i, " --> ", HashTable[index][i])


HashTable = [[] for _ in range(int(input("Enter the hash table size: ")))]
while True:
    print("\nMenu:\n1.Insert\n2.Search\n3.Show\n4.Exit\n")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        hashing(int(input("Enter data: ")))
    elif choice == 2:
        search(int(input("Enter the search element: ")))
    elif choice == 3:
        show()
    elif choice == 4:
        print("System Terminated...")
        exit(0)
    else:
        print("Invalid Choice...")
