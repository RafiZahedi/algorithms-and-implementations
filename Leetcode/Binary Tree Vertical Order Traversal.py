from typing import List


class Solution:

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        res = 0
        n = len(word)
        right = n - 1

        for left in range(n - 1, -1, -1):

            for k in range(left, min(left + 10, right + 1)):
                if word[left:k + 1] in forbidden:
                    right = k - 1
                    break

            res = max(res, right - left + 1)

        return res


sol = Solution()
print(sol.longestValidSubstring('cbaaaabc', ["aaa", "cb"]))
