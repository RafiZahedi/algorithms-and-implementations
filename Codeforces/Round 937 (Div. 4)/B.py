def solve():
    n = int(input())
    for row in range(2 * n):
        for col in range(n):
            if (row // 2 + col) % 2 == 0:
                print('##', end="")
            else:
                print('..', end='')
        # have to print a new empty line.
        print()


for _ in range(int(input())):
    solve()
