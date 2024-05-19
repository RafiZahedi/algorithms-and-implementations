from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        differences = [nums1[i] - nums2[i] for i in range(n)]
        # if we sort the differences we don't ruin the indices of tow arrays
        differences.sort()
        count = 0
        # and then we use two pointers
        left, right = 0, n - 1

        while left != right:
            if differences[left] + differences[right] > 0:  # if so, from the left to the right will make valid paris
                count += right - left
                # shrink the window from the right side
                right -= 1
            else:
                # otherwise check the next pair
                left += 1

        return count


sol = Solution()
print(sol.countPairs([2, 1, 2, 1], [1, 2, 1, 2]))  # -> 1
# The pairs satisfying the condition are:
# - (0, 2) where 2 + 2 > 1 + 1.
print(sol.countPairs([1, 10, 6, 2], [1, 4, 1, 5]))  # -> 5
# The pairs satisfying the condition are:
# - (0, 1) where 1 + 10 > 1 + 4.
# - (0, 2) where 1 + 6 > 1 + 1.
# - (1, 2) where 10 + 6 > 4 + 1.
# - (1, 3) where 10 + 2 > 4 + 5.
# - (2, 3) where 6 + 2 > 1 + 5.
print(sol.countPairs([5, 1, 1, 15, 3, 14, 19, 1, 9, 12, 6, 8, 2, 4, 19, 17, 19, 5],
                     [1, 16, 5, 3, 7, 9, 19, 3, 7, 2, 13, 4, 4, 17, 13, 12, 19, 16]))
