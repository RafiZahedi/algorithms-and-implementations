def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    a = [10 ** 8]
    for xi in nums:
        a.append(a[-1] + xi)

    print(*a)


for _ in range(int(input())):
    solve()
