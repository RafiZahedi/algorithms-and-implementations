def solve():
    n = int(input().strip())

    if n == 1:
        print(n)
        return

    if n <= 3:
        print("NO SOLUTION")
    else:
        start = n if n % 2 == 0 else n - 1
        for i in range(start - 1, 0, -2):
            print(i, end=" ")
        for i in range(start, 1, -2):
            print(i, end=" ")
        if n % 2 == 1:
            print(n)
        print()


for _ in range(1):
    solve()
