w = eval(input("Enter the weights: "))
v = eval(input("Enter the values: "))
W = int(input("Enter the max Weight: "))
o = [i for i in range(1,len(w)+1)]
r = [v[i]/w[i] for i in range(len(w))]
x = [0]*len(w)
V = 0

w,v,r,o = zip(*sorted(zip(w,v,r,o), key= lambda x:x[2], reverse = True))

for i in range(len(w)):
    if w[i] < W:
        x[i] = 1
        V += v[i]
        W -= w[i]
    else:
        x[i] = W/w[i]
        V += v[i]*x[i]
        W = 0
        break

print("Items: ",o)
print("Ratio: ",x)
print("Total Value: ",V)
        
"""
    [4,8,2,6,1]
    [12,32,40,30,50]
"""