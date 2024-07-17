def solve():
    n = int(input())
    nums = [1 << i for i in range(61) if n & (1 << i)]
    results = [n] + [n - bit for bit in nums if n - bit > 0]
    results.reverse()
    print(len(results))
    print(" ".join(map(str, results)))


for _ in range(int(input())):
    solve()
