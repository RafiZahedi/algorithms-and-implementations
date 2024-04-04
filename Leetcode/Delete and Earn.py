# 740. Delete and Earn
from collections import defaultdict


def solve(nums):
    freq = defaultdict(int)
    maximum = 0
    for num in nums:
        freq[num] += num
        maximum = max(maximum, num)
    # dp = [0] * (maximum + 1)
    # dp[1] = freq[1]
    two_behind = 0
    one_behind = freq.get(1, 0)
    for i in range(2, maximum + 1):
        # dp[i] = max(dp[i - 1], dp[i - 2] + freq[i])
        current = max(one_behind, two_behind + freq[i])
        two_behind = one_behind
        one_behind = current
    return one_behind


print(solve([3, 4, 2]))  # -> 6
print(solve([2, 2, 3, 3, 3, 4]))  # -> 9
print(solve([2, 2, 2, 5, 6, 8]))
