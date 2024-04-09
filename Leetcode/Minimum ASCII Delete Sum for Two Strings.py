# 712. Minimum ASCII Delete Sum for Two Strings
class Solution:
    def solve(self, s1, s2):
        m_row = len(s1)
        n_col = len(s2)

        dp = [[0] * (n_col + 1) for _ in range(m_row + 1)]

        # fill the first row
        for col in range(1, n_col + 1):
            dp[0][col] = ord(s2[col - 1]) + dp[0][col-1]

        # fil the first col
        for row in range(1, m_row + 1):
            dp[row][0] = ord(s1[row - 1]) + dp[row - 1][0]

        for row in range(1, m_row + 1):
            for col in range(1, n_col + 1):

                # if two characters are the same it's the up left diagonal
                if s1[row - 1] == s2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    # otherwise it's the minimum between (dp[up] + left char, or dp[left] + up char)
                    dp[row][col] = min(
                        dp[row - 1][col] + ord(s1[row - 1]),
                        dp[row][col - 1] + ord(s2[col - 1]))

        return dp[-1][-1]


sol = Solution()
print(sol.solve('sea', 'eat'))
print(sol.solve('leet', 'delete'))
