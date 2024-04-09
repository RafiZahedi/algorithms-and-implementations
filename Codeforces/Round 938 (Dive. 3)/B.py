def solve():
    n, a, b = map(int, input().split())
    nums = list(map(int, input().split()))
    # nums must be sorted
    nums.sort()
    dp1 = [0] * (n * n)
    dp2 = [0] * (n * n)

    base = nums[0]
    flag = False
    for row in range(n):
        dp1[row] = base + (row * b)

    # Calculating the array d
    for row in range(n):
        for col in range(n):
            dp2[row * n + col] = dp1[row] + (a * col)
    dp2.sort()

    # Checking if arrays c and d are equal
    for row in range(n * n):
        if nums[row] != dp2[row]:
            flag = True
            break

    return "YES" if not flag else "NO"


for _ in range(int(input())):
    print(solve())