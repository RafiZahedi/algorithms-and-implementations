from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1

            min_coin = float('inf')
            for i in range(len(coins)):
                res = dp(n - coins[i])
                if res != -1:
                    min_coin = min(min_coin, res + 1)

            memo[n] = min_coin
            return min_coin

        result = dp(amount)
        return result if result != float('inf') else -1


sol = Solution()
print(sol.coinChange(coins=[1, 2, 5], amount=11))  # -> 3
