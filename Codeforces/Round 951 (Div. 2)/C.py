from math import gcd


# tents to be faster than built in
def myGCD(a, b):
    while b:
        a, b = b, a % b
    return a


def sol():
    n = int(input())
    k = list(map(int, input().split()))

    product = 1  # to store the product off all
    for item in k:
        temp = gcd(product, item)
        temp = item // temp
        product *= temp

    total = 0
    result = []
    for item in k:
        total += product // item
        result.append(product // item)

    # if our total is greater than the product then impossible
    if total >= product:
        print(-1)
    else:
        print(*result)


for _ in range(int(input())):
    sol()
