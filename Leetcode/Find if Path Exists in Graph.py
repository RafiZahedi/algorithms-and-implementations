# 1971. Find if Path Exists in Graph

from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        def dfs(source, destination, visited):
            if source == destination:
                return True
            if source in visited:
                return False
            visited.add(source)
            for neighbor in graph[source]:
                if dfs(neighbor, destination, visited):
                    return True

            return False

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return dfs(source, destination, set())


sol = Solution()
print(sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # -> True
