from typing import List


class SegmentTree:
    def init(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        max_val = 0
        while left < right:
            if left % 2 == 1:
                max_val = max(max_val, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                max_val = max(max_val, self.tree[right])
            left //= 2
            right //= 2
        return max_val


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        n = len(nums)

        take = [0] * n
        no_take = [0] * n

        take[0] = max(0, nums[0])
        no_take[0] = 0

        for i in range(1, n):
            take[i] = max(0, nums[i] + no_take[i - 1])
            no_take[i] = max(take[i - 1], no_take[i - 1])

        total = 0

        for query in queries:
            pos = query[0]
            x = query[1]

            nums[pos] = x

            if pos == 0:
                take[0] = max(0, nums[0])
                no_take[0] = 0

            for i in range(max(1, pos), n):
                if i == pos:
                    take[i] = max(0, nums[i] + (no_take[i - 1] if i > 0 else 0))
                else:
                    take[i] = max(0, nums[i] + no_take[i - 1])
                no_take[i] = max(take[i - 1], no_take[i - 1])

            maxSum = max(take[n - 1], no_take[n - 1])
            total = (total + maxSum) % MOD

        return total


s = Solution()
print(s.maximumSumSubsequence([3, 5, 9], [[1, -2], [0, -3]]))  # -> 21
print(s.maximumSumSubsequence([0, -1], [[0, -5]]))  # -> 0
