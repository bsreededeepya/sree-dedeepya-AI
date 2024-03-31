from collections import deque

from collections import deque

# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Function to perform Breadth-First Search
def bfs(graph, start):
    visited = set()              # Set to keep track of visited nodes
    queue = deque([start])       # Initialize queue with the starting node

    while queue:
        node = queue.popleft()   # Dequeue a node from the queue
        if node not in visited:
            print(node)          # Process the node (in this case, just printing)
            visited.add(node)    # Mark the node as visited
            neighbors = graph.get(node, [])  # Get the neighbors of the current node
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)   # Enqueue unvisited neighbors              

# Example usage
start_node = 'A'
print("BFS traversal:")
bfs(graph, start_node)





