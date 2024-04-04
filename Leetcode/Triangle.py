# 120. Triangle
def solve(triangle):
    m_row = len(triangle)
    # from the second last row, we find the minimum of each possible moves and go up.
    for row in range(m_row - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

print(solve([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # -> 11
print(solve([[-10]]))
