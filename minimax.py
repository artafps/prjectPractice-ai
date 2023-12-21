import sys

def print_board(board):
    for row in board:
        print(" ".join(row))

def is_winner(board, player):
    # بررسی برنده بودن یکی از بازیکنان
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # بررسی پر بودن صفحه
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if is_winner(board, 'X'):
        return scores['X'] - depth
    elif is_winner(board, 'O'):
        return scores['O'] + depth
    elif is_board_full(board):
        return scores['tie']

    if is_maximizing:
        max_eval = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = -sys.maxsize
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if is_winner(board, 'X'):
            print("X is the winner!")
            break
        elif is_winner(board, 'O'):
            print("O is the winner!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        if current_player == 'X':
            row, col = find_best_move(board)
            board[row][col] = 'X'
        else:
            print("Player O's turn.")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] != ' ':
                print("Cell already occupied. Try again.")
                continue
            board[row][col] = 'O'

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
