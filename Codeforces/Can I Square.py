import math


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    sq_n = math.sqrt(total)
    return 'YES' if sq_n * sq_n == total else 'NO'


for _ in range(int(input())):
    print(solve())
