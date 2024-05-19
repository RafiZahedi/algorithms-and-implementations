from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0] * len(grid)
        col_count = [0] * len(grid[0])

        # count the number of servers in each row and column
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # If there's a server at this location
                    row_count[i] += 1  # Increment the count for this row
                    col_count[j] += 1  # Increment the count for this column

        count = 0

        # for each server, check if it communicates with any other server
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # If there's a server at this location
                    # If there's another server in its row or column
                    if row_count[i] > 1 or col_count[j] > 1:
                        count += 1  # Increment the total count

        return count

sol = Solution()
print(sol.countServers([[1, 0], [0, 1]]))  # -> 0
print(sol.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))  # -> 4
