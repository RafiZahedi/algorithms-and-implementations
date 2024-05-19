from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, n):
            if (i, n) in memo:
                return memo[(i, n)]
            if i >= len(coins) or n <= 0:
                return 1 if n == 0 else 0

            memo[(i, n)] = dp(i, n - coins[i], ) + dp(i + 1, n)
            return memo[(i, n)]

        return dp(0, amount)


sol = Solution()
print(sol.change(amount=5, coins=[1, 2, 5]))  # -> 4
print(sol.change(amount=12, coins=[1, 2, 4]))  # -> 16
