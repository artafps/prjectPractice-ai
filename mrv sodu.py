def is_valid(board, row, col, num):
    # بررسی وجود عدد در سطر
    if num in board[row]:
        return False
    
    # بررسی وجود عدد در ستون
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # بررسی وجود عدد در بلوک 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty_location(board):
    # یافتن مکان خالی در صفحه
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    
    # اگر تمام مکان‌ها پر شده باشند، مسئله حل شده است
    if not empty_location:
        return True
    
    row, col = empty_location
    
    # امتحان کردن اعداد ممکن برای مکان خالی
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # با استفاده از روش MRV، اعداد ممکن برای مکان خالی مرتب شده و امتحان می‌شوند
            sorted_values = sorted(range(1, 10), key=lambda x: sum(1 for i in range(9) if is_valid(board, row, col, x)))
            
            # تلاش برای حل مسئله با اعداد مرتب شده
            if solve_sudoku(board):
                return True
            
            # اگر حل نشود، مقدار را به حالت اولیه باز می‌گردانیم
            board[row][col] = 0
    
    # اگر هیچ مقداری برای مکان خالی مناسب نبود، مسئله حل نمی‌شود
    return False

# مثال:
sudoku_board = [
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

if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")



