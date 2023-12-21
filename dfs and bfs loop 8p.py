class Puzzle8:
    def __init__(self, initial_state):
        # مقداردهی اولیه شیء Puzzle8 با وضعیت اولیه
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # وضعیت هدف که باید به آن برسیم
        self.size = 3  # اندازه یک طرف صفحه

    def display_state(self, state):
        # نمایش وضعیت صفحه
        for i in range(0, self.size ** 2, self.size):
            print(state[i:i + self.size])

    def find_blank(self, state):
        # یافتن موقعیت خانه‌ی خالی
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
            return None  # حرکت معتبر نیست

        return new_state

    def dfs(self, state, depth, path):
        # الگوریتم جستجوی عمقی
        if state == self.goal_state:
            print("Goal Reached!")
            print("Path:", path)
            return True

        if depth == 0:
            return False  # عمق به پایان رسیده و جواب پیدا نشده

        for direction in ["up", "down", "left", "right"]:
            new_state = self.move(state, direction)
            if new_state is not None and new_state not in path:
                if self.dfs(new_state, depth - 1, path + [new_state]):
                    return True  # جواب پیدا شده

        return False  # هیچ حرکت معتبری وجود ندارد

    def solve(self, max_depth=50):
        # حل مسئله با الگوریتم جستجوی عمقی
        if self.initial_state == self.goal_state:
            print("The puzzle is already solved!")
            return

        for depth in range(1, max_depth + 1):
            print(f"Searching at depth {depth}...")
            if self.dfs(self.initial_state, depth, [self.initial_state]):
                return  # جواب پیدا شده

        print("Solution not found within the specified depth limit.")


# Example Usage:
# مثال استفاده
initial_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]
puzzle = Puzzle8(initial_state)
puzzle.display_state(initial_state)
puzzle.solve()
