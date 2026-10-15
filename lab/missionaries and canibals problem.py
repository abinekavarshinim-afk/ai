from collections import deque

# State: (missionaries_left, cannibals_left, boat_side)
start = (3, 3, 0)  # 0 = left bank, 1 = right bank
goal = (0, 0, 1)
boat_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]


def safe(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)


def solve():
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        m, c, side = state
        for dm, dc in boat_moves:
            next_state = (
                (m - dm, c - dc, 1) if side == 0
                else (m + dm, c + dc, 0)
            )
            nm, nc, _ = next_state

            if (dm + dc <= 2 and safe(nm, nc) and safe(3 - nm, 3 - nc)
                    and next_state not in visited):
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None


for step, (m, c, side) in enumerate(solve()):
    bank = "Left" if side == 0 else "Right"
    print(f"Step {step}: {m} missionaries, {c} cannibals on left; boat on {bank}")
