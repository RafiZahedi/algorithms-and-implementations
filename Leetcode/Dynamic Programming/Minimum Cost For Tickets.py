from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(days):
                return 0
            buy_1 = costs[0] + dfs(i + 1)
            seven_days = days[i] + 7
            j = i
            while j < len(days) and days[j] < seven_days:
                j += 1
            buy_7 = costs[1] + dfs(j)
            thirty_days = days[i] + 30
            j = i
            while j < len(days) and days[j] < thirty_days:
                j += 1
            buy_30 = costs[2] + dfs(j)

            memo[i] = min(buy_30, buy_7, buy_1)
            return memo[i]

        return dfs(0)


sol = Solution()
print(sol.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))  # -> 11
print(sol.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))  # -> 17
