def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Macierz nie jest kwadratowa")

    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for k in range(len(matrix)):
        wspolczynnik = matrix[0][k] * ((-1) ** k)
        podwyznacznik = [row[:k] + row[k + 1:] for row in (matrix[1:])]

        det += wspolczynnik * determinant(podwyznacznik)

    return det


matrix = [[1, 2, 3],
          [6, 5, 4],
          [3, 7, 2]
          ]

print(determinant(matrix))
