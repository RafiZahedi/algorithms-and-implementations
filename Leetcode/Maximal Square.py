# 221. Maximal Square
def solve(matrix):
    m_row = len(matrix)
    n_col = len(matrix[0])
    # convert it int matrix ( goooosh )
    has_one = False
    for row in range(m_row):
        for col in range(n_col):
            matrix[row][col] = int(matrix[row][col])
            if matrix[row][col]:
                has_one = True
    if not has_one:
        return 0
    answer = 1
    for row in range(1, m_row):
        for col in range(1, n_col):
            # if square has 0 just continue
            if not matrix[row][col] or not matrix[row - 1][col] or not matrix[row][col - 1] \
                    or not matrix[row - 1][col - 1]:
                continue

            matrix[row][col] = min(matrix[row - 1][col], matrix[row][col - 1], matrix[row - 1][col - 1]) + 1
            answer = max(answer, matrix[row][col])

    return answer ** 2


print(
    solve([["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "0", "1", "0"]
           ]))
print(solve([["1", "1", "1", "1", "0"]]))
print(solve([["0"]]))
