height = [1, 4, 6, 5, 3, 7, 6, 2]
left, right = 0, len(height) - 1
Max = 0
while left < right:
    current_area = min(height[left], height[right]) * (max(right, left) - min(right, left))
    Max = max(Max, current_area)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(Max)
