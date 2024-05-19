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
        answer = []

        p_change = [0] * (n - 1)
        for i in range(n - 1):
            p_change[i] = 1 if (nums[i] % 2 != nums[i + 1] % 2) else 0

        pre_sum = [0] * n
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + p_change[i - 1]

        for q in queries:
            start, end = q[0], q[1]
            if start == end:
                answer.append(True)
            else:
                changes = pre_sum[end] - pre_sum[start]
                answer.append(changes == (end - start))

        return answer


sol = Solution()
print(sol.isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))
print(sol.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
