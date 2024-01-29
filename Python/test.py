def minimum_cost_path(matrix: list[list]) -> int:
    # first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i-1]

    # first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i-1][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

    return matrix[-1][-1]

print(minimum_cost_path([[1, 10, 10], [1, 10, 1], [1, 100, 1]]))