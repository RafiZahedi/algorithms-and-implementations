from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        count = 0

        for box in sorted(boxes, reverse=True):
            if count < len(warehouse) and box <= warehouse[count]:
                count += 1

        return count


sol = Solution()
print(sol.maxBoxesInWarehouse([4, 3, 4, 1], [5, 3, 3, 4, 1]))  # -> 3
print(sol.maxBoxesInWarehouse([1, 2, 2, 3, 4], [3, 4, 1, 2]))  # -> 3
