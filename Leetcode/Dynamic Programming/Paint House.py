from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}

        def dfs(i, prev_color):
            if (i, prev_color) in memo:
                return memo[(i, prev_color)]
            if i == len(costs):
                return 0
            min_cost = float('inf')
            for color in range(3):
                if color != prev_color:
                    min_cost = min(min_cost, costs[i][color] + dfs(i + 1, color))
            memo[(i, prev_color)] = min_cost
            return min_cost
        return dfs(0, -1)


sol = Solution()
print(sol.minCost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]))  # -> 10
print(sol.minCost(costs=[[7, 6, 2]]))  # -> 2
print(sol.minCost(costs=[[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]))  # -> 26
