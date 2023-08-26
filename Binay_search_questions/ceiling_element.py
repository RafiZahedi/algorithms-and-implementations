array = [-1, 0, 1, 5, 6, 8, 11, 15, 16, 18]
target = 17
start, end = 0, len(array) - 1


def bin_search(array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    if target >= array[mid]:
        return bin_search(array, mid + 1, end, target)
    return bin_search(array, start, mid - 1, target)


while bin_search(array, start, end, target) == -1 and target <= array[-1]:
    target += 1

print(bin_search(array, start, end, target))