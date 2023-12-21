import random
import math

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def calculate_cost(board):
    cost = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                for k in range(9):
                    if k != j and board[i][k] == board[i][j]:
                        cost += 1
                    if k != i and board[k][j] == board[i][j]:
                        cost += 1
                    r, c = 3 * (i // 3) + k // 3, 3 * (j // 3) + k % 3
                    if r != i and c != j and board[r][c] == board[i][j]:
                        cost += 1
    return cost

def copy_board(board):
    return [row.copy() for row in board]

def simulated_annealing(board, initial_temperature=1.0, cooling_rate=0.99, target_cost=0):
    current_board = copy_board(board)
    current_cost = calculate_cost(current_board)
    temperature = initial_temperature

    while current_cost > target_cost and temperature > 0.1:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while current_board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)

        original_value = current_board[row][col]
        new_value = random.randint(1, 9)

        while not is_valid(current_board, row, col, new_value):
            new_value = random.randint(1, 9)

        current_board[row][col] = new_value
        new_cost = calculate_cost(current_board)

        delta_cost = new_cost - current_cost

        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_cost = new_cost
        else:
            current_board[row][col] = original_value

        temperature *= cooling_rate

    return current_board

# مثال استفاده:
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_board = simulated_annealing(initial_board, initial_temperature=1.0, cooling_rate=0.95)
print("Solved Sudoku:")
for row in solved_board:
    print(row)
