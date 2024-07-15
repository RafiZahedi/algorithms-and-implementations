def solve():
    n, l, r = map(int, input().split())
    result = [i for i in range(1, n + 1)]
    result[l - 1:r] = result[l - 1:r][::-1]
    print(*result)


#
# for _ in range(int(input())):
#     print(solve())
#
for _ in range(1):
    solve()
