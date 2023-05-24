matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def transpose(matrix):
    # створити порожню матрицю розміру NxN
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    # транспонувати матрицю
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j][i] = matrix[i][j]

    return result

