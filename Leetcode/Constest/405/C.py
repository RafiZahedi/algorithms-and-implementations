from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp_x = [[0] * (n + 1) for _ in range(m + 1)]
        dp_y = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    dp_x[i + 1][j + 1] += 1
                elif grid[i][j] == 'Y':
                    dp_y[i + 1][j + 1] += 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp_x[i][j] += dp_x[i - 1][j] + dp_x[i][j - 1] - dp_x[i - 1][j - 1]
                dp_y[i][j] += dp_y[i - 1][j] + dp_y[i][j - 1] - dp_y[i - 1][j - 1]

        count = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = dp_x[i][j]
                y = dp_y[i][j]
                # if they are equal and we have x
                if x == y and x > 0:
                    count += 1

        return count


sol = Solution()
print(sol.numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]))
print(sol.numberOfSubmatrices([["X", "X"], ["X", "Y"]]))
