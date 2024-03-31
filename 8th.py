# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Function to perform Depth-First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes
    
    visited.add(start)  # Mark the current node as visited
    print(start)        # Process the current node (in this case, just printing)

    neighbors = graph.get(start, [])  # Get the neighbors of the current node
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively visit unvisited neighbors

# Example usage
start_node = 'A'
print("DFS traversal:")
dfs(graph, start_node)

