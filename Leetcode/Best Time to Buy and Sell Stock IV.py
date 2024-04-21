# 188. Best Time to Buy and Sell Stock IV
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profit_after_buying = [float('-inf')] * (k + 1)
        profit_after_selling = [0] * (k + 1)

        for i in range(n):
            cur_price = prices[i]
            for j in range(k, 0, -1):
                profit_after_buying[j] = max(profit_after_buying[j], profit_after_selling[j - 1] - cur_price)
                profit_after_selling[j] = max(profit_after_selling[j], profit_after_buying[j] + cur_price)

        return profit_after_selling[k]


sol = Solution()
print(sol.maxProfit(2, [2, 4, 1]))  # -> 2
print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))  # -> 7
