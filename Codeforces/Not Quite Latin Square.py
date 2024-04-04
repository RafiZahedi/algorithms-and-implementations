def solve():
    mp = {}
    for _ in range(3):
        row = input()
        for char in row:
            mp[char] = mp.get(char, 0) + 1
    if mp['A'] != 3:
        return 'A'
    if mp['B'] != 3:
        return 'B'
    return 'C'


for _ in range(int(input())):
    print(solve())
