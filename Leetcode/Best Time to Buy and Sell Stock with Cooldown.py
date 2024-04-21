# 309. Best Time to Buy and Sell Stock with Cooldown
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def helper(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            cooldown = helper(i + 1, can_buy)
            if can_buy:
                buy = helper(i + 1, not can_buy) - prices[i]
                dp[(i, can_buy)] = max(buy, cooldown)
            else:
                sell = helper(i + 2, not can_buy) + prices[i]
                dp[(i, can_buy)] = max(sell, cooldown)
            return dp[(i, can_buy)]

        return helper(0, True)


sol = Solution()
print(sol.maxProfit([1, 2, 3, 0, 2])) # -> 3
