# 673. Number of Longest Increasing Subsequence
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_lis = max(length)
        result = 0
        for i in range(len(nums)):
            if length[i] == max_lis:
                result += count[i]
        return result


sol = Solution()
print(sol.findNumberOfLIS([1, 3, 5, 4, 7]))
