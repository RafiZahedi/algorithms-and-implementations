def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    total = 0
    for num in nums:
        total += abs(num)
    return total


for _ in range(int(input())):
    print(solve())
