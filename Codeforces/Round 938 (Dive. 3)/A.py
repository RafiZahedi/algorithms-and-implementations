def solve():
    n, a, b = map(int, input().split())
    price = 0
    while n >= 2:
        price += min((a * 2), b)
        n -= 2
    return price if not n else price + a


for _ in range(int(input())):
    print(solve())
