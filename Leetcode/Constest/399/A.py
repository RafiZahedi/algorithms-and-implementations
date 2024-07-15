from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
        return count


s = Solution()
print(s.numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
print(s.numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
