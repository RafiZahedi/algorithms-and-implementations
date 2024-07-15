
def dfs(index, adj, low, parent):
    global dfs_timer
    if low[index] != -1:
        return (low[index], 0)

    dfs_timer += 1
    low[index] = dfs_timer

    result = low[index]
    subtree_size = 1

    for neighbor in adj[index]:
        if neighbor == parent:
            continue
        neighbor_result = dfs(neighbor, adj, low, index)
        neighbor_low, sub_tree_size = neighbor_result

        subtree_size += sub_tree_size

        if neighbor_low <= low[index]:
            result = min(result, neighbor_low)
        else:
            min_cut_edges[(index, neighbor)] = sub_tree_size

    low[index] = result
    return result, subtree_size


def main():
    global min_cut_edges, dfs_timer

    for _ in range(int(input())):
        num_vertices, num_edges = map(int, input().split())

        graph = [[] for _ in range(num_vertices)]

        for _ in range(num_edges):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        min_cut_edges = {}
        dfs_timer = 0
        low = [-1] * num_vertices
        articulation_result = dfs(0, graph, low, -1)

        answer = num_vertices * (num_vertices - 1) // 2

        for edge, size in min_cut_edges.items():
            left = size
            right = num_vertices - size
            answer = min(answer, (left * (left - 1) + (right * (right - 1))) // 2)

        print(answer)


if __name__ == "__main__":
    main()
