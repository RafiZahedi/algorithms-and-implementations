def solve():
    a, b, c = map(int, input().split())

    for _ in range(5):
        least = min(a, b, c)
        if least == a:
            a += 1
            continue
        if least == b:
            b += 1
            continue
        c += 1
    return a * b * c


for _ in range(int(input())):
    print(solve())

# print(solve())
