nums = [0, 0, 0, 0, 1, 1, 1, 1]
max_size = 0
count_zero = 0
left, right = 0, 0
while right < len(nums):
    if nums[right] == 0:
        count_zero += 1
    while count_zero == 2:
        if nums[left] == 0:
            count_zero -= 1
        left += 1
    max_size = max(max_size, right - left + 1)
    right += 1
print(max_size)
