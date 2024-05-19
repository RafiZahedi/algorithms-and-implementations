from typing import List


class Solution:
    def isSpecial(self, nums: List[int]) -> bool:
        last = nums[0]
        for num in nums[1:]:
            if num % 2 == last % 2:
                return False
            last = num
        return True

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        result = []

        parity_change = [0] * (n - 1)
        for i in range(n - 1):
            parity_change[i] = 1 if (nums[i] % 2 != nums[i + 1] % 2) else 0

        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + parity_change[i - 1]

        for q in queries:
            start, end = q, q
            if start == end:
                result.append(True)
            else:
                parity_changes_in_subarray = prefix_sum[end] - prefix_sum[start]
                result.append(parity_changes_in_subarray == (end - start))

        return result


sol = Solution()
print(sol.isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))  # -> False
print(sol.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
