# 96. Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        if n == 2:
            return 2
        dp = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                left = root - 1
                right = node - root
                total += dp[left] * dp[right]
            dp[node] = total
        return dp[n]


sol = Solution()
print(sol.numTrees(3))  # -> 5
print(sol.numTrees(1))  # -> 1
print(sol.numTrees(14))  # -> 267440
