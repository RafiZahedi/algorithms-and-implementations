maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [3, 2]

from collections import deque


def solve():
    m, n = len(maze), len(maze[0])
    visited = {tuple(start)}
    q = deque([tuple(start)])
    while len(q) > 0:
        x, y = q.popleft()
        if x == destination[0] and y == destination[1]:
            return True
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1:
                nx += dx
                ny += dy
            nx -= dx
            ny -= dy
            if (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
    return False


print(solve())
