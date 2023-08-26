# If you fight for it, you deserve it
# If you deserve it, fight for it     ~ Rafi - SIZ
n = int(input())
w = int(input())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))
items = []
for i in range(n):
    items.append([values[i], weights[i]])
items.sort(key=lambda items: (items[0] / items[1]), reverse=True)
profit = 0
for i in range(len(items)):
    if items[i][1] <= w:
        profit += items[i][0]
        w -= items[i][1]
    else:
        profit += items[i][0] * w / items[i][1]
        break

print(int(profit))
