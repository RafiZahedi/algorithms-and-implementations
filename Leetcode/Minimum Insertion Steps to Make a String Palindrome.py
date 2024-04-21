# 1312. Minimum Insertion Steps to Make a String Palindrome
class Solution:
    # Longest Palindromic Subsequence
    def lps(self, s1, s2):
        m_row = len(s1)
        n_col = len(s2)

        dp = [[0] * (m_row + 1) for _ in range(n_col + 1)]

        for row in range(1, m_row + 1):
            for col in range(1, n_col + 1):
                if s1[row - 1] == s2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]

    def minInsertions(self, s: str) -> int:
        if s[::-1] == s:
            return 0
        # we just need to fine the Longest Palindromic Subsequence of the
        # given string. then (length of the string - lps of s) is the answer
        length = self.lps(s, s[::-1])
        return len(s) - length


sol = Solution()
print(sol.minInsertions('zzazz'))  # -> 0
print(sol.minInsertions('mbadm'))  # -> 2
print(sol.minInsertions('leetcode'))  # -> 5
