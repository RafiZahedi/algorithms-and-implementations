# If you fight for it, you deserve it
# If you deserve it, fight for it     ~ Rafi - SIZ
for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append([start[i], end[i]])
    arr.sort(key=lambda x: x[1])
    jobs = []
    i, j = 0, 1
    jobs.append(arr[0])
    while j < len(arr):
        if arr[i][1] <= arr[j][0]:
            jobs.append(arr[j])
            i = j
        j += 1
    print(len(jobs) , "->" ,jobs )

