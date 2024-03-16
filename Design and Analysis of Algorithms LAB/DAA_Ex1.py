def Greddy_Fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    value = 0
    weight = 0
    for item in items:
        if weight + item[1] <= capacity:
            weight += item[1]
            value += item[0]
            print("ele:", item)
        else:
            remaining_capacity = capacity - weight
            value += remaining_capacity * item[0] / item[1]
            print("remainingcapacity:", remaining_capacity)
            break
    return value

items = [(60, 10), (100, 20), (120, 30), (100,10), (200,20)]
capacity = 50
print("Maximum value:", Greddy_Fractional_knapsack(items, capacity))
