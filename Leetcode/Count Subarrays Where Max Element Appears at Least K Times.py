# 2962. Count Subarrays Where Max Element Appears at Least K Times

def solve():
    nums = [1, 3, 2, 3, 3]
    k = 2
    mx = max(nums)
    count_mx, left = 0, 0
    subarray_count = 0
    for right in range(len(nums)):
        if nums[right] == mx:
            count_mx += 1
        while count_mx == k:
            if nums[left] == mx:
                count_mx -= 1
            left += 1
        subarray_count += left
    return subarray_count


print(solve())
