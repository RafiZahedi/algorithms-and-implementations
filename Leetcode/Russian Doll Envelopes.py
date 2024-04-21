# 354. Russian Doll Envelopes
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[0])
        n, count = len(envelopes), 0
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):

                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            count = max(count, dp[i])
        return count


sol = Solution()
print(sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))  # -> 3
