def is_possible(edge, mst_edges):
    mst_copy = dict(mst_edges)
    start = edge[0]
    node = edge[1]
    while node in mst_copy.keys() and node != start:
        node = mst_copy[node]
    return node != start

def kruskals(graph):
    weights = dict()
    for node in graph:
        for neighbour, weight in graph[node]:
            edge = tuple(sorted((node, neighbour)))
            weights[edge] = min(weight, weights.get(edge, float("inf")))
        
    mst_edges = set()
    queue = sorted(weights.keys(), key = lambda x: weights[x])
    mst_edges.add(queue[0])
    queue.pop(0)
    ind = 0
    while len(queue) > 0:
        edge = queue.pop(0)
        if is_possible(edge, mst_edges):
            mst_edges.add(edge)
            
    mst = dict()
    for edge in mst_edges:
        mst[edge[0]] = (edge[1], weights[edge])
    return mst

vertices = input("Enter all vertices of the graph: ").split(" ")
graph = dict()
for vertice in vertices:
    neighbours = list()
    print("Enter neighbours of", vertice, "as neighbour,weight : ")
    for edge in input().split(" "):
        neighbour, weight = edge.split(",")
        neighbours.append((neighbour, int(weight)))
    graph[vertice] = neighbours
    
print("The minimum spanning tree is: ", kruskals(graph))