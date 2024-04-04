# 1137. N-th Tribonacci Number

def solve():
    n = 25
    first, second, third = 0, 1, 1
    result = 0
    for i in range(3, n + 1):
        result = first + second + third
        first = second
        second = third
        third = result
    return result


print(solve())
