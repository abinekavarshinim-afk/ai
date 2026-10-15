from collections import deque

def solve(capacity_a, capacity_b, target):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path + [(a, b)]

        pour_a_to_b = min(a, capacity_b - b)
        pour_b_to_a = min(b, capacity_a - a)

        next_states = [
            (capacity_a, b),                 # Fill jug A
            (a, capacity_b),                 # Fill jug B
            (0, b),                          # Empty jug A
            (a, 0),                          # Empty jug B
            (a - pour_a_to_b, b + pour_a_to_b),  # Pour A into B
            (a + pour_b_to_a, b - pour_b_to_a),  # Pour B into A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(a, b)]))

    return None


# Example: measure 2 liters using 4- and 3-liter jugs
solution = solve(4, 3, 2)

if solution:
    for a, b in solution:
        print(f"Jug A: {a} L, Jug B: {b} L")
else:
    print("No solution")
