# 1544. Make The String Great
class Solution:
    def is_pair(self, ch1, ch2):
        return ch1.lower() == ch2.lower() and ch1 != ch2

    def solve(self, s):
        stack = []
        for char in s:
            if len(stack) == 0 or not self.is_pair(char, stack[-1]):
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)


sol = Solution()

print(sol.solve('leEeetcode')) # -> 'leetcode'
print(sol.solve('abBAcC')) # -> '' (empty)