# 931. Minimum Falling Path Sum
def solve(matrix):
    m_row = len(matrix)
    n_col = len(matrix[0])

    for row in range(1, m_row):
        for col in range(n_col):
            if col == 0:
                # up and right diagonal
                matrix[row][col] += min(matrix[row - 1][col], matrix[row - 1][col + 1])
            elif col == n_col - 1:
                # up and left diagonal
                matrix[row][col] += min(matrix[row - 1][col], matrix[row - 1][col - 1])
            else:
                matrix[row][col] += min(matrix[row - 1][col], matrix[row - 1][col + 1], matrix[row][col - 1])
    return min(matrix[-1])

print(solve([[2, 1, 3], [6, 5, 4], [7, 8, 9], [1, 2, 5]]))
