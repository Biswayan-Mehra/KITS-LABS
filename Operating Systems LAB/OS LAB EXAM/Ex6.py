n = int(input("Enter no. of processes: "))
r = int(input("Enter no. of resources: "))

allocate = eval(input("Enter allocation Matrix: "))
max_need = eval(input("Enter max need Matrix: "))

req_need = [[max_need[i][j] - allocate[i][j]for j in range(len(max_need[i]))] for i in range(len(max_need))]

Available = eval(input("Enter availabe resources: "))

seq = ""

while len(req_need)>0:
    for i in range(n):
        f=0
        for j in range(r):
            if Available[i] >= req_need[i][j]:
                f+=1
        if f==n:
            print("Process",i,"Executed.")
            seq += "P"+str(i)+" "
            for m in range(len(allocate[i])):
                Available[m] += allocate[i][m]
            req_need.remove(req_need[i])
            allocate.pop(allocate[i])
        else:
            break
    
    if len(req_need) != 0:
        print("Unsafe State...")
        exit(0)
else:
    print(seq)
            
#[[0,1,0],[3,0,2],[3,0,2],[2,1,1],[0,0,2]]
#[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
#[1,0,2]

"""[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
[3,3,2]"""