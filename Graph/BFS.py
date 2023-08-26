from collections import defaultdict as dd
# test case             # Output -> 0 9 7 11 10 8 6 3 1 12 5 2 4
# 11 15
# 0 9
# 0 7
# 0 11
# 9 10
# 9 8
# 7 6
# 7 3
# 7 11
# 10 1
# 8 1
# 8 12
# 12 2
# 3 2
# 3 4
# 6 5
v, e = map(int, input().split())
Graph = dd(list)
for i in range(e):
    a, b = input().split()
    Graph[a].append(b)
    Graph[b].append(a)
visited = set()
queue = []
start = '0'


def bfs(Graph, start):
    visited.add(start)
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in Graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print(bfs(Graph, start))
