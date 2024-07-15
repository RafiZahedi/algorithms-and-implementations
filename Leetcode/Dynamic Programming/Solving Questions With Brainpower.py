from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(questions):
                return 0
            pick = questions[i][0] + dp(i + questions[i][1] + 1)
            no_pick = dp(i + 1)

            memo[i] = max(pick, no_pick)
            return max(pick, no_pick)

        return dp(0)


sol = Solution()
print(sol.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))  # -> 5
print(sol.mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))  # -> 7
