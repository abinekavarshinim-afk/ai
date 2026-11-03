# Alpha-Beta Pruning Algorithm

def alphabeta(depth, node, alpha, beta, maximizingPlayer):

    if depth == 3:
        return tree[node]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              alpha, beta, False)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              alpha, beta, True)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Leaf node values
tree = [3, 5, 6, 9, 1, 2, 0, -1]

# Initial alpha and beta values
alpha = float('-inf')
beta = float('inf')

# Find the optimal value
result = alphabeta(0, 0, alpha, beta, True)

print("The optimal value is:", result)
