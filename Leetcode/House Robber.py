# 198. House Robber
def solve():
    nums = [2, 7, 9, 3, 1]
    n = len(nums)
    two_before = nums[0]
    one_before = max(nums[0], nums[1])
    for i in range(2, n):
        # It's either the previous house(dp[i-1]) or
        # The current house + the two before house(dp[i-2])
        current = max(one_before, nums[i] + two_before)
        two_before = one_before
        one_before = current
    return one_before


print(solve())
