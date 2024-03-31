# Define the list of states and their neighbors
states = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

# Define the colors available for coloring the map
colors = ['Red', 'Green', 'Blue']

# Function to check if a color assignment is consistent with the neighbors
def is_consistent(state, color, assignment):
    for neighbor in states[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Function to solve the Map Coloring problem using Backtracking
def map_coloring(assignment={}):
    if len(assignment) == len(states):
        return assignment  # All states are colored, return the solution
    
    # Select an unassigned state
    unassigned_state = next(state for state in states if state not in assignment)
    
    # Try assigning each color to the unassigned state
    for color in colors:
        if is_consistent(unassigned_state, color, assignment):
            assignment[unassigned_state] = color
            result = map_coloring(assignment)
            if result is not None:
                return result
            del assignment[unassigned_state]  # Backtrack if no solution found
    
    return None  # No solution found

# Example usage
solution = map_coloring()
if solution:
    print("Map coloring solution:")
    for state, color in solution.items():
        print(f"{state}: {color}")
else:
    print("No solution found.")


