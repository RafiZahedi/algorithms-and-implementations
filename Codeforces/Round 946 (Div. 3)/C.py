from collections import defaultdict


def is_beautiful(t1, t2):
    diff_count = 0
    if t1[0] != t2[0]:
        diff_count += 1
    if t1[1] != t2[1]:
        diff_count += 1
    if t1[2] != t2[2]:
        diff_count += 1
    return diff_count == 1


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    ab = defaultdict(int)
    bc = defaultdict(int)
    ac = defaultdict(int)
    ab1 = defaultdict(int)
    bc1 = defaultdict(int)
    ac1 = defaultdict(int)
    answer = 0
    for i in range(n - 2):
        current = nums[i]
        nextNumber = nums[i + 1]
        afterNext = nums[i + 2]
        ab[(current, nextNumber)] += 1
        bc[(nextNumber, afterNext)] += 1
        ac[(current, afterNext)] += 1

        check = [(current, nextNumber, afterNext)]
        ab1[tuple(check)] += 1
        bc1[tuple(check)] += 1
        ac1[tuple(check)] += 1
        answer += ab[(current, nextNumber)] - ab1[tuple(check)]
        answer += bc[(nextNumber, afterNext)] - bc1[tuple(check)]
        answer += ac[(current, afterNext)] - ac1[tuple(check)]
    return answer


for _ in range(int(input())):
    print(solve())
