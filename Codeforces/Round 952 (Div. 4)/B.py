import math


def accepted(v, i, j, curr_sum):
    for k in range(i, j + 1):
        if 2 * v[k] == curr_sum:
            return True
    return False


def solve():
    x, y, z, k = map(int, input().split())
    answer = 0

    for a in range(1, int(k ** (1 / 3)) + 1):
        if k % a == 0:
            for b in range(1, int((k // a) ** 0.5) + 1):
                if (k // a) % b == 0:
                    c = k // (a * b)

                    # case # 1 a < x b <= y c <= z
                    if a <= x and b <= y and c <= z:
                        answer = max(answer, (x - a + 1) * (y - b + 1) * (z - c + 1))
                    # case # 4
                    if a <= x and c <= y and b <= z:
                        answer = max(answer, (x - a + 1) * (y - c + 1) * (z - b + 1))
                    # case 3
                    if b <= x and a <= y and c <= z:
                        answer = max(answer, (x - b + 1) * (y - a + 1) * (z - c + 1))

                    if b <= x and c <= y and a <= z:
                        answer = max(answer, (x - b + 1) * (y - c + 1) * (z - a + 1))
                    if c <= x and a <= y and b <= z:
                        answer = max(answer, (x - c + 1) * (y - a + 1) * (z - b + 1))
                    if c <= x and b <= y and a <= z:
                        answer = max(answer, (x - c + 1) * (y - b + 1) * (z - a + 1))
    return answer


for _ in range(int(input())):
    print(solve())
