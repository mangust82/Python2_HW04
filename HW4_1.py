# 1. Напишите функцию для транспонирования матрицы

def transponir(matrix: list[list[int]]) -> list[list[int]]:
    """Func will transpose matrix"""
    tr_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < 1:
                a = []
                tr_matrix.append(a)
            tr_matrix[j].append(matrix[i][j])
    return tr_matrix

def print_m(matrix: list[list[int]]) -> None:
    for string in matrix:
        print(string)
    print()

matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [0, 0, 0]]

print(f'Транспонированная матрица в строку: {transponir(matrix)}')
print('Исходная матрица')
print_m(matrix)
print('Транспонированная матрица')
print_m(transponir(matrix))
