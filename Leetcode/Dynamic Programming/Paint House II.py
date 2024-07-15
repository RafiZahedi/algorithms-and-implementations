from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        memo = {}
        def dfs(i, prev_color):
            if (i, prev_color) in memo:
                return memo[(i, prev_color)]
            if i == len(costs):
                return 0
            min_cost = float('inf')
            for color in range(len(costs[i])):
                if color != prev_color:
                    min_cost = min(min_cost, costs[i][color] + dfs(i + 1, color))

            memo[(i, prev_color)] = min_cost
            return min_cost

        return dfs(0, -1)


sol = Solution()
print(sol.minCostII([[1, 5, 3], [2, 9, 4]]))  # -> 5
print(sol.minCostII([[1, 3], [2, 4]]))  # -> 5
