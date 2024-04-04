def solve(s, t):
    # 205. Isomorphic Strings
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


print(solve('bbbaaaba', 'aaabbbba'))
print(solve('egg', 'add'))
print(solve('paper', 'title'))
