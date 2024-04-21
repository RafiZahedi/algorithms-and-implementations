# 1035. Uncrossed Lines
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m_row = len(nums2)
        n_col = len(nums1)
        dp = [[0] * n_col for _ in range(m_row)]

        # base case for the first row and col
        dp[0][0] = 1 if nums2[0] == nums1[0] else 0

        # fill the first row
        for col in range(1, n_col):
            dp[0][col] = 1 if nums2[0] == nums1[col] else dp[0][col - 1]

        # fill the first col
        for row in range(1, m_row):
            dp[row][0] = 1 if nums1[0] == nums2[row] else dp[row - 1][0]

        for row in range(1, m_row):
            for col in range(1, n_col):
                # if two numbers match It's the up left diagonal
                if nums2[row] == nums1[col]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                # otherwise It's the max between left and right
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[-1][-1]


sol = Solution()
print(sol.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))  # -> 3
print(sol.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))  # -> 2
print(sol.maxUncrossedLines([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1]))  # -> 5
