def is_valid(board, row, col, num):
    # بررسی وجود عدد در سطر
    if num in board[row]:
        return False

    # بررسی وجود عدد در ستون
    if num in [board[i][col] for i in range(9)]:
        return False

    # بررسی وجود عدد در بلوک 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in [board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]:
        return False

    return True

def find_empty_location(board):
    # یافتن یک خانه خالی در تخته سودوکو
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def sudoku_solver(board):
    empty_location = find_empty_location(board)

    # اگر هیچ خانه‌ای خالی نباشد، مسئله حل شده است
    if not empty_location:
        return True

    row, col = empty_location

    # امتحان کردن اعداد از 1 تا 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # اگر عدد مورد نظر درست باشد، آن را در خانه قرار داده و بازگشت به تابع برای ادامه حل مسئله
            board[row][col] = num

            if sudoku_solver(board):
                return True  # حل موفقیت‌آمیز

            # اگر حل نشد، عدد را از خانه حذف و به انتخاب عدد بعدی می‌پردازیم
            board[row][col] = 0

    return False  # هیچ عددی مناسب پیدا نشد

# مثال استفاده:
sudoku_board = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if sudoku_solver(sudoku_board):
    # نمایش جواب
    for row in sudoku_board:
        print(row)
else:
    print("مسئله حل‌ناپذیر است.")
