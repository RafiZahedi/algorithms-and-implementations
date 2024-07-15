import math


def solve():
    left, right = map(int, input().split())

    return int(math.log2(right))


for _ in range(int(input())):
    print(solve())
