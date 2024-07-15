def solve():
    grid = [[1, 2, 9, 10, 25],
            [4, 3, 8, 11, 24],
            [5, 6, 7, 12, 23],
            [16, 15, 14, 13, 22],
            [17, 18, 19, 20, 21]]
    row, col = map(int, input().split())

    return grid[row - 1][col - 1]


for _ in range(int(input())):
    print(solve())
