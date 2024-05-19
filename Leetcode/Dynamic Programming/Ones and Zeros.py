from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dp(ones, zeros, i):
            if (ones, zeros, i) in memo:
                return memo[(ones, zeros, i)]
            if i == len(strs) or (ones + zeros) == 0:
                return 0

            this_zeros = strs[i].count('0')
            this_ones = strs[i].count('1')

            skip = dp(ones, zeros, i + 1)

            take = 0
            if this_zeros <= zeros and this_ones <= ones:
                take = 1 + dp(ones - this_ones, zeros - this_zeros, i + 1)

            memo[(ones, zeros, i)] = max(skip, take)
            return max(skip, take)

        # n = 1
        # m = 0
        return dp(n, m, 0)


sol = Solution()
print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))  # Output: 4
print(sol.findMaxForm(["10", "0", "1"], 1, 1))  # Output: 2
