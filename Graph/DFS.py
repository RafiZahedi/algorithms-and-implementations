from collections import defaultdict

visited = set()
path = []
queue = []


def dfs(graph, start):
    if start in visited:
        return
    visited.add(start)
    for node in graph[start]:
        dfs(graph, node)
    print(start)
    return


def bfs(graph, start):
    visited.add(start)
    queue.append(start)
    while queue:
        m = queue.pop(0) # a f g d e c b None
        print(m, end=' ')
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


v, e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(bfs(graph, 0))
