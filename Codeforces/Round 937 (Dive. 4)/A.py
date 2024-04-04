def solve(word1, word2):
    n_col = len(word1)
    m_row = len(word2)
    dp = [[0] * (n_col + 1) for _ in range(m_row + 1)]
    # fill the first column.
    for row in range(n_col + 1):
        dp[0][row] = row
    # fill the first row.
    for col in range(m_row + 1):
        dp[col][0] = col

    for row in range(1, m_row + 1):
        for col in range(1, n_col + 1):
            # if the words are equal, answer is the behind diagonal.
            if word2[row - 1] == word1[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                # otherwise it's the minimum of the three behind adjacent cells
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1

    return dp[m_row][n_col]


print(solve("AGGCTATCACCTGACCTCCAGGCCGATGCCC", "TAGCTATCACGACCGCGGTCGATTTGCCCGAC"))
print(solve("horse", "ros"))
