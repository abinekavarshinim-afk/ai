# Map Colouring using CSP

# Define the map regions
regions = ['A', 'B', 'C', 'D']

# Available colours
colours = ['Red', 'Green', 'Blue']

# Define neighbouring regions
neighbours = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Check whether the colour is valid
def is_valid(region, colour, assignment):
    for neighbour in neighbours[region]:
        if neighbour in assignment and assignment[neighbour] == colour:
            return False
    return True

# CSP Backtracking algorithm
def map_colouring(assignment):
    if len(assignment) == len(regions):
        return assignment

    region = next(r for r in regions if r not in assignment)

    for colour in colours:
        if is_valid(region, colour, assignment):
            assignment[region] = colour

            result = map_colouring(assignment)

            if result:
                return result

            del assignment[region]

    return None

# Display the result
solution = map_colouring({})

if solution:
    print("Map Colouring Solution:")
    for region, colour in solution.items():
        print(region, ":", colour)
else:
    print("No solution exists")
