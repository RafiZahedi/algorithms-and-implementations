def solve():
    n = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (p[i - 1] * p[j - 1]) % (i * j) == 0:
                count += 1
    print(count)


for _ in range(int(input())):
    solve()
