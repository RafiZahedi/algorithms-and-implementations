def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    s = set()

    total = 0
    for i in range(n):
        s.add(a[i])
        total += a[i]
        max_sofar = max(s)
        # if total - max equal max so far then yes
        if max_sofar == (total - max_sofar):
            ans += 1

    return ans


for _ in range(int(input())):
    print(solve())
