from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        memo = {}

        def dfs(i, k):
            if i >= len(piles) or k == 0:
                return 0
            if (i, k) in memo:
                return memo[(i, k)]
            max_pile = dfs(i + 1, k)
            current_sum = 0
            for j in range(min(len(piles[i]), k)):
                current_sum += piles[i][j]
                max_pile = max(max_pile, current_sum + dfs(i + 1, k - j - 1))

            memo[(i, k)] = max_pile
            return max_pile

        return dfs(0, k)


sol = Solution()
print(sol.maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))  # -> 101
