import heapq

class Puzzle8:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1,2,3,4,0,5,6,7,8]
        self.size = 3

    def display_state(self, state):
        for i in range(0, self.size ** 2, self.size):
            print(state[i:i + self.size])

    def find_blank(self, state):
        return state.index(0)

    def move(self, state, direction):
        blank_index = self.find_blank(state)
        # ایجاد یک تاپل جدید با استفاده از انتساب مقدارهای جدید به تاپل موجود
        new_state = list(state)
        
        if direction == "up" and blank_index >= self.size:
            new_state[blank_index], new_state[blank_index - self.size] = new_state[blank_index - self.size], new_state[blank_index]
        elif direction == "down" and blank_index < self.size * (self.size - 1):
            new_state[blank_index], new_state[blank_index + self.size] = new_state[blank_index + self.size], new_state[blank_index]
        elif direction == "left" and blank_index % self.size != 0:
            new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        elif direction == "right" and (blank_index + 1) % self.size != 0:
            new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]

        return tuple(new_state)

    def heuristic(self, state):
        # تابع هیوریستیک بر اساس فاصله منهتن یا تعداد خانه‌های اشتباه
        return sum(abs(i % self.size - j % self.size) + abs(i // self.size - j // self.size) for i, j in zip(state, self.goal_state) if i != 0)

    def a_star(self):
        start_node = (self.heuristic(self.initial_state), 0, tuple(self.initial_state))
        priority_queue = [start_node]
        visited = set()

        while priority_queue:
            _, cost, current_state = heapq.heappop(priority_queue)

            if current_state == tuple(self.goal_state):
                print("Goal Reached!")
                return

            if current_state in visited:
                continue

            visited.add(current_state)

            blank_index = self.find_blank(current_state)
            for direction in ["up", "down", "left", "right"]:
                new_state = self.move(current_state, direction)
                if new_state != current_state:
                    new_cost = cost + 1
                    priority = new_cost + self.heuristic(new_state)
                    heapq.heappush(priority_queue, (priority, new_cost, new_state))

    def solve(self):
        if self.initial_state == self.goal_state:
            print("The puzzle is already solved!")
            return

        print("Searching with A* algorithm based on Manhattan Distance...")
        self.a_star()

# Example Usage:
initial_state = [1, 2, 3, 4, 5, 0, 7, 8, 6]
puzzle = Puzzle8(initial_state)
puzzle.display_state(initial_state)
puzzle.solve()
