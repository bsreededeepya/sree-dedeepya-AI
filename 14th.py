# Function to evaluate the game state
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return 1 if board[i][0] == 'X' else -1
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return 1 if board[0][i] == 'X' else -1
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 1 if board[0][0] == 'X' else -1
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 1 if board[0][2] == 'X' else -1
    # Check for a draw
    if all(cell != ' ' for row in board for cell in row):
        return 0
    # Game is still ongoing
    return None

# Function to implement the Alpha-Beta Pruning algorithm
def alphabeta(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score is not None:
        return score

    if is_maximizing:
        max_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    max_score = max(max_score, alphabeta(board, depth + 1, alpha, beta, False))
                    board[i][j] = ' '
                    alpha = max(alpha, max_score)
                    if beta <= alpha:
                        break
        return max_score
    else:
        min_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    min_score = min(min_score, alphabeta(board, depth + 1, alpha, beta, True))
                    board[i][j] = ' '
                    beta = min(beta, min_score)
                    if beta <= alpha:
                        break
        return min_score

# Function to find the best move using Alpha-Beta Pruning
def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = alphabeta(board, 0, alpha, beta, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Initial Board:")
    print_board(board)
    while True:
        # Player's move
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if board[row][col] != ' ':
            print("Cell already occupied. Try again.")
            continue
        board[row][col] = 'O'
        print("Player's Move:")
        print_board(board)
        if evaluate(board) is not None:
            break

        # Computer's move
        row, col = find_best_move(board)
        board[row][col] = 'X'
        print("Computer's Move:")
        print_board(board)
        if evaluate(board) is not None:
            break

# Start the game
play_game()



