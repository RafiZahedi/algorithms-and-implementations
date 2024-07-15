def solve():
    x, y = map(int, input().split())
    xor = x ^ y
    count = 0 # to count the trailling zeros I think.
    while xor & 1 == 0 and xor:
        count += 1
        xor >>= 1
    return 1 << count


for _ in range(int(input())):
    print(solve())
