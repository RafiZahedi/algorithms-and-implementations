# find the number of distinct substrings with length of two
for _ in range(int(input())):
    s = input()
    my_set = set()
    for i in range(len(s) - 1):
        my_set.add(s[i] + s[i+1])
    print(len(my_set))