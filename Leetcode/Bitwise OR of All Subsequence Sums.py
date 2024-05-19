from typing import List


class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        result = 0
        prefix_sum = 0

        for num in nums:
            # Update the cumulative sum by adding the current element
            prefix_sum += num
            # Update the result by performing bitwise OR with the current element and the cumulative sum
            result |= num | prefix_sum

        return result


sol = Solution()
print(sol.subsequenceSumOr([2, 1, 0, 3]))  # -> 7

