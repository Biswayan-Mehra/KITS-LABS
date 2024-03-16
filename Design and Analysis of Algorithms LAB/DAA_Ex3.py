def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if items[i-1][1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][1]] + items[i-1][0])
    res = dp[n][capacity]
    print()
    print("    ",end="")
    for j in range(capacity+1):
        print(j, end = " ")
    print()
    print("---" * (capacity+2))
    print("0 | ",end='')
    for j in range(capacity+1):
        print("0", end = " ")
    print()
    for i in range(1, n+1):
        print(str(i)+" | 0", end=' ')
        for j in range(1, capacity+1):
            print(dp[i][j], end=' ')
        print()
    return res

items = []
num = int(input("Enter no. of items:"))
capacity = int(input("Enter max weight of sack:"))
for i in range(num):
    items.append((int(input("Enter value:")), int(input("Enter Weight:"))))
print("Maximum value:", knapsack_01(items, capacity))

#items = [(60, 10), (100, 20), (120, 30), (110, 10), (220, 30)]
#capacity = 50
