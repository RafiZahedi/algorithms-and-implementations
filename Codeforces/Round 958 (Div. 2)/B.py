def solve():
    n = int(input())
    s = input().strip()

    count = [0, 0]
    string = [s[0]]

    for i in range(1, n):
        # we don't need this case
        if s[i] == s[i - 1] and s[i] == '0':
            continue
        string.append(s[i])

    for char in string:
        count[ord(char) - ord('0')] += 1

    if count[1] > count[0]:
        return "YES"
    return "NO"


for _ in range(int(input())):
    print(solve())

# print(solve())
