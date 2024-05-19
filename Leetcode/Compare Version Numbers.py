# 165. Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)
        to_go = max(n1, n2)

        for i in range(to_go):

            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0

            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0


sol = Solution()
print(sol.compareVersion('1.01', '1.001'))  # -> 0
print(sol.compareVersion('1.0', '1.0.0'))  # -> 0
print(sol.compareVersion('0.1', '1.1'))  # -> -1
