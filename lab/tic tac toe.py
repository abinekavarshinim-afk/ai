# Tic Tac Toe Game

board = [' ' for i in range(9)]

def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for pos in winning_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

# Main game
player = 'X'

while True:
    display_board()

    move = int(input("Player " + player + ", enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move! Try again.")
        continue

    board[move] = player

    if check_winner(player):
        display_board()
        print("Player", player, "wins!")
        break

    if ' ' not in board:
        display_board()
        print("Game is a Draw!")
        break

    player = 'O' if player == 'X' else 'X'
