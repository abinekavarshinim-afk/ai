
from itertools import permutations

n = 4
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = range(1, n)
min_cost = float('inf')
best_path = []

for path in permutations(cities):
    route = (0,) + path + (0,)
    total = sum(cost[route[i]][route[i+1]]
                for i in range(n))

    if total < min_cost:
        min_cost = total
        best_path = route

print("Best path:", [city + 1 for city in best_path])
print("Minimum cost:", min_cost)
