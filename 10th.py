import heapq

# Define a graph as an adjacency list
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 3, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 5},
    'D': {'B': 7, 'C': 5}
}

# Define heuristic values for each node (straight-line distance to the goal)
heuristic = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 0
}

# Function to perform A* search
def astar(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(0, start)]  # Priority queue to store nodes to visit, ordered by the total cost
    came_from = {}  # Dictionary to store parent nodes

    while priority_queue:
        _, current = heapq.heappop(priority_queue)  # Pop the node with the lowest total cost
        visited.add(current)

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_cost = cost + heuristic[neighbor]  # Cost from start to neighbor via current node
                heapq.heappush(priority_queue, (new_cost, neighbor))  # Add neighbor to the queue
                came_from[neighbor] = current  # Record the current node as the parent of the neighbor

    return None  # No path found

# Example usage
start_node = 'A'
goal_node = 'D'
path = astar(graph, start_node, goal_node, heuristic)
print("Shortest path from", start_node, "to", goal_node, ":", path)





