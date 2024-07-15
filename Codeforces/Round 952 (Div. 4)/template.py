import heapq


def solve():
    h, n = map(int, input().split())
    damages = list(map(int, input().split()))
    cooldowns = list(map(int, input().split()))

    total_damage = 0
    turn = 0
    cooldown_heap = []

    for i in range(n):
        heapq.heappush(cooldown_heap, (0, damages[i], cooldowns[i]))

    while total_damage < h:
        turn += 1
        current_damage = 0
        next_heap = []

        while cooldown_heap and cooldown_heap[0][0] <= turn:
            available_turn, damage, cooldown = heapq.heappop(cooldown_heap)
            current_damage += damage
            next_available_turn = turn + cooldown
            next_heap.append((next_available_turn, damage, cooldown))

        total_damage += current_damage

        for item in next_heap:
            heapq.heappush(cooldown_heap, item)

    return turn


for _ in range(int(input())):
    print(solve())
