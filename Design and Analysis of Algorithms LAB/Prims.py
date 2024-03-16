def prims_algo(graph):
    MST = dict()
    unvisited = set(graph.keys())
    node = sorted(graph.keys(), key = lambda x: len(graph[x]))[0]
    unvisited.discard(node)
    while len(unvisited) > 0:
        min_ind = 0
        while graph[node][min_ind][1] not in unvisited:
            min_ind += 1
        MST[node] = graph[node][min_ind]
        node = MST[node][1]
        unvisited.discard(node)
    return MST
        
vertices = input("Enter all vertices of the graph: ").split(" ")
graph = dict()
for vertice in vertices:
    neighbours = list()
    print("Enter neighbours of", vertice, "as neighbour,weight : ")
    for edge in input().split(" "):
        neighbour, weight = edge.split(",")
        neighbours.append((int(weight), neighbour))
    graph[vertice] = list(sorted(neighbours))
    
print("The minimum spanning tree is: ", prims_algo(graph))
