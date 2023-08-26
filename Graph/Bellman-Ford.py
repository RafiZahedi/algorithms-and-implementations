def bellman_ford(src, v, graph):
    distance = [float("inf")] * v
    distance[src] = 0

    for _ in range(v - 1):
        for u, v, w in graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            print("Graph has a negative cycle")
            return

    for i in range(v + 1):
        # print("from source to", i, "shortest is", distance[i])
        print(i + 1, distance[i])


g = []
num_vertices, num_edges = map(int, input().split())
for _ in range(num_edges):
    sr, des, wt = map(int, input().split())
    g.append([sr - 1, des - 1, wt])
bellman_ford(0, 5, g)

# input
# 5 6
# 0 1 1
# 0 2 4
# 1 2 3
# 1 3 2
# 2 3 -5
# 3 4 -1
# output
# 0 0
# 1 1
# 2 4
# 3 -1
# 4 -2
