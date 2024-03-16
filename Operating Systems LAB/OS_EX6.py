p=int(input('Enter the number of process: '))
r=int(input('Enter the number of resources: '))
maxavail=eval(input('Enter the availible resources: '))

allocated=[]*p
maximum=[]*p
Sequence=[0]*p
visited=[0]*p

for i in range(p):
    print('Enter the allocation of ',i+1)
    a=eval(input())
    allocated.append(a)
    print('Enter the max resources of',i+1)
    m=eval(input())
    maximum.append(m)
    
needed=[]*p

for i in range(p):
    n=[]
    for j in range(r):
        ns=maximum[i][j]-allocated[i][j]
        n.append(ns)
    needed.append(n)
    
tallocate=[]*r

for i in range(r):
    sum=0
    for j in range(p):
        sum+=allocated[j][i]
    tallocate.append(sum)
    
available=[]*r

for i in range(r):
    available.append(maxavail[i]-tallocate[i])
    
def check(i):
    for j in range(r):
        if(needed[i][j]>available[j]):
                return 0
        return 1
    
count = 0

while( count < p ):
    temp=0
    for i in range( p ):
        if visited[i] == 0:
            if(check(i)):
                Sequence[count]=i;
                count+=1
                visited[i]=1
                temp=1
                for j in range(r):
                    available[j] += allocated[i][j]
    if(temp == 0):
        break
    
if(count < p):
    print('The system is Unsafe')
else:
    print("The system is Safe")
    print("Safe Sequence: ",Sequence)
    print("Available Resource:",available)
    
print("Process    Allocated      Maximum       Remaining")

for i in range(p):
    print(i,'      ',allocated[i],"     ",maximum[i],'     ',needed[i])