def solve():
    n = int(input())
    a = list(map(int, input().split()))

    res = float('inf')
    for i in range(n - 1):
        res = min(res, max(a[i], a[i + 1]))
    return res - 1


for _ in range(int(input())):
    print(solve())
