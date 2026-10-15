def solve(row=0, columns=set(), diag1=set(), diag2=set(), board=[]):
    if row == 8:
        return board

    for col in range(8):
        if col not in columns and row - col not in diag1 and row + col not in diag2:
            result = solve(
                row + 1,
                columns | {col},
                diag1 | {row - col},
                diag2 | {row + col},
                board + [col],
            )
            if result:
                return result


solution = solve()

for col in solution:
    print("." * col + "Q" + "." * (7 - col))
