def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(a[:k])
    res = n - a[k - 1]

    for i in range(k - 1):
        res += a[i] - 1

    print(res)


for _ in range(int(input())):
    solve()
