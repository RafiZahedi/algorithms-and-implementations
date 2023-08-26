nums = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
max_size = 0
counter = 0
for num in nums:
    if num == 1:
        counter += 1
    else:
        counter = 0
    max_size = max(counter, max_size)
print(max_size)
