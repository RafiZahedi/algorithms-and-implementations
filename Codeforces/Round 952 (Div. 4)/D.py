def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = input()
        grid.append(row)
    total_x, total_y, count = 0, 0, 0

    for y in range(n):
        for x in range(m):
            if grid[y][x] == '#':
                total_x += x + 1
                total_y += y + 1
                count += 1

    center_x = total_x // count
    center_y = total_y // count

    print(center_y, center_x)


for _ in range(int(input())):
    solve()
