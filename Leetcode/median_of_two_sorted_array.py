nums1 = [0, 0, 0, 0, 0]
nums2 = [-1, 0, 0, 0, 0, 0, 1]


def solve():
    arr = nums2 + nums1
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2
    return arr[((len(arr)) // 2)] / 1.0


print(solve())
