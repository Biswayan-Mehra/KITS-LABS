import heapq
def dijkstra(graph, start, end):
    unvisited = set(graph.keys())  
    distances = {vertex: float('inf') for vertex in graph} 
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    # Step 3: Main loop
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_vertex)
        if distances[current_vertex] == float('inf'):
            break
        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + int(weight)
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex
    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.insert(0, current_vertex)
    return path, distances[end]
no_of_vertex = int(input("How many Vertex: "))
graph = {}
for vertexs in range(no_of_vertex):
    name = input("Vertex name: ")
    no_of_connections = int(input("No of connections: "))
    connections = {}
    for i in range(no_of_connections):
        name_connected = input("Name_connected: ")
        weight_distance = input("weight/distance: ")
        connections[name_connected] = weight_distance
    graph[name] = connections
start_vertex = input("Enter the starting vertex: ")
end_vertex = input("Enter the ending vertex: ")
shortest_path, distance = dijkstra(graph, start_vertex, end_vertex)
print(f"Shortest path: {shortest_path}")
print(f"Distance: {distance}")
