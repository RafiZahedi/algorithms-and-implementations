from typing import List


# Main challenge: Solve in O(1) space

# The idea is to count the occurrence of one element as we iterate,
# whenever the count is zero we select a candidate, and then we check how many times
# we see it, if we saw the same number, we increase the count and if we didn't we decrease
# the count, again if the count is reached to zero we select a new candidate.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            # if the number we saw was the same as candidate increase the count
            # otherwise decrease it.
            count += 1 if candidate == num else -1

        return candidate


sol = Solution()
print(sol.majorityElement([3, 2, 3]))  # -> 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # -> 2
