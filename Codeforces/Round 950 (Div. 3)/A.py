import collections


def solve():
    n, m = map(int, input().split())
    bank = input()

    count = 0
    for i in range(ord('A'), ord('H')):
        if chr(i) not in bank:
            count += m
        else:
            temp = bank.count(chr(i))
            if temp < m:
                count += m - temp
    return count


for _ in range(int(input())):
    print(solve())

