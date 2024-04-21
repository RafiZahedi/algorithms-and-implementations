# 1218. Longest Arithmetic Subsequence of Given Difference
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        count = 1
        for a in arr:
            before = dp.get(a - difference, 0)
            dp[a] = before + 1
            count = max(count, dp[a])
        return count


sol = Solution()
# print(sol.longestSubsequence([1, 2, 3, 4], 1))  # -> 4
# print(sol.longestSubsequence([1, 3, 5, 7], 1))  # -> 1
print(sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))  # -> 4
