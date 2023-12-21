class Puzzle8:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.size = 3

    def display_state(self, state):
        # نمایش وضعیت فعلی صفحه
        for i in range(0, self.size ** 2, self.size):
            print(state[i:i + self.size])

    def find_blank(self, state):
        # یافتن مکان خانه‌ی خالی (صفر) در وضعیت فعلی
        return state.index(0)

    def move(self, state, direction):
        # انجام یک حرکت به اتفاق یک جهت مشخص
        blank_index = self.find_blank(state)
        new_state = state.copy()

        if direction == "up" and blank_index >= self.size:
            new_state[blank_index], new_state[blank_index - self.size] = new_state[blank_index - self.size], new_state[
                blank_index]
        elif direction == "down" and blank_index < self.size * (self.size - 1):
            new_state[blank_index], new_state[blank_index + self.size] = new_state[blank_index + self.size], new_state[
                blank_index]
        elif direction == "left" and blank_index % self.size != 0:
            new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        elif direction == "right" and (blank_index + 1) % self.size != 0:
            new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        else:
            return None

        return new_state

    def is_goal(self, state):
        # بررسی آیا وضعیت فعلی برابر با وضعیت هدف است
        return state == self.goal_state

    def is_valid_move(self, state, direction):
        # بررسی اعتبار یک حرکت
        new_state = self.move(state, direction)
        return new_state is not None

    def heuristic_mrv(self, state):
        # تابع هیوریستیک بر اساس تعداد خانه‌های خالی در حالت فعلی
        return state.count(0)

    def dfs_mrv(self, state, depth, path):
        # الگوریتم DFS با استفاده از تابع هیوریستیک MRV
        if self.is_goal(state):
            print("Goal Reached!")
            print("Path:", path)
            return True

        if depth == 0:
            return False

        # انتخاب حرکت‌های معتبر و مرتب‌سازی بر اساس تابع هیوریستیک MRV
        valid_moves = [dir for dir in ["up", "down", "left", "right"] if self.is_valid_move(state, dir)]
        sorted_moves = sorted(valid_moves, key=lambda x: self.heuristic_mrv(self.move(state, x)))

        for direction in sorted_moves:
            new_state = self.move(state, direction)
            if new_state not in path:
                # فراخوانی بازگشتی با حرکت جدید
                if self.dfs_mrv(new_state, depth - 1, path + [new_state]):
                    return True

        return False

    def solve_mrv(self, max_depth=50):
        # حل مسئله با الگوریتم DFS و تابع هیوریستیک MRV
        if self.initial_state == self.goal_state:
            print("The puzzle is already solved!")
            return

        for depth in range(1, max_depth + 1):
            print(f"Searching at depth {depth}...")
            if self.dfs_mrv(self.initial_state, depth, [self.initial_state]):
                return

        print("Solution not found within the specified depth limit.")


# مثال:
initial_state_8puzzle = [1, 2, 3, 4, 0, 5, 7, 8, 6]
puzzle_8 = Puzzle8(initial_state_8puzzle)
puzzle_8.display_state(initial_state_8puzzle)
puzzle_8.solve_mrv()
