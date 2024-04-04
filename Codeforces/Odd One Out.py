def solve():
    nums = list(map(int, input().split()))
    for num in nums:
        if nums.count(num) == 1:
            return num


for _ in range(int(input())):
    print(solve())
