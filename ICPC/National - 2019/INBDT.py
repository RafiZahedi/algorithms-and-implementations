from collections import deque

def BFS(ways, parent, visited, n, s, t):
    q = deque()
    parent[s] = -1
    q.append(s)
    while q:
        u = q.popleft()
        for i in range(n):
            if not visited[i] and ways[u][i] > 0:
                q.append(i)
                parent[i] = u
                visited[i] = True
    return visited[t]

def DFS(rGraph, parent, visited, n, x, t):
    if x == t:
        return True
    visited[x] = True
    for i in range(n):
        if rGraph[x][i] > 0 and not visited[i]:
            parent[i] = x
            if DFS(rGraph, parent, visited, n, i, t):
                return True
    return False

def FordFulkerson(graph, n, s, t):
    rGraph = [[0 for _ in range(n)] for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]

    # Replicate the graph for the residual one
    for i in range(n):
        for j in range(n):
            rGraph[i][j] = graph[i][j]

    max_flow = 0

    while BFS(rGraph, parent, visited, n, s, t):
        # while DFS(rGraph, parent, visited, n, s, t):
        visited = [False for _ in range(n)]
        path_flow = float('inf')  # Current flow to add to the max flow later

        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, rGraph[u][v])
            v = u

        v = t
        while v != s:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())  # Read the number of nodes (n) and edges (m).
        s, t, m = map(int,
                      input().split())  # Read the starting point (s), ending point (t), and the number of edges (m).
        s -= 1
        t -= 1

        graph = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(m):
            a, b, k = map(int, input().split())
            graph[a - 1][b - 1] = k

        print("Max Flow in this graph is:", FordFulkerson(graph, n, s, t))
