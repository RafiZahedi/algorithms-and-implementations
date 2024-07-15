def solve():
    n, a, b = map(int, input().split())
    animals = list(map(int, input().split()))

    for i in range(n):
        predator, prey = 0, 0
        for j in range(n):
            if i == j:
                continue
            # predator chance
            if animals[i] <= animals[j]:
                if (animals[j] - animals[i]) >= a:
                    predator += 1
            # prey chance
            else:
                if (animals[i] - animals[j]) >= b:
                    prey += 1
        print(predator, prey)

for _ in range(1):
    solve()
