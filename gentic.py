import random

def initialize_population(size, board):
    # تولید جمعیت اولیه
    population = []
    for _ in range(size):
        individual = []
        for i in range(9):
            row = board[i]
            random.shuffle(row)
            individual.extend(row)
        population.append(individual)
    return population

def fitness(board):
    # تابع هدف - ارزیابی امتیاز هر فرد
    # می‌توانید یک تابع ارزیابی سودوکو ایجاد کنید که امتیاز بر اساس صحت سودوکو حساب شود.
    pass

def crossover(parent1, parent2):
    # عملیات ترکیب والدین
    crossover_point = random.randint(1, 8)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual):
    # عملیات جهش
    mutation_point = random.randint(0, 80)
    new_value = random.randint(1, 9)
    individual[mutation_point] = new_value
    return individual

def genetic_algorithm(board, population_size=100, generations=1000):
    population = initialize_population(population_size, board)

    for generation in range(generations):
        # ارزیابی امتیاز هر فرد
        scores = [(individual, fitness(individual)) for individual in population]

        # انتخاب والدین
        parents = [individual for individual, _ in scores[:int(population_size/2)]]

        # تولید نسل جدید
        new_generation = parents.copy()

        while len(new_generation) < population_size:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # احتمال جهش
                child = mutate(child)
            new_generation.append(child)

        population = new_generation

        # چاپ بهترین امتیاز در هر نسل (اختیاری)
        best_individual, best_score = max(scores, key=lambda x: x[1])
        print(f"Generation {generation + 1}, Best Score: {best_score}")

        # اگر به حل رسیده باشیم
        if best_score == 0:
            print("Solution Found!")
            break

    return best_individual

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

solution = genetic_algorithm(initial_board)
print("Solution:")
for i in range(0, len(solution), 9):
    print(solution[i:i+9])
