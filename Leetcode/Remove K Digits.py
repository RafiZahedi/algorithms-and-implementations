# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k:
            stack.pop()
            k -= 1

        result = ''.join(stack)
        result = result.lstrip('0')
        return result if result else '0'


sol = Solution()
print(sol.removeKdigits('1432219', 3))  # -> 1219
print(sol.removeKdigits('10200', 1))  # -> 200
print(sol.removeKdigits('10', 2))  # -> 0
