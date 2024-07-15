def solve():
    n, m = map(int, input().split())

    if n == 0:
        # if m is zero this is an endge case
        if m == 0:
            return 0
        # if n is zero and m not
        # its just m >> of all then -1
        i = 1
        while m >> i:
            i += 1
        return (1 << i) - 1

    time = 0
    # we only need to check up to 31
    for i in range(32):
        # either it's true
        if (n >> i) & 1:
            time += (1 << i)
        # or not
        else:
            pos = n - ((n >> i) << i)
            if m >= (pos + 1):
                time += (1 << i)
            elif m >= (1 << i) - pos:
                time += (1 << i)

    return time


for _ in range(int(input())):
    print(solve())
