def is_binary(num):
    for digit in str(num):
        if digit != '0' and digit != '1':
            return False
    return True


def solve():
    n = int(input())
    copy_n = n
    product, result = 0, 0
    for _ in range(len(str(n))):
        reminder = n % 10
        n //= 10
        product = product * 10 + reminder
        result += 1
    if (product == copy_n and not copy_n % 11 and result > 2) or is_binary(copy_n):
        return "YES"
    return "NO"


for _ in range(int(input())):
    print(solve())
