class Solution:
    def __init__(self):
        self.dp = {}

    def waysToReachStair(self, k: int) -> int:
        def dp(k, i, jump, can):
            if i > k + 5:
                return 0

            if jump > 31:
                return 0

            if (i, jump, can) in self.dp:
                return self.dp[(i, jump, can)]

            ans = (i == k)
            if can:
                ans += dp(k, i - 1, jump, 0)
            if i + (1 << jump) <= k + 1:
                ans += dp(k, i + (1 << jump), jump + 1, 1)

            self.dp[(i, jump, can)] = ans
            return ans

        return dp(k, 1, 0, 1)


solution = Solution()
print(solution.waysToReachStair(8))
