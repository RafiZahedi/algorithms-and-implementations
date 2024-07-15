import math


def solve():
    x, y = map(int, input().split())

    for_y = math.ceil(y / 2)

    if y % 2 == 0:
        rem_cell = for_y * 7
    else:
        rem_cell = 11 + (for_y - 1) * 7

    if rem_cell >= x:
        for_x = 0
    else:
        for_x = math.ceil((x - rem_cell) / 15)
    answer = for_y + for_x

    return answer


for _ in range(int(input())):
    print(solve())
