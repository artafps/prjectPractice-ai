def filter_values(board, row, col):
    possible_values = set(range(1, 10))

    # فیلترینگ بر اساس سطر
    possible_values -= set(board[row])

    # فیلترینگ بر اساس ستون
    possible_values -= set(board[i][col] for i in range(9))


    # فیلترینگ بر اساس بلوک 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    possible_values -= set(board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3))

    return list(possible_values)

def mrv(board):
    # یافتن خانه خالی با کمترین انتخاب‌های ممکن
    empty_locations = [(i, j, filter_values(board, i, j)) for i in range(9) for j in range(9) if board[i][j] == 0]
    empty_locations.sort(key=lambda x: len(x[2]))
    return empty_locations

def is_valid(board, row, col, num):
    # بررسی وجود عدد در سطر، ستون و بلوک
    return num not in board[row] and num not in [board[i][col] for i in range(9)] and num not in [board[i][j] for i in range(3 * (row // 3), 3 * (row // 3) + 3) for j in range(3 * (col // 3), 3 * (col // 3) + 3)]

def find_empty_location(board):
    # یافتن یک خانه خالی با کمترین انتخاب‌های ممکن
    empty_locations = mrv(board)
    return empty_locations[0] if empty_locations else None

def sudoku_solver(board):
    empty_location = find_empty_location(board)

    # اگر هیچ خانه‌ای خالی نباشد، مسئله حل شده است
    if not empty_location:
        return True

    row, col, possible_values = empty_location

    # امتحان کردن اعداد ممکن
    for num in possible_values:
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
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]

if sudoku_solver(sudoku_board):
    # نمایش جواب
    for row in sudoku_board:
        print(row)
else:
    print("مسئله حل‌ناپذیر است.")
