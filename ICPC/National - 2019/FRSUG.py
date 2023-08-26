# this problem can be solved using Dijkstra Algorithm.
# in the second test case of this question there is a problem.
# the q queries of this test case is given in one line, but the all queries must be in separated lines each.

# Two tricks must be handled:
# 1- you will not be given the number of vertices
# 2- You need to check if the target is a valid target or no (if no print "----" )
import heapq


def dijkstra(start_point, num_vertices, g):
    distance = [float('inf')] * num_vertices
    distance[start_point] = 0
    pq = [(0, start_point)]
    while pq:
        dist_source, source = heapq.heappop(pq)
        if dist_source > distance[source]:
            continue
        for edge in g:
            if edge[0] == source:
                destination, weight = edge[1], edge[2]
                if distance[source] + weight < distance[destination]:
                    distance[destination] = distance[source] + weight
                    heapq.heappush(pq, (distance[destination], destination))
    return distance


graph = []
n = int(input())
for _ in range(n):
    src, nbr, wt = map(int, input().split())
    graph.append([src - 1, nbr - 1, wt])
start = int(input())
result = dijkstra(start, n, graph)
hm = dict()
for i, res in enumerate(result):
    hm[i] = res
for _ in range(int(input())):
    target = int(input())
    if target not in hm.keys():
        print("----")
    else:
        print(hm[target])