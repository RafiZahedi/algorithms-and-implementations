# 300. Longest Increasing Subsequence
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        answer = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            answer = max(answer, dp[i])
        return answer


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
