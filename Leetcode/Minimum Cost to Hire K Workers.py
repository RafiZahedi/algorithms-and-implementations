import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        worker = []
        answer = float('inf')

        for i in range(len(wage)):
            worker.append((wage[i] / quality[i], quality[i]))

        worker.sort(key=lambda x: x[0])

        max_heap = []
        total_quality = 0
        for rate, q in worker:
            heapq.heappush(max_heap, -q)  # -q to represent the max heap
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                answer = min(answer, total_quality * rate)

        return answer


sol = Solution()
print(sol.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2))  # -> 105.0
print(sol.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3))  # -> 30.66
