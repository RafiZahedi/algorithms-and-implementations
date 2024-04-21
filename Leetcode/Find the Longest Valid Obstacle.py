# 1964. Find the Longest Valid Obstacle Course at Each Position
from bisect import bisect_right
from typing import List


# Similar to LIS but will face TLE, so we use Binary Search instead

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [1] * n
        # lis[i] records the lowest increasing sequence of length i + 1.
        lis = []

        for i, height in enumerate(obstacles):
            # Find the rightmost position to insert the current height in the lis list
            idx = bisect_right(lis, height)

            # If the position is equal to the current length of lis, append the height
            # current obstacle is greater than all previous heights
            if idx == len(lis):
                lis.append(height)
            # Otherwise, update the element at position idx with the current height
            # already an element greater than, maintain increasing order
            else:
                lis[idx] = height

            # Update the output array with the length of the longest obstacle course at the current position
            dp[i] = idx + 1

        return dp


sol = Solution()
print(sol.longestObstacleCourseAtEachPosition([1, 2, 3, 2]))
