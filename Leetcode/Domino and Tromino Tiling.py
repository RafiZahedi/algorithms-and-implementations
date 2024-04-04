def solve():
    # 790. Domino and Tromino Tiling
    n = 7
    MOD = 10 ** 9 + 7
    three_before = 1
    two_before = 2
    one_before = 5
    for i in range(4, n + 1):
        current = ((one_before * 2) + three_before) % MOD
        three_before, two_before, one_before = two_before, one_before, current
    return one_before


print(solve())
