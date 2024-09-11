# exercise 1
HEX_FACTOR = 16
def int_to_hex(n):
    # Список символов для шестнадцатеричной системы
    hex_digits = '0123456789abcdef'
        
    if n < 16:
        return hex_digits[n]
    
    # Рекурсивное деление числа на 16
    return int_to_hex(n // HEX_FACTOR) + hex_digits[n % HEX_FACTOR]

# Основной код с проверкой на ввод
try:
    # Получаем число от пользователя
    user_input = input("Введите целое число: ")
    
    # Пробуем преобразовать строку в целое число
    num = int(user_input)
    
    # Проверка на отрицательное число
    if num < 0:
        custom_hex = '-' + int_to_hex(-num)  
    else:
        custom_hex = int_to_hex(num)
    
    # Преобразование с использованием встроенной функции hex
    builtin_hex = hex(num)

    print(f"Результат своей функции: {custom_hex}")
    print(f"Результат встроенной функции hex: {builtin_hex}")

except ValueError:    
    print("Ошибка: введено не число. Пожалуйста, введите целое число.")
