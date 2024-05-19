# 881. Boats to Save People
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # base case: if after sorting, the first person has a weight equal to the limit
        # means that all the people need a boat.
        if people[0] == limit:
            return len(people)

        n = len(people)
        left = 0
        right = n - 1
        count = 0
        reduced = 0  # to keep track of the people who got a boat

        # people with weight equal to limit will definitely take one boat
        # so shrink down the window from right until the weight is less than limit
        while right >= left and people[right] == limit:
            right -= 1
            count += 1
            reduced += 1

        while left < right:
            pair = people[left] + people[right]
            if pair <= limit:
                reduced += 2
                count += 1
                right -= 1
                left += 1
                continue

            if pair > limit:  # if above the limit, then moving the right pointer guaranties the limit to be lower
                right -= 1

        count += n - reduced # all the people who didn't receive a boat
        return count


sol = Solution()
print(sol.numRescueBoats([1, 2], 3))  # ->  1
print(sol.numRescueBoats([3, 2, 2, 1], 3))  # -> 3
print(sol.numRescueBoats([3, 5, 3, 4], 5))  # -> 4
print(sol.numRescueBoats([1, 2, 4, 6, 7], 9))  # -> 3
