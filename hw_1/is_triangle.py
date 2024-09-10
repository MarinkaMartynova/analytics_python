# exercise 1
print('Введите длины сторон треугольника: ')
a, b, c = float(input('a = ')), \
          float(input('b = ')), \
          float(input('c = '))

if a < b + c and \
        b < a + c and \
        c < a + b:
    print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')