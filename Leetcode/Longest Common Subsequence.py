# 1143. Longest Common Subsequence

def solve():
    text1 = "abcde"
    text2 = "ace"
    n = len(text1)
    m = len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if text1[row - 1] == text2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[-1][-1]


print(solve())
