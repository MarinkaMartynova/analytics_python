# exercise 2
from fractions import Fraction

def input_fraction(prompt):
    # Получаем дробь в формате "a/b" и преобразуем в объект Fraction
    fraction_str = input(prompt)
    return Fraction(fraction_str)

def main():
    # Ввод двух дробей
    fraction1 = input_fraction("Введите первую дробь (a/b): ")
    fraction2 = input_fraction("Введите вторую дробь (a/b): ")
    
    # Вычисляем сумму и произведение
    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2
    
    # Выводим результаты
    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {product_result}")

if __name__ == "__main__":
    main()
