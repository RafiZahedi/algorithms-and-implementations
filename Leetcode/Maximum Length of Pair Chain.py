# 646. Maximum Length of Pair Chain
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]):
        pairs.sort(key=lambda x: x[1])
        # USING DP
        # --------------------------------
        # n = len(pairs)
        # dp = [1] * n
        # result = 1
        # for i in range(1, n):
        #     for j in range(i):
        #         if pairs[i][0] > pairs[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     result = max(result, dp[i])
        # return result
        # GREEDY
        # -------------------------------------
        last_time = float('-inf')
        ans = 0
        for pair in pairs:
            if pair[0] > last_time:
                ans += 1
                last_time = pair[1]
        return ans


sol = Solution()
print(sol.findLongestChain([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]])) # -> 4
print(sol.findLongestChain([[1, 2], [2, 3], [3, 4]])) # -> 2
print(sol.findLongestChain([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]])) # -> 4
print(sol.findLongestChain([[1, 2], [7, 8], [4, 5]])) # -> 3
