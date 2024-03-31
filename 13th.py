import math

# Define the constants for players
EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

# Define the evaluation function for the game
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 1 if board[i][0] == PLAYER_X else -1
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 1 if board[0][i] == PLAYER_X else -1
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 1 if board[0][0] == PLAYER_X else -1
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 1 if board[0][2] == PLAYER_X else -1

    # If no winner, return 0 for a tie or None for an unfinished game
    return 0 if all(cell != EMPTY for row in board for cell in row) else None

# Implement the Minimax algorithm
def minimax(board, depth, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using Minimax
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            row, col = find_best_move(board)
            print(f"Player X moves to row {row}, column {col}")
        else:
            row = int(input(f"Player O, enter row (0, 1, 2): "))
            col = int(input(f"Player O, enter column (0, 1, 2): "))

        if board[row][col] != EMPTY:
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = current_player

        result = evaluate(board)
        if result == 1:
            print_board(board)
            print("Player X wins!")
            break
        elif result == -1:
            print_board(board)
            print("Player O wins!")
            break
        elif result == 0:
            print_board(board)
            print("It's a tie!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

# Start the game
play_game()



