# 115. Distinct Subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m_row = len(t)
        n_col = len(s)

        dp = [[0] * n_col for _ in range(m_row)]
        # base case
        dp[0][0] = 0 if s[0] != t[0] else 1
        # fill the first row
        for col in range(1, n_col):
            if t[0] == s[col]:
                dp[0][col] = dp[0][col - 1] + 1
            else:
                dp[0][col] = dp[0][col - 1]

        for row in range(1, m_row):
            for col in range(1, n_col):
                # if equal then up left diagonal and left
                if s[col] == t[row]:
                    dp[row][col] = dp[row-1][col-1] + dp[row][col-1]
                # else just left
                else:
                    dp[row][col] = dp[row][col-1]
        # for row in dp:
        #     print(row)
        return dp[-1][-1]

sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit")) # -> 3
print(sol.numDistinct("babgbag", "bag")) # -> 5