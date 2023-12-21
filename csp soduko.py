from constraint import Problem

def add_constraint(problem, cells):
    problem.addConstraint(lambda *args: len(set(args)) == len(args), cells)

def get_block(i, j):
    return [(i + m, j + n) for m in range(3) for n in range(3)]

def sudoku_solver(board):
    problem = Problem()

    # افزودن متغیرها به مسئله
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                problem.addVariable(f"{i}_{j}", range(1, 10))

    # افزودن محدودیت‌ها به مسئله
    for i in range(9):
        # محدودیت برای هر ستون
        add_constraint(problem, [f"{i}_{j}" for j in range(9)])

        # محدودیت برای هر ردیف
        add_constraint(problem, [f"{j}_{i}" for j in range(9)])

    # محدودیت‌های بلوک‌ها
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = get_block(i, j)
            add_constraint(problem, [f"{x}_{y}" for x, y in block])

    # حل مسئله
    solution = problem.getSolution()

    if solution:
        # ترکیب جواب با تخته اصلی
        for key, value in solution.items():
            i, j = map(int, key.split("_"))
            board[i][j] = value

    return board

# مثال استفاده:
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

solved_sudoku = sudoku_solver(sudoku_board)

# نمایش جواب
for row in solved_sudoku:
    print(row)
