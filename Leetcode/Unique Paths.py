# 62. Unique Paths
def solve():
    m = 3
    n = 7
    # output: 28
    dp = [[1] * n for _ in range(m)]
    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    return dp[-1][-1]


print(solve())
