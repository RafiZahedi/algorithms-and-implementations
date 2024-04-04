# 63. Unique Paths II
def solve(grid):
    m_row = len(grid)
    n_col = len(grid[0])
    if grid[0][0] == 1:
        return 0

    # Number of ways to cell 0
    grid[0][0] = 1

    # Fill the first column
    for col in range(1, m_row):
        grid[col][0] = int(grid[col][0] == 0 and grid[col - 1][0] == 1)

    # Fill the first row
    for row in range(1, n_col):
        grid[0][row] = int(grid[0][row] == 0 and grid[0][row - 1] == 1)

    for col in range(1, m_row):
        for row in range(1, n_col):
            if grid[col][row] == 0:
                grid[col][row] = grid[col - 1][row] + grid[col][row - 1]
            else:
                grid[col][row] = 0

    return grid[-1][-1]


# print(solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# print(solve([[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]))
print(solve([[0]]))
# print(solve([[1]]))
# print(solve([[0, 1]]))
