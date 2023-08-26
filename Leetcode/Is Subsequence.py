s = "abc"
t = "ahbgdc"


# Ture
def solve(s, t):
    if not len(s):
        return True
    if len(s) > len(t):
        return False
    i, j = 0, 0
    while i < len(t) and j < len(s):
        if s[j] == t[i]:
            j += 1
        i += 1
    return j == len(s)


print(solve(s, t))
