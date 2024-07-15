def solve():
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    count = 0

    if k % 2 == 0:
        left = k // 2
        right = k // 2
    else:
        left = (k + 1) // 2
        right = (k - 1) // 2

    # first from left to right
    for i in range(n):
        if ships[i] <= left:
            left -= ships[i]
            ships[i] = 0
            count += 1
        else:
            ships[i] -= left
            break
    # from right to left
    for i in range(n - 1, -1, -1):
        if ships[i] == 0:
            break
        if ships[i] <= right:
            right -= ships[i]
            ships[i] = 0
            count += 1
        else:
            ships[i] -= right
            break

    return count


for _ in range(int(input())):
    print(solve())
