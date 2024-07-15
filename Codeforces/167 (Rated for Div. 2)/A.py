def solve():
    x, y = map(int, input().split())
    if y < -1:
        return "NO"
    return "YES"

for _ in range(int(input())):
    print(solve())

# print(solve())
