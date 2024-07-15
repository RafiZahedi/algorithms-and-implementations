def sovle():
    n = int(input())
    layers = list(map(int, input().split()))

    total = 0
    for i in range(1, n):
        total += layers[i] * layers[i-1]

    return total

print(sovle())
