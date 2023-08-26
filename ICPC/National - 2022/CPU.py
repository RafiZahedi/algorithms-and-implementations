for _ in range(int(input())):
    n = int(input())
    starts = list(map(int, input().split()))
    ends = list(map(int, input().split()))
    jobs = sorted(zip(starts, ends), key=lambda x: x[1])
    last_finish = float('-inf')
    count = 0
    for s, f in jobs:
        if s > last_finish:
            count += 1
            last_finish = f
    print(count)
