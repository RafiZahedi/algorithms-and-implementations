# 64. Minimum Path Sum
def solve(grid):
    m_row = len(grid)
    n_col = len(grid[0])
    # fill the first row
    for col in range(1, n_col):
        grid[0][col] += grid[0][col - 1]

    # fill the first col
    for row in range(1, m_row):
        grid[row][0] += grid[row - 1][0]
    for row in range(1, m_row):
        for col in range(1, n_col):
            grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

    return grid[-1][-1]


print(solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # -> 7
print(solve([[1, 2, 3], [4, 5, 6]]))  # -> 12
print(solve([[1], [1], [4]]))  # -> 6
