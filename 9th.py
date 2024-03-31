
from sys import maxsize 
from itertools import permutations

# Function to calculate the total distance of a tour
def total_distance(tour, distances):
    total = 0
    for i in range(len(tour) - 1):
        total += distances[tour[i]][tour[i + 1]]
    total += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total

# Function to find the optimal tour using brute force
def tsp_brute_force(distances):
    num_cities = len(distances)
    best_tour = None
    min_distance = float('inf')
    
    for tour in permutations(range(num_cities)):
        distance = total_distance(tour, distances)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    
    return best_tour, min_distance

# Example usage
# Define the distances between cities (example: distances[i][j] is the distance from city i to city j)
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_tour, min_distance = tsp_brute_force(distances)
print("Optimal tour:", optimal_tour)
print("Minimum distance:", min_distance)






