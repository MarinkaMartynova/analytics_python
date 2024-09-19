# exercise 2
names = ['str', 'int', 'bool', 'None', 'float', 'list', 'tuple', 'set']
vals = ['abc', 10, True, None, 3.14, [1, 2, 3], (1, 2, 3), {1, 2, 3}]

def create_dict_from_lists(names, vals):
    result = {}
    for name, value in zip(names, vals):
        try:
            # Пробуем использовать значение как ключ
            result[value] = name
        except TypeError:
            # Если значение не хешируемо, используем его строковое представление
            result[str(value)] = name
    return result

# Пример использования
result_dict = create_dict_from_lists(names, vals)

print(result_dict)
