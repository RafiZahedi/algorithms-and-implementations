def solve():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    accept = False
    while not accept:
        accept = True
        for row in range(n):
            for col in range(m):
                res = 0
                flag = True
                if row > 0:
                    res = max(res, matrix[row - 1][col])
                if col > 0:
                    res = max(res, matrix[row][col - 1])
                if row < n - 1:
                    res = max(res, matrix[row + 1][col])
                if col < m - 1:
                    res = max(res, matrix[row][col + 1])

                if row > 0 and matrix[row][col] <= matrix[row - 1][col]:
                    flag = False
                if col > 0 and matrix[row][col] <= matrix[row][col - 1]:
                    flag = False
                if row < n - 1 and matrix[row][col] <= matrix[row + 1][col]:
                    flag = False
                if col < m - 1 and matrix[row][col] <= matrix[row][col + 1]:
                    flag = False

                if flag:
                    matrix[row][col] = res
                    accept = False

    for row in range(n):
        print(" ".join(map(str, matrix[row])))


for _ in range(int(input())):
    solve()
