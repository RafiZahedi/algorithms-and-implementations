# 42. Trapping Rain Water
from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        # precalculating the right max element for each item,
        # so we don't need to find the right max element each time
        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        count = 0
        left_max = height[0]
        for i in range(1, n):

            # main calculation
            water = (min(left_max, right_max[i])) - height[i]
            if water >= 0:
                count += water

            # we update the left max each time for the next calculation.
            left_max = max(left_max, height[i])
        return count


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # -> 6
print(sol.trap([4, 2, 0, 3, 2, 5]))  # -> 9
