def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    if total % 3 == 0:
        return 0
    if (total + 1) % 3 == 0:
        return 1
    for num in nums:
        if (total - num) % 3 == 0:
            return 1
    return 2


for _ in range(int(input())):
    print(solve())
