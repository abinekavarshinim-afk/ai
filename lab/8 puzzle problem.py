import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)  # 0 is the blank


def heuristic(board):
    return sum(
        abs(i // 3 - (tile - 1) // 3) + abs(i % 3 - (tile - 1) % 3)
        for i, tile in enumerate(board) if tile
    )


def solve(start):
    queue = [(heuristic(start), 0, start, [])]
    seen = {start}

    while queue:
        _, moves, board, path = heapq.heappop(queue)
        if board == goal:
            return path + [board]

        blank = board.index(0)
        for other in (blank - 3, blank + 3, blank - 1, blank + 1):
            if 0 <= other < 9 and (abs(blank - other) != 1 or blank // 3 == other // 3):
                next_board = list(board)
                next_board[blank], next_board[other] = next_board[other], next_board[blank]
                next_board = tuple(next_board)
                if next_board not in seen:
                    seen.add(next_board)
                    heapq.heappush(queue, (
                        moves + 1 + heuristic(next_board),
                        moves + 1, next_board, path + [board]
                    ))

    return None


result = solve(start)
if result:
    for board in result:
        print(*(board[i:i + 3] for i in (0, 3, 6)), sep="\n")
        print()
else:
    print("No solution")
