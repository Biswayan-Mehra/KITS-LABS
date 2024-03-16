n = int(input("Enter no. of vertices: "))
distMat = eval(input("Enter the distance Matrix: "))

for k in range(n):
    for i in range(n):
        for j in range(n):
            distMat[i][j] = min(distMat[i][j], distMat[i][k] + distMat[k][j])
        
print(distMat)

"""
[[0,3,999,5],[2,0,999,4],[999,1,0,999],[999,999,2,0]]
"""
