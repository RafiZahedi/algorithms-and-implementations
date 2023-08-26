def bin_search(arr, left, right):
    if left == right:
        return arr[left]

    mid = left + (right - left) // 2

    if arr[mid] < arr[mid + 1]:
        return bin_search(arr, mid + 1, right)
    else:
        return bin_search(arr, left, mid)


def wrapper_function(arr):
    return bin_search(arr, 0, len(arr) - 1)


# Test cases
print(wrapper_function([0, 1, 2, 5, 6, 11, 15, 13, 12, 4, 3]))
