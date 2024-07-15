def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mp = {}
    for item in a:
        mod = item % k
        if item in mp.get(mod, set()):
            mp[mod].remove(item)
        else:
            mp.setdefault(mod, set()).add(item)

    count = 0
    value = -1
    for mod, values in mp.items():
        length = len(values)
        # we need to check if length is odd or even
        if length % 2 != 0:
            count += 1
            value = mod

    # if found more than 1 then no answer
    if count > 1:
        print(-1)
        return

    ans = 0
    for mod, values in mp.items():
        if mod == value:
            continue
        sorted_values = sorted(values)
        i = 0
        while i < len(sorted_values) - 1:
            current = sorted_values[i]
            i += 1
            copy_current = sorted_values[i]
            ans += (copy_current - current) // k
            i += 1

    if count:
        v = sorted(mp[value])
        n = len(v)
        if n == 1:
            print(ans)
            return

        pref = [0] * n
        suf = [0] * n

        pref[1] = v[1] - v[0]
        for i in range(3, n, 2):
            pref[i] = v[i] - v[i - 1] + pref[i - 2]

        suf[n - 2] = v[n - 1] - v[n - 2]
        for i in range(n - 4, -1, -2):
            suf[i] = v[i + 1] - v[i] + suf[i + 2]

        minimum = float('inf')
        for i in range(0, n, 2):
            item = 0
            if i > 0:
                item += pref[i - 1]
            if i + 1 < n:
                item += suf[i + 1]
            minimum = min(minimum, item)

        ans += minimum // k

    print(ans)


for _ in range(int(input())):
    solve()