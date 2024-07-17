def solve():
    n, k = map(int, input().split())
    k -= 1
    if n == 1:
        return 0

    count = 0
    while n > 1:
        n -= k
        count += 1

    return count

for _ in range(int(input())):
    print(solve())

# print(solve())
