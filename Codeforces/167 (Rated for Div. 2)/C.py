def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    good = sum(1 for i in range(n) if a[i] == b[i] == 1)
    bad = sum(-1 for i in range(n) if a[i] == b[i] == -1)

    pos = sum(a[i] for i in range(n) if a[i] != b[i] and a[i] > b[i])
    neg = sum(b[i] for i in range(n) if a[i] != b[i] and a[i] <= b[i])

    if pos > neg:
        pos, neg = neg, pos

    half = min(neg - pos, good)
    pos += half
    good -= half

    half = good // 2
    pos += max(half, good - half)
    neg += min(half, good - half)

    if pos > neg:
        pos, neg = neg, pos

    half = max(pos - neg, bad)
    neg += half
    bad -= half

    half = bad // 2
    pos += max(half, bad - half)
    neg += min(half, bad - half)

    return min(pos, neg)


for _ in range(int(input())):
    print(solve())
