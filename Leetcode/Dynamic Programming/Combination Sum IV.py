from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            if n >= target:
                return 1 if n == target else 0
            total = 0
            for num in nums:
                total += dp(n + num)
            memo[n] = total
            return memo[n]

        return dp(0)


sol = Solution()
print(sol.combinationSum4([1, 2, 3], 4))  # -> 7
