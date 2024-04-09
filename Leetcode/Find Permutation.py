# 484. Find Permutation
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        result = []
        s += 'I'
        for i in range(len(s)):
            stack.append(i+1)

            if s[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return result

obj = Solution()
print(obj.findPermutation('DIDII')) # -> [2, 1, 4, 3, 5, 6]
# print(obj.findPermutation('I')) # -> [1, 2]
# print(obj.findPermutation('DDD')) # -> [4, 3, 2, 1]
