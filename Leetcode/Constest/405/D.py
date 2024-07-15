from typing import List


class Solution:
    def is_valid(self, s):
        for i in range(len(s) - 1):
            if s[i] == '0' and s[i + 1] == '0':
                return False
        return True

    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        mp = {}
        for index, word in enumerate(words):
            mp[word] = min(mp.get(word, float('inf')), costs[index])

        dp = [float('inf')] * (n + 1)
        # starts from zero
        dp[0] = 0
        for i in range(1, n + 1):
            for word in mp:
                # if 'i' passed the len of the word
                if i >= len(word) and target[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)] + mp[word])

        # if we have the last value then that is the answer
        if dp[n] != float('inf'):
            return dp[n]
        # otherwise no answer
        return -1


sol = Solution()
print(sol.minimumCost(target="abcdef", words=["abdef", "abc", "d", "def", "ef"], costs=[100, 1, 1, 10, 5]))  # -> 7
