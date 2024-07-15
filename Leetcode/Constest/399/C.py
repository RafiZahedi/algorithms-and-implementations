from typing import List
from collections import defaultdict


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def get_divisors(n):
            divisors = set()
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    if i != n // i:  # Avoid adding the square root twice for perfect squares
                        divisors.add(n // i)

        freq = defaultdict(int)
        for num in nums1:
            freq[num] += 1

        countDivisible = {}

        count = 0
        for num in nums2:
            product = num * k
            if product in countDivisible:
                count += countDivisible[product]
                continue

            currentCount = 0
            multiple = product
            while multiple <= 1000000:
                if multiple in freq:
                    currentCount += freq[multiple]
                multiple += product

            countDivisible[product] = currentCount
            count += currentCount

        return count


s = Solution()
print(s.numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))  # -> 5
print(s.numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))  # -> 2
