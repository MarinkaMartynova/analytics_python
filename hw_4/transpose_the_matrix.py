# exercise 1
def transpose_matrix(matrix):
    # Используем функцию zip() для транспонирования
    return [list(row) for row in zip(*matrix)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
