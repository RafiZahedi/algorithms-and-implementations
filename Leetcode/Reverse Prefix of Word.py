# 2000. Reverse Prefix of Word
import collections


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        for i in range(len(word)):
            if word[i] == ch:
                # from the reverse index back to zero + reverse index + 1 all the way to last
                return word[i::-1] + word[i + 1:]

        return word


sol = Solution()
print(sol.reversePrefix('abcdefd', 'd'))  # -> dcbaefd
print(sol.reversePrefix('xyxzxe', 'z'))  # -> zxyxxe
print(sol.reversePrefix('abcd', 'z'))  # -> abcd
print(sol.reversePrefix('rzwuktxcjfpamlonbgyieqdvhs', 's'))  # -> shvdqeiygbnolmapfjcxtkuwzr

