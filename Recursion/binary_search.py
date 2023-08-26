array = [-1, 0, 1, 5, 6, 8, 11, 15]
n = len(array) - 1
left = 0
right = n

while input() == 'y':
    x = int(input("Search for: "))


    def binary_search(array, left, right, x):
        if left > right:
            return 'Not In The Array'
        mid = int((left + right) / 2)
        if array[mid] == x:
            return mid
        if x >= array[mid]:
            return binary_search(array, mid + 1, right, x)
        return binary_search(array, left, mid - 1, x)


    print(binary_search(array, left, right, x))
