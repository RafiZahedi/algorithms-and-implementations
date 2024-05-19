import heapq
from typing import List


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for _ in range(n)]

        for a, b, cost in roads:
            graph[a - 1].append([b - 1, cost])
            graph[b - 1].append([a - 1, cost])

        def dijkstra(start, graph):
            costs = [float('inf') for _ in range(n)]
            # start city has no cost
            costs[start] = 0

            pq = [(0, start)]
            min_cost = float('inf')

            while pq:
                cur_cost, cur_start = heapq.heappop(pq)

                # main calculation
                min_cost = min(min_cost, appleCost[cur_start] + (k + 1) * cur_cost)

                for city, cost in graph[cur_start]:

                    next_cost = cur_cost + cost

                    if next_cost < costs[city]:
                        costs[city] = next_cost
                        heapq.heappush(pq, (next_cost, city))

            return min_cost

        result = []
        for i in range(n):
            result.append(dijkstra(i, graph))
        return result


sol = Solution()
print(
    sol.minCost(n=4, roads=[[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]], appleCost=[56, 42, 102, 301], k=2))
