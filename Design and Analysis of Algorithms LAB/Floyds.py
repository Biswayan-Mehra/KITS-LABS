nV = int(input("Enter the number of vertices: ")) # The number of vertices

# Taking input from the user for the graph G
G = []
print("Enter the adjacency matrix for the graph G: ")
for i in range(nV):
    row = list(map(int, input().split()))
    G.append(row)

def floyd_warshall(distance):
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) # check if every element is small or if we add the 2 
    print_solution(distance)

def print_solution(distance): # to just print it like a matrix 
    for i in range(nV):
        for j in range(nV):
            print(distance[i][j], end="  ")
        print(" ")

floyd_warshall(G)
