# exercise 4
import random
from itertools import combinations

# Словарь с вещами и их массой
items = {
    "палатка": 3,
    "спальник": 2,
    "еда": 5,
    "вода": 4,
    "фонарь": 1,
    "аптечка": 1,
    "карта": 0.1,
    "одежда": 2
}

# Максимальная грузоподъёмность рюкзака
max_weight = 10

# Функция для нахождения всех возможных вариантов
def find_all_variants(items, max_weight):
    valid_combinations = []
    for r in range(1, len(items) + 1):
        for combo in combinations(items.keys(), r):
            total_weight = sum(items.get(item, 0) for item in combo)
            if total_weight <= max_weight:
                valid_combinations.append((combo, total_weight))
    return valid_combinations

# Поиск всех возможных вариантов
all_variants = find_all_variants(items, max_weight)

# Проверяем, что есть допустимые варианты
if all_variants:
    # Вывод случайного допустимого варианта
    random_variant = random.choice(all_variants)
    print("Случайный допустимый вариант:")
    print(f"Вещи: {random_variant[0]} с общей массой: {random_variant[1]} кг")
else:
    print("Нет допустимых вариантов.")

# * Вывод всех возможных вариантов
print("\nВсе возможные варианты комплектации рюкзака:")
for combo, total_weight in all_variants:
    print(f"Вещи: {combo} с общей массой: {total_weight} кг")



