import heapq


def dijkstra(src, num_vertices, graph):
    distance = [float('inf')] * num_vertices
    distance[src] = 0

    paths = [-1] * num_vertices

    pq = [(0, src)]

    while pq:
        dist_source, source = heapq.heappop(pq)

        if dist_source > distance[source]:
            continue

        for edge in graph:
            if edge[0] == source:
                destination, weight = edge[1], edge[2]
                if distance[source] + weight < distance[destination]:
                    distance[destination] = distance[source] + weight
                    paths[destination] = source
                    heapq.heappush(pq, (distance[destination], destination))

    # Print the shortest distances and paths
    print("Vertex\tDistance from Source\tPath")
    for i in range(num_vertices):
        print(f"{i}\t{distance[i]}\t\t{get_shortest_path(paths, src, i)}")


def get_shortest_path(paths, src, dest):
    path = [dest]
    while dest != src:
        dest = paths[dest]
        path.append(dest)
    return " -> ".join(map(str, reversed(path)))


g = []
num_vertices, num_edges = map(int, input().split())
for _ in range(num_edges):
    src, nbr, wt = map(int, input().split())
    g.append([src, nbr, wt])
print(dijkstra(0, num_vertices, g))
# 5 6
# 0 1 4
# 0 2 1
# 1 3 1
# 2 3 5
# 2 1 2
# 3 4 3

# output: 7
