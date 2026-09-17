import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != EMPTY:
            return board[condition[0]]
    if EMPTY not in board:
        return 'Tie'
    return None

def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if winner == 'Tie':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval_score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval_score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval

def get_best_move(board):
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe vs Unbeatable AI!")
    print("Positions are numbered 1-9 starting from top-left to bottom-right.")
    print_board([str(i+1) for i in range(9)])

    while True:
        # Human Move
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == EMPTY:
                    board[move] = HUMAN
                    break
                print("Invalid move! Cell is already taken or out of range.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        print_board(board)
        result = check_winner(board)
        if result:
            break

        # AI Move
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move] = AI
        print_board(board)
        
        result = check_winner(board)
        if result:
            break

    if result == 'Tie':
        print("It's a Tie!")
    elif result == HUMAN:
        print("You won!")
    else:
        print("AI Wins!")

if __name__ == "__main__":
    play_game()
