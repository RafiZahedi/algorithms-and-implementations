def solve():
    n, f, k = map(int, input().split())
    cubes = list(map(int, input().split()))

    favorite_value = cubes[f - 1]
    cubes_sorted = sorted(cubes, reverse=True)

    after = cubes_sorted[:k]

    count = after.count(favorite_value)

    all_count = cubes.count(favorite_value)

    remaining = all_count - count

    if favorite_value in after:
        if count == all_count:
            return "YES"
        elif remaining > 0:
            return "MAYBE"
        else:
            return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    print(solve())
