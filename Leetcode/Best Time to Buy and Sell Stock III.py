# 123. Best Time to Buy and Sell Stock III

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_price = prices[-1]  # Initialize max_price with the last price
        dp = [0] * n  # Initialize a dynamic programming table

        # Backward pass to calculate maximum profit if selling on or after day i
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            dp[i] = max(dp[i + 1], max_price - prices[i])

        min_price = prices[0]  # Initialize min_price with the first price
        # Forward pass to calculate maximum profit if buying on or before day i and selling on or after day i
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], dp[i] + (prices[i] - min_price))

        return dp[-1]


sol = Solution()
print(sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # -> 6
print(sol.maxProfit([1, 2, 3, 4, 5]))  # -> 4
