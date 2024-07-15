def check(a, b, op):
    if op == '+':
        return a + b
    else:
        return a * b


def bfs(index, adj, low, parent):
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

        # if neighbor_low <= low[index]:
        #     result = min(result, neighbor_low)
        # else:
        #     min_cut_edges[(index, neighbor)] = sub_tree_size

    low[index] = result
    return result, subtree_size


def dfs(s, pos, count, dp):
    if count == 0:
        return int(s[pos:])
    if dp[pos][count] != -1:
        return dp[pos][count]
    res = float('inf')
    for i in range(pos, len(s) - count):
        a = int(s[pos:i + 1])
        b = dfs(s, i + 1, count - 1, dp)
        res = min(res, check(a, b, '+'))
        res = min(res, check(a, b, '*'))
    dp[pos][count] = res
    return res


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        dp = [[-1] * 25 for _ in range(25)]
        print(dfs(s, 0, n - 2, dp))


if __name__ == "__main__":
    main()
