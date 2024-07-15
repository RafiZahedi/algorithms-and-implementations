def solve():
    n = int(input())
    x = input()
    y = input()

    for i in range(n):
        if not (x[i] == y[i] or (x[i] == 'G' and y[i] == 'C') or (x[i] == 'C' and y[i] == 'G')
                or (x[i] == 'A' and y[i] == 'T') or (x[i] == 'T' and y[i] == 'A')):
            return "NO"
    return "YES"


for _ in range(1):
    print(solve())
