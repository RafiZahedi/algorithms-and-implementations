def solve():
    n, m = map(int, input().split())
    s = input()
    ind = list(map(int, input().split()))
    c = input()

    c = ''.join(sorted(c))

    freq = {}
    for item in ind:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    total = sum(count - 1 for count in freq.values())

    c = c[:m - total]

    s_list = list(s)

    i = 0
    for item in sorted(freq.keys()):
        s_list[item - 1] = c[i]
        i += 1

    return ''.join(s_list)


# Handling multiple test cases
for _ in range(int(input())):
    print(solve())
