def solve():
    a = input().strip()
    b = input().strip()

    count = 0
    for i in range(len(b)):
        j = 0
        for k in range(len(a)):
            if j + i < len(b) and b[j + i] == a[k]:
                j += 1
        count = max(count, j)

    # a + b - count is the answer
    print(len(a) + len(b) - count)


for _ in range(int(input())):
    solve()
