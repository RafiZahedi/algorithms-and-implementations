class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}

        def dp(length):
            if length > high:
                return 0
            if length >= low:
                result = 1
            else:
                result = 0
            if length in memo:
                return memo[length]

            append_one = dp(length + one)
            append_zero = dp(length + zero)

            memo[length] = (result + append_zero + append_one) % MOD
            return memo[length]

        result = dp(0)
        return result


sol = Solution()
print(sol.countGoodStrings(low=3, high=3, zero=1, one=1))  # -> 8
print(sol.countGoodStrings(low=2, high=3, zero=1, one=2))  # ->  5
