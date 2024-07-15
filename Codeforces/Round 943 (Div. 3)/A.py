def solve():
    n, k, pb, ps = map(int, input().split())
    pb -= 1
    ps -= 1
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    b = []
    s = []
    vb = [False] * n
    vs = [False] * n

    while not vb[pb]:
        b.append(a[pb])
        vb[pb] = True
        pb = p[pb]

    while not vs[ps]:
        s.append(a[ps])
        vs[ps] = True
        ps = p[ps]

    sb = 0
    sc = 0
    csb = 0
    csc = 0

    for i in range(min(len(b), k)):
        sb = max(sb, csb + b[i] * (k - i))
        csb += b[i]

    for i in range(min(len(s), k)):
        sc = max(sc, csc + s[i] * (k - i))
        csc += s[i]

    print("Draw" if sb == sc else "Bodya" if sb > sc else "Sasha")


if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        solve()
