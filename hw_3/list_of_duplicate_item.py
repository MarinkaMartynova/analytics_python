# exercise 2
def find_duplicates(list):
    duplicates = []
    seen = set()
    
    for item in list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    
    return duplicates

# Пример использования
list = [1, 2, 3, 2, 4, 3, 5, 2, 5, 7, 8, 9, 10, 10]
result = find_duplicates(list)
print(result)

