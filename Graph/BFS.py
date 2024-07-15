from collections import defaultdict as dd

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
