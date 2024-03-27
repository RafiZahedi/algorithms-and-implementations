def solve(nums, k):
    # LeetCode: 713. Subarray Product Less Than K

    # two pointers technique.
    left, right = 0, 0
    count, product = 0, 1
    while right < len(nums):
        # while we can, we increase the size of the window
        product *= nums[right]

        # while the condition is not satisfied we shrink the size of the window
        while product >= k:
            # while we shrink the window, we exclude the left element.
            product //= nums[left]
            left += 1

        # this will be the size of the window
        count += right - left + 1
        right += 1

    return count


print(solve([10, 5, 2, 6], 100))
