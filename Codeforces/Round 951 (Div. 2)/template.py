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


def operation(mat):
    n = len(mat)
    t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][i] = mat[i][j]
    return t


def solve():
    n, m = map(int, input().split())

    grid1 = [list(map(int, input().split())) for _ in range(n)]
    grid2 = [list(map(int, input().split())) for _ in range(n)]

    if n == m:
        st = set()
        for item in grid1:
            temp = frozenset(item)
            st.add(temp)

        for item in grid2:
            temp = frozenset(item)
            if temp not in st:
                return "NO"

        # we should do trans then.
        grid1 = operation(grid1)
        grid2 = operation(grid2)
        # and clear the data
        st.clear()

        for item in grid1:
            temp = frozenset(item)
            st.add(temp)

        for item in grid2:
            temp = frozenset(item)
            if temp not in st:
                return "NO"

        return "YES"
    else:
        # create a new set
        st = set()
        for item in grid1:
            temp = frozenset(item)
            st.add(temp)

        for item in grid2:
            temp = frozenset(item)
            if temp not in st:
                return "NO"

        st.clear()

        for j in range(m):
            temp = frozenset(grid1[i][j] for i in range(n))
            st.add(temp)

        for j in range(m):
            temp = frozenset(grid2[i][j] for i in range(n))
            if temp not in st:
                return 'NO'

        return "YES"


for _ in range(int(input())):
    print(solve())
