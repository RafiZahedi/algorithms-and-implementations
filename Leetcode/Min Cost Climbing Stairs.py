# 746. Min Cost Climbing Stairs

def solve():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # we modify the array itself
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 2], cost[i - 1])
    return min(cost[-1], cost[-2])


print(solve())
