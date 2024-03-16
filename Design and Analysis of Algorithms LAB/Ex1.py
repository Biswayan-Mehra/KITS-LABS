items = []
order = []
profit = 0.0

def Greedy(maxw):
    count = 0
    profit = 0.0
    for x in items:
        if maxw >= x.weight:
            count += 1
            maxw -= x.weight
            order.append(x.copy(x.weight, x.value))
            profit += x.value
        else:
            order.append(x.copy(maxw, maxw*x.ratio))
            x.Mod(maxw, maxw*x.ratio)
            profit += maxw*x.ratio
            break
    while count != 0:
        items.pop(0)
        count -= 1
    return profit

class item:
    def __init__(self, n, w, v):
        self.name = n
        self.weight = float(w)
        self.value = float(v)
        self.ratio = round(self.value/self.weight,3)
       
    def Mod(self, neww, newv):
        self.weight -= neww
        self.value -= newv
         
    def copy(self, neww, newv):
        return item(self.name, neww, newv)
    
    def display(self):
        print(f"Name: {self.name}\tWeight: {self.weight}\tValue: {self.value}")

while True:
    print("\nGreedy Menu:\n0. Exit\n1. Insert Item\n2. Display Store items\n3. Display Order List\n")
    choice = int(input("Enter your Choice: "))
    if choice == 0:
        print("System Terminated...")
        exit(0)
    elif choice == 1:
        items.append(item(input("Enter item name: "), input("Enter weight: "), input("Enter value: ")))
        items = sorted(items, key = lambda x : x.ratio, reverse=True)
    elif choice == 2:
        print("Store Item List: ")
        for x in items:
            x.display()
    elif choice == 3:
        profit = Greedy(float(input("Enter the max items: ")))
        print("Greedy Order List: ")
        for x in order:
            x.display()
        print("Total Profit:",profit)
    else:
        print("Invalid Choice...")