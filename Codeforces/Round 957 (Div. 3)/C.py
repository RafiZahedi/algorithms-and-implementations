def solve():
    n, m, k = map(int, input().split())

    for i in range(n, m, -1):
        print(i, end=" ")
    for i in range(1, m + 1):
        print(i, end=" ")
    print()


for _ in range(int(input())):
    solve()
