def solve():
    n = int(input())
    string = input()

    symmetric = ""
    st = set()
    for i in range(len(string)):
        if string[i] not in st:
            st.add(string[i])
            symmetric += string[i]

    # have to sort it as well.
    symmetric = ''.join(sorted(symmetric))
    mp = {}
    # two pointer maybe
    left, right = 0, len(symmetric) - 1
    for char in symmetric:
        mp[symmetric[right]] = char
        right -= 1  # shrink from right
        left += 1  # shrink from left

    # convert to list
    result = list(string)
    for left in range(n):
        result[left] = mp[string[left]]

    return ''.join(result)


for _ in range(int(input())):
    print(solve())
