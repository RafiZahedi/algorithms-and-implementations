# 516. Longest Palindromic Subsequence
class Solution:
    def palindrome(self, string):
        return string[::-1] == string

    def lcm(self, string1, string2):
        n = len(string1)
        m = len(string2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if string1[row - 1] == string2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]

    def solve(self, string):
        # if the string is already a palindrome. the length is the
        # longest common sub seq
        if self.palindrome(string):
            return len(string)
        # the answer is the lcm of the string and it's reverse.
        return self.lcm(string, string[::-1])


sol = Solution()
print(sol.solve('bbbab')) # -> 4
print(sol.solve('cbbd')) # -> 2
