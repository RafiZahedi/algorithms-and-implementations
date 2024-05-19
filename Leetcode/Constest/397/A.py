from typing import List


class Solution:
    def helper(self, grid):
        pass

    def maxScore(self, grid: List[List[int]]) -> int:
        m_row, n_col = len(grid), len(grid[0])
        upcoming_max = [[-float('inf')] * n_col for _ in range(m_row)]
        upcoming_max[m_row - 1][n_col - 1] = grid[m_row - 1][n_col - 1]
        for row in range(m_row - 1, -1, -1):
            for col in range(n_col - 1, -1, -1):
                if row < m_row - 1:

                    upcoming_max[row][col] = max(upcoming_max[row][col], upcoming_max[row + 1][col])
                if col < n_col - 1:
                    upcoming_max[row][col] = max(upcoming_max[row][col], upcoming_max[row][col + 1])
                upcoming_max[row][col] = max(upcoming_max[row][col], grid[row][col])

        answer = float('-inf')
        for row in range(m_row):
            for col in range(n_col):
                if row < m_row - 1:
                    answer = max(answer, upcoming_max[row + 1][col] - grid[row][col])
                if col < n_col - 1:
                    answer = max(answer, upcoming_max[row][col + 1] - grid[row][col])

        return answer


sol = Solution()
print(sol.maxScore([[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]))
