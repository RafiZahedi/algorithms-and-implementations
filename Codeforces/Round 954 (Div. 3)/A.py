def solve():
    x = list(map(int, input().split()))

    return max(x) - min(x)


for _ in range(int(input())):
    print(solve())

# print(solve())
