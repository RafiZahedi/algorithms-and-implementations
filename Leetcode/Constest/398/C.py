from collections import Counter
from typing import List


class Solution:
    def diff(self, a, b):
        answer = 0
        for d1, d2 in zip(str(a), str(b)):
            answer += abs(int(d1) - int(d2))
        return answer

    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(str(nums[0]))  # Length of each number (assuming all are of the same length)
        # total_count = len(nums)

        # Initialize a list of Counter objects to count digit occurrences at each position
        number_of_digits = [Counter() for _ in range(n)]

        # Count digits at each position for all numbers
        for num in nums:
            str_num = str(num)
            for i in range(n):
                number_of_digits[i][str_num[i]] += 1

        answer = 0

        # Calculate the total digit differences
        for i in range(n):
            for d1 in number_of_digits[i]:
                count1 = number_of_digits[i][d1]
                for d2 in number_of_digits[i]:
                    if d1 != d2:  # Only if they are not equal maybe??
                        count2 = number_of_digits[i][d2]
                        answer += count1 * count2

        return answer // 2  # Divide by 2 to avoid double counting


sol = Solution()
print(sol.sumDigitDifferences(nums=[10, 10, 10, 10]))
print(sol.sumDigitDifferences(nums=[13, 23, 12]))
