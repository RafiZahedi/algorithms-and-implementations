from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fractions = []

        for i in range(n):
            for j in range(n - 1, i, -1):
                fractions.append([arr[i], arr[j]])

        fractions.sort(key=lambda x: x[0] / x[1])
        return fractions[k-1]


sol = Solution()
print(sol.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))  # -> [2,5]
# print(sol.kthSmallestPrimeFraction(arr=[1, 7], k=1))  # -> [2,5]
