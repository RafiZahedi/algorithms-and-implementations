import math


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = [math.gcd(a[i], a[i + 1]) for i in range(n - 1)]

    # looking for an index that is greater than the next one
    to_delete = -1
    for i in range(n - 2):
        if b[i] > b[i + 1]:
            to_delete = i
            break
    # if we can't find one we can do it.
    if to_delete == -1:
        return "YES"

    pair1 = []
    for i in range(n):
        if i != to_delete + 1:
            pair1.append(a[i])

    pair2 = []
    for i in range(n):
        if i != to_delete + 2:
            pair2.append(a[i])
    pair3 = []
    for i in range(n):
        if i != to_delete:
            pair3.append(a[i])

    b1 = []
    b2 = []
    b3 = []

    for i in range(n - 2):
        gcd_b1 = math.gcd(pair1[i], pair1[i + 1])
        b1.append(gcd_b1)

        gcd_b2 = math.gcd(pair2[i], pair2[i + 1])
        b2.append(gcd_b2)

        gcd_b3 = math.gcd(pair3[i], pair3[i + 1])
        b3.append(gcd_b3)

    f_pair1 = True
    for i in range(n - 3):
        if not (b1[i] <= b1[i + 1]):
            f_pair1 = False
            break

    f_pair2 = True
    for i in range(n - 3):
        if not (b2[i] <= b2[i + 1]):
            f_pair2 = False
            break

    f_pair3 = True
    for i in range(n - 3):
        if not (b3[i] <= b3[i + 1]):
            f_pair3 = False
            break

    if not (f_pair1 or f_pair2 or f_pair3):
        return "NO"
    else:
        return "YES"


for _ in range(int(input())):
    print(solve())
