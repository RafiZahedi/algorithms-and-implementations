from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        extras = set()
        answer = 0
        
        for num in nums:
            # if this is a positive, and we have its negative
            # in the set, It's a valid one, so we take max
            if num > 0 and -num in extras:
                answer = max(answer, num)
            # if this is a negative, and we have its positive
            # in the set, It's a valid one, so we take max
            elif num < 0 and (num * -1) in extras:
                answer = max(answer, (num * -1))
            # otherwise just add this number to the set
            extras.add(num)
        # either we updated the answer and found something
        # or we didn't and return -1
        return answer or -1


sol = Solution()
print(sol.findMaxK([-1, 2, -3, 3]))         # ->  3
print(sol.findMaxK([-1, 10, 6, 7, -7, 1]))  # ->  7
print(sol.findMaxK([-10, 8, 3, 7, -2, -3])) # -> -3
print(sol.findMaxK([10, 8, 6, 7, -2, 10]))  # -> -1
