w = eval(input("Enter the weights: "))
v = eval(input("Enter the values: "))
W = int(input("Enter the max Weight: "))

m = [[0]*(W+1) for _ in range(0, len(v)+1)]

for i in range(1, len(m)):
    for j in range(1, len(m[i])):
        if w[i-1] >= j:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(m[i-1][j], v[i-1] + m[i-1][j-w[i-1]])

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
        V = m[i][j]
    print()
    
print("Max profit: ", V)

#backtracking
items = []
weight = W
for i in range(len(m), 0, -1):
    if V <= 0:
        break
    if V == m[i-1][weight]:
        continue
    else:
        items.append(w[i-1])
        V -= v[i-1]
        weight -= w[i-1]
        
print(items)    

"""
[1,2,3]
[10,15,40]
6
"""